---
source: https://shopify.dev/docs/api/shopify-cli/app
---

# Shopify CLI App commands

[app build

This command executes the build script specified in the element's TOML file.](/docs/api/shopify-cli/app/app-build)[app config link

Pulls app configuration from the Developer Dashboard and creates or overwrites a configuration file.](/docs/api/shopify-cli/app/app-config-link)[app config pull

Pulls the latest configuration from the already-linked Shopify app and updates the selected configuration file.](/docs/api/shopify-cli/app/app-config-pull)[app config use

Sets default configuration when you run app-related CLI commands.](/docs/api/shopify-cli/app/app-config-use)[app deploy

Builds the app, then deploys your app configuration and extensions.](/docs/api/shopify-cli/app/app-deploy)[app dev

Builds and previews your app on a dev store, and watches for changes.](/docs/api/shopify-cli/app/app-dev)[app dev clean

Stop the dev preview that was started with `shopify app dev`.](/docs/api/shopify-cli/app/app-dev-clean)[app env pull

Creates or updates an `.env` files that contains app and app extension environment variables.](/docs/api/shopify-cli/app/app-env-pull)[app env show

Displays environment variables that can be used to deploy apps and app extensions.](/docs/api/shopify-cli/app/app-env-show)[app function build

Compiles the function in your current directory to WebAssembly (Wasm) for testing purposes.](/docs/api/shopify-cli/app/app-function-build)[app function info

The information returned includes the following: - The function handle - The function name - The function API version - The targeting configuration - The schema path - The WASM path - The function runner path](/docs/api/shopify-cli/app/app-function-info)[app function replay

Runs the function from your current directory for testing purposes.](/docs/api/shopify-cli/app/app-function-replay)[app function run

Runs the function from your current directory for testing purposes.](/docs/api/shopify-cli/app/app-function-run)[app function schema

Generates the latest GraphQL schema for a function in your app.](/docs/api/shopify-cli/app/app-function-schema)[app function typegen

Creates GraphQL types based on your input query for a function written in JavaScript.](/docs/api/shopify-cli/app/app-function-typegen)[app generate extension

Generates a new app extension.](/docs/api/shopify-cli/app/app-generate-extension)[app import-custom-data-definitions

Import metafield and metaobject definitions from your development store.](/docs/api/shopify-cli/app/app-import-custom-data-definitions)[app import-extensions

Import dashboard-managed extensions into your app.](/docs/api/shopify-cli/app/app-import-extensions)[app info

The information returned includes the following: - The app and dev store that's used when you run the dev command.](/docs/api/shopify-cli/app/app-info)[app init

Create a new app project](/docs/api/shopify-cli/app/app-init)[app logs

Opens a real-time stream of detailed app logs from the selected app and store.](/docs/api/shopify-cli/app/app-logs)[app logs sources

The output source names can be used with the `--source` argument of `shopify app logs` to filter log output.](/docs/api/shopify-cli/app/app-logs-sources)[app release

Releases an existing app version.](/docs/api/shopify-cli/app/app-release)[app versions list

Lists the deployed app versions.](/docs/api/shopify-cli/app/app-versions-list)[app webhook trigger

Triggers the delivery of a sample Admin API event topic payload to a designated address.](/docs/api/shopify-cli/app/app-webhook-trigger)