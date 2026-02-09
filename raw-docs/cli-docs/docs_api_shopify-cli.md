---
source: https://shopify.dev/docs/api/shopify-cli
---

# Shopify CLI

Shopify CLI is a command-line interface tool that helps you generate and work with Shopify apps, themes and custom storefronts. You can also use it to automate many common development tasks.

Ask assistant

## [Anchor to Requirements](/docs/api/shopify-cli#requirements)Requirements

* [Node.js](https://nodejs.org/en/download/): 20.10 or higher
* A Node.js package manager: [npm](https://www.npmjs.com/get-npm), [Yarn 1.x](https://classic.yarnpkg.com/lang/en/docs/install), or [pnpm](https://pnpm.io/installation).
* [Git](https://git-scm.com/downloads): 2.28.0 or higher

---

## [Anchor to Installation](/docs/api/shopify-cli#installation)Installation

This installs Shopify CLI globally on your system, so you can run `shopify` commands from any directory. Find out more about the available commands by running `shopify` in your terminal.

---

## [Anchor to Commands](/docs/api/shopify-cli#commands)Commands

Shopify CLI groups commands into topics. The command syntax is: `shopify [topic] [command]`.
Refer to each topic section in the sidebar for a list of available commands.

Or, run the `help` command to get this information right in your terminal.

---

## [Anchor to Upgrade Shopify CLI](/docs/api/shopify-cli#upgrade-shopify-cli)Upgrade Shopify CLI

We recommend that you always use the latest version of Shopify CLI if possible. To upgrade, run `version` to check the current version and determine if there are any updates available. Run the [install](#installation) command to upgrade to the latest CLI version.

---

## [Anchor to Network proxy configuration](/docs/api/shopify-cli#network-proxy-configuration)Network proxy configuration

When working behind a network proxy, you can configure Shopify CLI (version 3.78+) to route connections through it:

1. Set the proxy for HTTP traffic:

   9

   1

   export SHOPIFY\_HTTP\_PROXY=http://proxy.com:8080
2. Optionally, set a different proxy for HTTPS traffic:

   9

   1

   export SHOPIFY\_HTTPS\_PROXY=https://secure-proxy.com:8443

   If not specified, the HTTP proxy will be used for all traffic.
3. For authenticated proxies, include credentials in the URL:

   9

   1

   export SHOPIFY\_HTTP\_PROXY=http://username:password@proxy.com:8080

---

## [Anchor to Usage reporting](/docs/api/shopify-cli#usage-reporting)Usage reporting

Anonymous usage statistics are collected by default. To opt out, you can use the environment variable `SHOPIFY_CLI_NO_ANALYTICS=1`.

---

## [Anchor to Contribute to Shopify CLI](/docs/api/shopify-cli#contribute-to-shopify-cli)Contribute to Shopify CLI

Shopify CLI is open source. [Learn how to contribute](https://github.com/Shopify/cli/wiki/Contributors:-Introduction) to our GitHub repository.

---

## [Anchor to Where to get help](/docs/api/shopify-cli#where-to-get-help)Where to get help

* [Shopify CLI and Libraries](https://community.shopify.dev/c/shopify-cli-libraries/14) - Report any issues with the CLI.
* [Dev Platform](https://community.shopify.dev/c/dev-platform/32) - Ask any questions and learn more about the Dev Platform powering the CLI.

---

## [Anchor to Resources](/docs/api/shopify-cli#resources)Resources

[![](/images/icons/32/pickaxe-1.png)![](/images/icons/32/pickaxe-1-dark.png)

Start building a theme

Learn how to set up your theme development environment and create a new theme

Start building a theme

Learn how to set up your theme development environment and create a new theme](/docs/themes/getting-started/create)

[Start building a theme](/docs/themes/getting-started/create)

[![](/images/icons/32/tutorial.png)![](/images/icons/32/tutorial-dark.png)

Start building an app

Learn how to set up your app development environment and start building

Start building an app

Learn how to set up your app development environment and start building](/docs/apps/getting-started/create)

[Start building an app  
  

Learn how to set up your app development environment and start building](/docs/apps/getting-started/create)

---

Was this page helpful?

YesNo