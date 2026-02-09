---
source: https://shopify.dev/docs/api/liquid/filters/external_video_url
---

9

1

media | external\_video\_url: attribute: string

returns [string](/docs/api/liquid/basics#string)

Returns the URL for a given external video. Use this filter to specify parameters for the external video player generated
by the [`external_video_tag` filter](/docs/api/liquid/filters/external_video_tag).

You can specify [YouTube](https://developers.google.com/youtube/player_parameters#Parameters) and [Vimeo](https://vimeo.zendesk.com/hc/en-us/articles/360001494447-Using-Player-Parameters) video parameters by adding a parameter that matches the parameter name, and the desired value.

9

1

2

3

4

5

6

7

8

9

{% for media in product.media %}

{% if media.media\_type == 'external\_video' %}

{% if media.host == 'youtube' %}

{{ media | external\_video\_url: color: 'white' | external\_video\_tag }}

{% elsif media.host == 'vimeo' %}

{{ media | external\_video\_url: loop: '1', muted: '1' | external\_video\_tag }}

{% endif %}

{% endif %}

{% endfor %}

##### Code

```liquid
{% for media in product.media %}
  {% if media.media_type == 'external_video' %}
    {% if media.host == 'youtube' %}
      {{ media | external_video_url: color: 'white' | external_video_tag }}
    {% elsif media.host == 'vimeo' %}
      {{ media | external_video_url: loop: '1', muted: '1' | external_video_tag }}
    {% endif %}
  {% endif %}
{% endfor %}
```

##### Data

```liquid
{
  "product": {
    "media": [
      {
        "host": "youtube",
        "media_type": "external_video"
      },
      {
        "host": null,
        "media_type": "video"
      }
    ]
  }
}
```

## Output

9

1

<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" src="https://www.youtube.com/embed/vj01PAffOac?color=white&amp;controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>

##### Output

```liquid
<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" src="https://www.youtube.com/embed/vj01PAffOac?color=white&amp;controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>
```

Was this page helpful?

YesNo