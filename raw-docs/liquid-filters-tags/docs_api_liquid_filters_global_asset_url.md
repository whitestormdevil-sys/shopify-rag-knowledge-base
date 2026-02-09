---
source: https://shopify.dev/docs/api/liquid/filters/global_asset_url
---

9

1

string | global\_asset\_url

returns [string](/docs/api/liquid/basics#string)

Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn) for a global asset.

Global assets are kept in a directory on Shopify's server. Using global assets can be faster than loading the resource
directly.

Depending on the resource type, you might need to use an additional filter to load the resource. The following table
outlines which filter to use for specific resource types.

| Resource type | Additional filter |
| --- | --- |
| JavaScript (`.js`) | [`script_tag`](/docs/api/liquid/filters/script_tag) |
| CSS (`.css`) | [`stylesheet_tag`](/docs/api/liquid/filters/stylesheet_tag) |

The following table outlines the available global assets:

| Category | Assets |
| --- | --- |
| Firebug | - `firebug/firebug.css` - `firebug/firebug.html` - `firebug/firebug.js` - `firebug/firebugx.js` - `firebug/errorIcon.png` - `firebug/infoIcon.png` - `firebug/warningIcon.png` |
| JavaScript libraries | - `controls.js` - `dragdrop.js` - `effects.js` - `ga.js` - `mootools.js` |
| Lightbox | - `lightbox.css` - `lightbox.js`  - `lightbox/v1/lightbox.css` - `lightbox/v1/lightbox.js`  - `lightbox/v2/lightbox.css` - `lightbox/v2/lightbox.js` - `lightbox/v2/close.gif` - `lightbox/v2/loading.gif` - `lightbox/v2/overlay.png` - `lightbox/v2/zoom-lg.gif`  - `lightbox/v204/lightbox.css` - `lightbox/v204/lightbox.js` - `lightbox/v204/bullet.gif` - `lightbox/v204/close.gif` - `lightbox/v204/closelabel.gif` - `lightbox/v204/donatebutton.gif` - `lightbox/v204/downloadicon.gif` - `lightbox/v204/loading.gif` - `lightbox/v204/nextlabel.png` - `lightbox/v204/prevlabel.gif` |
| Prototype | - `prototype.js` - `prototype/1.5/prototype.js` - `prototype/1.6/prototype.js` |
| script.aculo.us | - `scriptaculous/1.8.2/scriptaculous.js` - `scriptaculous/1.8.2/builder.js` - `scriptaculous/1.8.2/controls.js` - `scriptaculous/1.8.2/dragdrop.js` - `scriptaculous/1.8.2/effects.js` - `scriptaculous/1.8.2/slider.js` - `scriptaculous/1.8.2/sound.js` - `scriptaculous/1.8.2/unittest.js` |
| Shopify | - `list-collection.css` - `textile.css` |

9

1

2

3

{{ 'lightbox.js' | global\_asset\_url | script\_tag }}

{{ 'lightbox.css' | global\_asset\_url | stylesheet\_tag }}

##### Code

```liquid
{{ 'lightbox.js' | global_asset_url | script_tag }}

{{ 'lightbox.css' | global_asset_url | stylesheet_tag }}
```

## Output

9

1

2

3

<script src="//polinas-potent-potions.myshopify.com/cdn/s/global/lightbox.js" type="text/javascript"></script>

<link href="//polinas-potent-potions.myshopify.com/cdn/s/global/lightbox.css" rel="stylesheet" type="text/css" media="all" />

##### Output

```liquid
<script src="//polinas-potent-potions.myshopify.com/cdn/s/global/lightbox.js" type="text/javascript"></script>

<link href="//polinas-potent-potions.myshopify.com/cdn/s/global/lightbox.css" rel="stylesheet" type="text/css" media="all" />
```

Was this page helpful?

YesNo