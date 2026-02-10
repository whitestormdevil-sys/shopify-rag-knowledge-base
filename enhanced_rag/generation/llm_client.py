"""
ShopifyAI LLM Client — Bedrock API wrapper for multi-model architecture.

Handles:
- Model routing (role → correct Claude model)
- Bedrock API calls (Messages API with streaming)
- Extended Thinking toggle
- Prompt caching (system prompt cache control)
- Token counting and cost tracking
"""

import json
import time
import logging
from dataclasses import dataclass, field
from typing import Optional, Generator

import boto3

logger = logging.getLogger(__name__)


@dataclass
class LLMResponse:
    """Response from an LLM call."""
    content: str                    # The text response
    thinking: Optional[str] = None  # Extended thinking content (if enabled)
    model_id: str = ""
    input_tokens: int = 0
    output_tokens: int = 0
    thinking_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0
    latency_ms: int = 0
    cost_estimate: float = 0.0
    role: str = ""


# ── Pricing (per 1K tokens) ─────────────────────────────────────────────────

PRICING = {
    "anthropic.claude-haiku-4-5-20251001-v1:0": {
        "input": 0.001, "output": 0.005, "cache_read": 0.0001, "cache_write": 0.00125,
    },
    "anthropic.claude-sonnet-4-5-20250929-v1:0": {
        "input": 0.003, "output": 0.015, "cache_read": 0.0003, "cache_write": 0.00375,
    },
    "anthropic.claude-opus-4-6-v1": {
        "input": 0.005, "output": 0.025, "cache_read": 0.0005, "cache_write": 0.00625,
    },
}


class LLMClient:
    """Multi-model Bedrock client with prompt caching and cost tracking."""
    
    def __init__(self, region: str = "us-east-1"):
        self.bedrock = boto3.client(
            "bedrock-runtime",
            region_name=region,
        )
        self.total_cost = 0.0
        self.call_history: list[LLMResponse] = []
    
    def call(
        self,
        role: str,
        system_prompt: str,
        user_message: str,
        model_id: str,
        max_tokens: int = 4096,
        temperature: float = 0.4,
        extended_thinking: bool = False,
        thinking_budget: int = 10000,
        cache_system: bool = True,
    ) -> LLMResponse:
        """Make a single LLM call to Bedrock.
        
        Args:
            role: Agent role name (for logging/tracking)
            system_prompt: System prompt text
            user_message: User message text
            model_id: Bedrock model identifier
            max_tokens: Maximum output tokens
            temperature: Sampling temperature (ignored if thinking=True)
            extended_thinking: Enable extended thinking
            thinking_budget: Max thinking tokens
            cache_system: Whether to cache the system prompt
        """
        start_time = time.time()
        
        # ── Build system block ──
        system_blocks = [{
            "type": "text",
            "text": system_prompt,
        }]
        if cache_system:
            system_blocks[0]["cacheControl"] = {"type": "ephemeral"}
        
        # ── Build messages ──
        messages = [{"role": "user", "content": user_message}]
        
        # ── Build request body ──
        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "system": system_blocks,
            "messages": messages,
            "max_tokens": max_tokens,
        }
        
        # ── Extended Thinking ──
        if extended_thinking:
            body["thinking"] = {
                "type": "enabled",
                "budget_tokens": thinking_budget,
            }
            # Temperature must be 1.0 with thinking
            body["temperature"] = 1.0
        else:
            body["temperature"] = temperature
        
        # ── API Call ──
        try:
            response = self.bedrock.invoke_model(
                modelId=model_id,
                contentType="application/json",
                accept="application/json",
                body=json.dumps(body),
            )
            
            result = json.loads(response["body"].read())
            
        except Exception as e:
            logger.error(f"[{role}] Bedrock API error: {e}")
            raise
        
        latency_ms = int((time.time() - start_time) * 1000)
        
        # ── Parse response ──
        content = ""
        thinking = None
        
        for block in result.get("content", []):
            if block["type"] == "text":
                content = block["text"]
            elif block["type"] == "thinking":
                thinking = block["thinking"]
        
        # ── Token usage ──
        usage = result.get("usage", {})
        input_tokens = usage.get("input_tokens", 0)
        output_tokens = usage.get("output_tokens", 0)
        
        # Cache tokens from Bedrock response headers
        cache_read = usage.get("cache_read_input_tokens", 0)
        cache_write = usage.get("cache_creation_input_tokens", 0)
        
        # Thinking tokens (part of output)
        thinking_tokens = 0
        if thinking:
            # Rough estimate: ~4 chars per token
            thinking_tokens = len(thinking) // 4
        
        # ── Cost calculation ──
        pricing = PRICING.get(model_id, {"input": 0.005, "output": 0.025, "cache_read": 0.0005, "cache_write": 0.00625})
        
        cost = (
            (input_tokens - cache_read - cache_write) * pricing["input"] / 1000
            + cache_read * pricing["cache_read"] / 1000
            + cache_write * pricing["cache_write"] / 1000
            + output_tokens * pricing["output"] / 1000
        )
        
        self.total_cost += cost
        
        # ── Build response ──
        llm_response = LLMResponse(
            content=content,
            thinking=thinking,
            model_id=model_id,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            thinking_tokens=thinking_tokens,
            cache_read_tokens=cache_read,
            cache_write_tokens=cache_write,
            latency_ms=latency_ms,
            cost_estimate=cost,
            role=role,
        )
        
        self.call_history.append(llm_response)
        
        logger.info(
            f"[{role}] {model_id.split('.')[-1][:20]} | "
            f"{input_tokens}→{output_tokens} tokens | "
            f"cache_r={cache_read} cache_w={cache_write} | "
            f"${cost:.4f} | {latency_ms}ms"
        )
        
        return llm_response
    
    def get_cost_summary(self) -> dict:
        """Get cost breakdown by role."""
        summary = {"total": self.total_cost, "calls": len(self.call_history), "by_role": {}}
        for resp in self.call_history:
            if resp.role not in summary["by_role"]:
                summary["by_role"][resp.role] = {"cost": 0, "calls": 0, "tokens_in": 0, "tokens_out": 0}
            summary["by_role"][resp.role]["cost"] += resp.cost_estimate
            summary["by_role"][resp.role]["calls"] += 1
            summary["by_role"][resp.role]["tokens_in"] += resp.input_tokens
            summary["by_role"][resp.role]["tokens_out"] += resp.output_tokens
        return summary
