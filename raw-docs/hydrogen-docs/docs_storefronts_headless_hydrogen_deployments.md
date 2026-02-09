---
source: https://shopify.dev/docs/storefronts/headless/hydrogen/deployments
---

A deployment is an [immutable](#deployment-immutability) snapshot of your Hydrogen app, running on Oxygen. Every deployment has its own unique preview URL so that you can view, test, or approve changes before merging them and deploying to production. You can also deploy to specific [environments](/docs/storefronts/headless/hydrogen/environments).

---

## [Anchor to Continuous deployment](/docs/storefronts/headless/hydrogen/deployments#continuous-deployment)Continuous deployment

Developers typically prefer automated systems that deploy their app whenever they update its code base. These types workflows are broadly known as continuous integration or continuous delivery/deployment (CI/CD) systems.

Hydrogen and Oxygen support [CI/CD with GitHub](/docs/storefronts/headless/hydrogen/deployments/github) out of the box. You can also [create your own CI/CD workflows](/docs/storefronts/headless/hydrogen/deployments/custom-ci-cd) using the Hydrogen CLI.

[![](/images/icons/48/github.png)![](/images/icons/48/github-dark.png)

Deploy with GitHub (recommended)

Automatically create deployments whenever you merge or push changes to your connected GitHub repo.

Deploy with GitHub (recommended)

Automatically create deployments whenever you merge or push changes to your connected GitHub repo.](/docs/storefronts/headless/hydrogen/deployments/github)

[Deploy with GitHub (recommended)  
  

Automatically create deployments whenever you merge or push changes to your connected GitHub repo.](/docs/storefronts/headless/hydrogen/deployments/github)

[![](/images/icons/48/gear.png)![](/images/icons/48/gear-dark.png)

Custom CI/CD

Configure your own advanced CI/CD workflows, such as deploying from BitBucket or GitLab.

Custom CI/CD

Configure your own advanced CI/CD workflows, such as deploying from BitBucket or GitLab.](/docs/storefronts/headless/hydrogen/deployments/custom-ci-cd)

[Custom CI/CD  
  

Configure your own advanced CI/CD workflows, such as deploying from BitBucket or GitLab.](/docs/storefronts/headless/hydrogen/deployments/custom-ci-cd)

---

## [Anchor to Manual deployment](/docs/storefronts/headless/hydrogen/deployments#manual-deployment)Manual deployment

You can create a new deployment from your local development environment with the Hydrogen CLI `deploy` command. The Hydrogen CLI builds, uploads, and deploys your app, then returns the deployment's unique URL.

$

$

npx shopify hydrogen deploy

Consult the Hydrogen CLI reference for the complete list of options for the [`deploy`](/docs/api/shopify-cli/hydrogen/hydrogen-deploy) command.

---

## [Anchor to Shareable links](/docs/storefronts/headless/hydrogen/deployments#shareable-links)Shareable links

Deployments are private by default, which means that you need to be logged in to your store to view them. If your store is on the Basic plan or above, then you can create shareable links that let anyone view deployments, even if they’re not logged in.

Be aware of the following when you use shareable links:

* Shareable links are URLs that include a token that bypasses the deployment's login requirement. Be sure to give shareable links only to people you trust.
* Making changes to a shareable link takes up to 30 seconds.
* Oxygen blocks search engines from indexing shared deployments with a `disallow` rule on the deployment's `robots.txt` file. This prevents potential harm to SEO caused by duplicated content.

### [Anchor to Create a shareable link](/docs/storefronts/headless/hydrogen/deployments#create-a-shareable-link)Create a shareable link

1. In your Hydrogen storefront, open the deployment details page for the deployment that you want to update.
2. Click **Share**.
3. Select **Anyone with the link**.
4. Click **Copy link** to copy the shareable link to your clipboard.
5. Click **Close**.

### [Anchor to Reset a shareable link](/docs/storefronts/headless/hydrogen/deployments#reset-a-shareable-link)Reset a shareable link

Resetting a shareable link revokes its existing token and creates a new one. The old link will stop working and people will need to use the new shareable link to view the deployment.

1. In your Hydrogen storefront, open the deployment details page for the deployment that you want to update.
2. Click **Share**.
3. Click **Reset link**.
4. Click **Reset** to confirm.
5. Click **Copy link** to copy the new link.
6. Click **Close**.

### [Anchor to Remove a shareable link](/docs/storefronts/headless/hydrogen/deployments#remove-a-shareable-link)Remove a shareable link

Removing a shareable link revokes its existing token, which returns the deployment to its default state, meaning it's accessible only to logged-in staff.

1. In your Hydrogen storefront, open the deployment details page for the deployment to update.
2. Click **Share**.
3. Click **Staff accounts only**.
4. Click **Close**.

---

## [Anchor to Deployment rollbacks](/docs/storefronts/headless/hydrogen/deployments#deployment-rollbacks)Deployment rollbacks

By default, [environment URLs](/docs/storefronts/headless/hydrogen/environments#environment-urls) point to the environment’s most recent deployment.

If the most recent update contains a bug or other error, you can temporarily roll back to a previous deployment while you work on a fix. Rolling back doesn't redeploy or delete any deployments; it simply changes which deployment the environment URL points to.

Caution

Oxygen deployments are [immutable](#deployment-immutability), which means that their environment variables could be outdated. Always verify that a previous deployment works as expected before rolling back to it.

**Caution:**

Oxygen deployments are [immutable](#deployment-immutability), which means that their environment variables could be outdated. Always verify that a previous deployment works as expected before rolling back to it.

### [Anchor to Roll back to a previous deployment](/docs/storefronts/headless/hydrogen/deployments#roll-back-to-a-previous-deployment)Roll back to a previous deployment

Only production and custom environments can be rolled back.

1. On your Hydrogen storefront overview page, click `…` on the environment to roll back.
2. Click **View deployments**.
3. In the list of deployments, click `…` beside the deployment to roll back to.
4. Click **Make this the current deployment**.
5. Click **Make current for {Environment}** to confirm.

The next time that you push an update to its linked branch, the environment will return to the default behavior of pointing to the most recent deployment.

---

## [Anchor to Redeployments](/docs/storefronts/headless/hydrogen/deployments#redeployments)Redeployments

Redeploying an Oxygen environment creates a new deployment that re-uses the original deployment's [immutable](#deployment-immutability) code, but injects the current set of [environment variables](/docs/storefronts/headless/hydrogen/environments#environment-variables).

Redeployments are available for production and custom environments, but not the preview environment. When you edit an environment variable in the Shopify admin, you'll be prompted with the option to redeploy the relevant environments, but you can redeploy at any time.

### [Anchor to Redeploy an environment](/docs/storefronts/headless/hydrogen/deployments#redeploy-an-environment)Redeploy an environment

Redeploying an environment redeploys its current deployment only. Older deployments in that environment aren’t redeployed.

1. On the storefront overview page, click the three dots in the upper right of the environment you want to redeploy.
2. Click **Redeploy environment**.
3. Click **Redeploy** to confirm.

---

## [Anchor to Deployment immutability](/docs/storefronts/headless/hydrogen/deployments#deployment-immutability)Deployment immutability

Every deployment in Oxygen is immutable: each deployment is a snapshot of your Hydrogen project's codebase at a specific point in time. Typically, that snapshot is an individual Git commit.

Deployments retain all the [environment variables](/docs/storefronts/headless/hydrogen/environments#environment-variables) that they had when they were first deployed. If you update your environment variables, then older deployments won't use the updated values until you [redeploy](#redeployments).

---

## [Anchor to Deployment retention policy](/docs/storefronts/headless/hydrogen/deployments#deployment-retention-policy)Deployment retention policy

Oxygen's data retention policy is designed to ensure that your Hydrogen storefront is always available to customers, and that you can always [roll back](#deployment-rollbacks) to a previous deployment in case of error.

Oxygen deployments remain accessible for a minimum of six months. After that time, deployments are deleted, including their bundled worker files, logs, and preview URLs.

Your ten most recent Oxygen deployments per environment always remain accessible, regardless of how old they are.

### [Anchor to Log data retention](/docs/storefronts/headless/hydrogen/deployments#log-data-retention)Log data retention

Deployments' runtime logging data is available for up to one month. If you need to retain logging data for longer than that, then consider connecting a [log drain](/docs/storefronts/headless/hydrogen/logging).

---

Was this page helpful?

YesNo