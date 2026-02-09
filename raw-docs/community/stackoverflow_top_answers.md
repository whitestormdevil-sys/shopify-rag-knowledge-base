---
source: Stack Overflow - Top Shopify Answers
---

# Top Shopify Answers from Stack Overflow

## Q: What&#39;s the cause of the error &#39;getaddrinfo EAI_AGAIN&#39;?
**Score:** 375 | https://stackoverflow.com/questions/40182121/whats-the-cause-of-the-error-getaddrinfo-eai-again

### Answer (Score: 285, Accepted: True)
EAI\_AGAIN is a DNS lookup timed out error, means it is a network connectivity error or proxy related error.

> My main question is what does dns.js do?

* The dns.js is there for node to get ip address of the domain(in brief).

Some more info:
<http://www.codingdefined.com/2015/06/nodejs-error-errno-eaiagain.html>

### Answer (Score: 215, Accepted: False)
If you get this error with Firebase Cloud Functions, this is due to the limitations of the free tier (*outbound networking only allowed to Google services*).

Upgrade to the **Flame** or **Blaze** plans for it to work.

[![enter image description here](https://i.sstatic.net/DoCWy.png)](https://i.sstatic.net/DoCWy.png)

---

## Q: Convert string to integer in Shopify Liquid?
**Score:** 58 | https://stackoverflow.com/questions/27198710/convert-string-to-integer-in-shopify-liquid

### Answer (Score: 114, Accepted: True)
Using `assign` with a math filter is correct. [See this thread on GitHub](https://github.com/Shopify/liquid/issues/130#issuecomment-19166529), and [this blog post](http://www.tetchi.ca/liquids-capture-tag-and-numbers/).

[Variables created through `{% capture %}` are strings](http://docs.shopify.com/themes/liquid-documentation/tags/variable-tags#capture). When using `assign`, either of these options should give you a number:

```
{% assign var1 = var1 | plus: 0 %}
{% assign var2 = var2 | times: 1 %}
```

If this doesn't work for you, can you post the relevant code?

### Answer (Score: -3, Accepted: False)
In Shopify Liquid programming language, you can convert a string to an integer using the `to_i` filter.

For example, if you have a variable `string_number` that contains a string representation of a number, you can convert it to an integer using the following code:

```
{{ string_number | to_i }}
```

It will convert the string to integer and you can use it in mathematical calculations, comparisons and other operations that work with integers.

For example, you could use the `to_i` filter to add two numbers together:

```
{% assign number_1 = "5" %}
{% assign number_2 = "2" %}
{% assign result = number_1 | to_i + number_2 | to_i %}
{{ result }}
```

This will output: 7

Please note that this filter will return 0 if the string is not a valid number.

[Source](https://dezefy.com/2023/01/18/how-to-convert-string-to-integer-in-shopify-liquid/)

---

## Q: Enabling Liquid templating syntax highlight in webStorm/phpStorm
**Score:** 48 | https://stackoverflow.com/questions/29123188/enabling-liquid-templating-syntax-highlight-in-webstorm-phpstorm

### Answer (Score: 133, Accepted: True)
I've found out that Twig have a very similar syntax to Liquid, enabling the Twig plugin will highlight Liquid syntax and will keep the HTML highlight/autocomplete/emmet functionality working as opposed to the "textMate Liquid bundle".

Go to `Settings > Editor > File Types` find "Twig" on that list and associate Liquid files with it by adding `*.liquid` to the registered patterns section.

If you can't find Twig, download the official plugin from the "Browse repositores" or in the "install JetBrains plugin". If you can't find it there then download the plugin and install it manually by pressing "install plugin from disk": <https://plugins.jetbrains.com/plugin/7303?pr=>

You will also want to associate `*.scss.liquid` to `.scss` files,
`*.css.liquid` to `.css` files and `*.js.liquid` to `.js` files so that Twig wouldn't run on those type of files.

The end result works like a charm! it's the best solution yet until some official plugin will come out

### Answer (Score: 8, Accepted: False)
To follow up on [Ilia luk's answer](https://stackoverflow.com/a/29337624), PHP Storm now has Twig support built in—just enable the plug-in if it isn't already.

---

## Q: webpack-merge merge is not a function
**Score:** 42 | https://stackoverflow.com/questions/62851934/webpack-merge-merge-is-not-a-function

### Answer (Score: 105, Accepted: True)
In a new version of [webpack-merge,](https://www.npmjs.com/package/webpack-merge) It is imported like below.

```
const { merge } = require('webpack-merge');
```

### Answer (Score: 15, Accepted: False)
As from version 5 of [webpack-merge](https://github.com/survivejs/webpack-merge), the merge function is now named export instead of a default export.

**Before version 5**

```
const merge = require('webpack-merge');
```

**From version 5**

```
const merge = require('webpack-merge').merge;
```

```
// or
```

```
const { merge } = require('webpack-merge');
```

**If you are using ES modules, then you should do as:**

```
import { merge } from "webpack-merge"
```

---

## Q: FlashList&#39;s rendered size is not usable
**Score:** 34 | https://stackoverflow.com/questions/73516978/flashlists-rendered-size-is-not-usable

### Answer (Score: 35, Accepted: True)
I had the same issue and a warning `FlashList rendered size is not useable` and the screen was blank .

According to [FlashList docs](https://shopify.github.io/flash-list/docs/known-issues/) we should use it inside a wrapper like `View` with hardcoded height style number like this :

```
<View style={{ height: 200, width: Dimensions.get("screen").width }}>
    <FlashList
       data={DATA}
       renderItem={({ item }) => <Text>{item.title}</Text>}
       estimatedItemSize={200}
    />
</View>
```

If I was in your shoes I would make a simple flashlist work perfectly fine then I'd implement the list I want and add more to it .

This fixed my problem . Hope you make it work .

### Answer (Score: 13, Accepted: False)
From the docs:

> ...So, make sure that the parent of the list mounts with a valid size (>=2px) and FlashList will match the size of its parent. ...

So, I decided to wrap the *FlashList* into a *View* and set *minHeight* property to 2, which satisfies the statement from the docs.

```
<View style={{minHeight: 2}}>
    <FlashList ... /> 
</View>
```

As a result, the warning went away.

---

## Q: How do I set up a session value in Capybara?
**Score:** 33 | https://stackoverflow.com/questions/8546839/how-do-i-set-up-a-session-value-in-capybara

### Answer (Score: 33, Accepted: False)
The accepted answer suggests [rack\_session\_access](https://github.com/railsware/rack_session_access). It works by inserting middleware controllers to edit and update the session state, then has capybara visit that page and submit a form with the session data. Very ingenious! But unnecessary if you are using Warden (directly or through Devise).

Warden has a hook [on\_next\_request](https://github.com/hassox/warden/wiki/Testing) that gives access to the warden mechanism, which can be used to set session keys directly. I threw this together to bundle it up in rspec:

Create `spec/support/inject_session.rb`:

```
module InjectSession
  include Warden::Test::Helpers

  def inject_session(hash)
    Warden.on_next_request do |proxy|
      hash.each do |key, value|
        proxy.raw_session[key] = value
      end
    end
  end
end
```

In `spec/spec_helper.rb` include the module in feature specs:

```
RSpec.configure do |config|
    config.include InjectSession, :type => :feature
end
```

Then sample use in a spec might be:

```
   inject_session :magic => 'pixie dust', :color => 'pink' 
   visit shopping_cart_path
   page.should be_all_sparkly_and_pink # or whatever
```

### Answer (Score: 27, Accepted: True)
Just found [rack\_session\_access](https://github.com/railsware/rack_session_access) gem and working as a charm.

---

## Q: Adding custom CSS and JS to Shopify
**Score:** 29 | https://stackoverflow.com/questions/20467240/adding-custom-css-and-js-to-shopify

### Answer (Score: 46, Accepted: True)
Simply upload your `filename.js` file in the **assets** folder.

then drop the following in your `theme.liquid` **head** section:

```
{{ 'filename.js' | asset_url | script_tag }}
```

by the way, you should **rename your file and add .liquid extension**

```
filename.js.liquid
```

Good luck!

### Answer (Score: 45, Accepted: False)
If I understand correctly, the [asset\_url filter](http://docs.shopify.com/themes/filters/asset-url) is what you are looking for.

To include a JS file in a .liquid file, you use:

```
{{ 'script.js' | asset_url | script_tag }}
```

And a CSS file:

```
{{ 'style.css' | asset_url | stylesheet_tag }}
```

---

## Q: Shopify Theme with Compass and Sass
**Score:** 29 | https://stackoverflow.com/questions/11237792/shopify-theme-with-compass-and-sass

### Answer (Score: 23, Accepted: True)
I'm not familiar with Shopify or liquid tags, but I do know that in SASS you can use [interpolations](http://sass-lang.com/docs/yardoc/file.SASS_REFERENCE.html#interpolation_) to output plain CSS as-is. For example, the SASS here:

```
.test {
    background: url( #{'{{ "splash-1.jpg" | asset_url }}'} )
}
```

Would be compiled to:

```
.test {
    background: url({{ "splash-1.jpg" | asset_url }}); }
```

Does that get you close to what you're looking for?

### Answer (Score: 10, Accepted: False)
How do you keep Compass from barfing on liquid logic between properties? E.g. any time there's a liquid `if` statement I get errors, and using `#{'...'}` doesn't seem to help.

This is a test I can't get to work:

```
#container {
  width:884px;
  margin:0px auto;
  min-height:500px;
  position:relative;
  padding:0 40px;
  {% if settings.page_bg_transparent %}
    background:transparent;
  {% else %}
    background:{{ settings.page_bg_color }};
  {% endif %}
}
```

**UPDATE** weirdly, commenting liquid logic works:

```
#container {
  width:884px;
  margin:0px auto;
  min-height:500px;
  position:relative;
  padding:0 40px; 
  /* {% if settings.page_bg_transparent %} */
    background:transparent;
  /* {% else %} */
    background:#{'{{ settings.page_bg_color }}'}; 
  /* {% endif %} */
}
```

---

## Q: Accessing API works fine with cURL but not with Fetch API
**Score:** 29 | https://stackoverflow.com/questions/53506848/accessing-api-works-fine-with-curl-but-not-with-fetch-api

### Answer (Score: 1, Accepted: False)
**Why? explained:**

The CORS policy is implemented *in browsers* to allow sharing resources between websites while preventing websites from attacking each other:

* [SOP (same origin policy)](https://portswigger.net/web-security/cors/same-origin-policy) prevents web sites from attacking each other but does not allow any sharing between origins.
* [CORS (cross origin resource sharing)](https://portswigger.net/web-security/cors) relaxes SOP restrictions, but requires specific server headers/configuration.

These policies only apply inside a browser. Presumably cURL works because it is making direct HTTP requests outside the context of a browser script. Which leads to how to work-around CORS restrictions...

**Solutions:**

[3 Ways to Fix the CORS Error — and How the Access-Control-Allow-Origin Header Works](https://medium.com/@dtkatz/3-ways-to-fix-the-cors-error-and-how-access-control-allow-origin-works-d97d55946d9) explains how to bypass CORS restrictions. They all work by manipulating the request headers/origin:

1. Browser extension. (Not sure if this still works in 2022. Only works if user installs browser extension.)
2. 3rd party request proxy. (The proxy linked in the demo is now limited due to abuse.)
3. Build your own proxy.

Realistically, option #3 is the only real solution. [SvelteKit endpoints](https://kit.svelte.dev/docs/routing) make it super simple to proxy requests.

### Answer (Score: 0, Accepted: False)
You have to use FormData instead of JSON.

```
    var data = new FormData();
    data.append('key', 'value');

    fetch('api', {
    method: 'POST',
    body: data,
    })
    .then(response => response.json())
    .then(data => {
    console.log(data);
    });
```

---

## Q: How do I retrieve a specific product in Shopify Liquid?
**Score:** 28 | https://stackoverflow.com/questions/13269125/how-do-i-retrieve-a-specific-product-in-shopify-liquid

### Answer (Score: 40, Accepted: True)
You can now retrieve a product via a handle using the following:

```
{% assign someProduct = all_products.some-handle %}
```

[Documentation](https://shopify.dev/docs/api/liquid/objects/all_products)

### Answer (Score: 10, Accepted: False)
Just to update for anyone just finding this, you can now reference products directly via handle by `all_products['handle']` as per [this response](https://github.com/Shopify/liquid/issues/438#issuecomment-108981467) on their Shopify/liquid repo.

---

## Q: Date Math / Manipulation in Liquid Template Filter
**Score:** 27 | https://stackoverflow.com/questions/21056965/date-math-manipulation-in-liquid-template-filter

### Answer (Score: 65, Accepted: True)
**Much thanks to [@iveskev](https://twitter.com/iveskev) from the Desk.com "WOW" team for this answer:**

If you do `{{'now'}}` it returns the string “now” not a timestamp for the current time. So if you do `{{'now' | minus: 604800 }}` it returns “-604800” not the current unix time minus 604800. When you use the `date` filter, then liquid picks up that you are referencing the current time and outputs the time as a string. However even if we get ‘now’ to output the current date, we are still subtracting from a string and so will be returned with “-604800”. The only time that math on a string works correctly is if the sting is only a number.

So in order to get the correct date we first have to get the unix timestamp for now, do the subtraction, then reformat to the desired formate. You can use `%s` to get unix time. So to get the current time in unix it would be:
`{{'now' | date: '%s' }}`

At that point you can then do the subtraction and then format the time in the correct way. We can do this all at once in the following statement:

`{{'now' | date: "%s" | minus : 604800 | date: "%b %d, %Y %I:%M %p -0500" | uri_encode | replace:"+","%20"}}`

### Answer (Score: 0, Accepted: False)
for those using liquidjs I couldn't find a way without having a new filter, so I made one:

```
daysAgo = (input) ->
  date = new Date()
  date.setDate(date.getDate() - parseInt(input, 10))
  date

parser.registerFilter('days_ago', (value) -> daysAgo(value))
```

then doing:

```
{{ 1 | day_ago | date "%Y-%m-%d" }}
2019-05-02
```

I've posted an issue on the liquidjs repo: <https://github.com/harttle/liquidjs/issues/125>

---

## Q: Print_r equivalent in Liquid
**Score:** 24 | https://stackoverflow.com/questions/6174665/print-r-equivalent-in-liquid

### Answer (Score: 45, Accepted: True)
Ah got there in the end! Not quite a print\_r, but near enough to see whats available. This prints out the properties in JSON format, so you can see whats in there.

```
{{item | json}}
```

---

## Q: How to develop Shopify themes locally?
**Score:** 24 | https://stackoverflow.com/questions/38803486/how-to-develop-shopify-themes-locally

### Answer (Score: 22, Accepted: True)
There are quite a few workflows you can use here.

# 1. Task runners

If you're using either Gulp or Grunt locally for development, there are libraries out there that will upload your files to the store through API credentials of a Private App that you have to create. Most work by uploading the files you change, using a watcher.

1. [**grunt-shopify**](https://github.com/wilr/grunt-shopify)
2. [**grunt-shopify-upload**](https://github.com/ryanburnette/grunt-shopify-theme)
3. [**gulp-shopify-upload**](https://github.com/mikenorthorp/gulp-shopify-upload) (it's my favourite since I use Gulp but has a known issue that sometimes it stops uploading files and you have to restart it).

# 2. Official Shopify Theme Kit

**Theme Kit** is a cross-platform CLI tool that was built by Shopify Employees. It can run on windows/linux/OS X. You can read more about it [on Shopify Blog](https://www.shopify.com/partners/blog/95401862-3-simple-steps-for-setting-up-a-local-shopify-theme-development-environment) or [download it directly](http://themekit.cat/). The alternative previously mentioned of Desktop Theme Editor is deprecated and has been replaced by Theme Kit.

# 3. Third-party SaaS Applications

Instead of watching for changes, these will work with a continuos integration workflow, where your latest push on a certain branch gets uploaded to the theme you've selected.

1. [**Beanstalk**](http://beanstalkapp.com). More specific information can be found on their landing page for Shopify, [here](http://beanstalkapp.com/shopify).
2. [**DeployBot**](https://deploybot.com/). Their [help article](http://support.deploybot.com/article/908-shopify) on Shopify has some information on how to get started.
   Both options are from the same company. [Here's](http://blog.beanstalkapp.com/post/124938580844/beanstalk-or-deploybot-how-to-choose-the-right) a comparison of both they've did on their blog.

# 4. Third-party libraries

1. There's also [an alternative not officially supported by Shopify](https://help.shopify.com/themes/development/getting-started/using-shopify-textmate-bundle) which is a **TextMate Bundle** in case you use that OSX editor.
2. There's an unofficial extended cli similar to theme kit but with further functionality called [**Quickshot**](https://quickshot.readme.io/), which I've just found out based on Matt's response and seems pretty awesome. Some of the features they highlight are:

   * Supports uploading to multiple Shopify stores and themes
   * Easy to use configuration wizard
   * Uploads/downloads in parallel greatly reducing transfer times
   * Supports autocompiling scss locally before uploading to Shopify
   * Supports autocompiling Babel/ES6 into modules which are easily used by - Requirejs and others
   * Can use with .gitignore files or a custom .quickshotignore file.
   * Can download/upload Shopify Blogs, Pages and Products! Easily transfer them between stores! Even the metafields! And edit them locally in your favorite editor.

### Answer (Score: 5, Accepted: False)
Shopify recently released Slate, a new tool for theme development.

<https://github.com/Shopify/slate>

---

## Q: Setting Content-Type in Django HttpResponse object for Shopify App
**Score:** 23 | https://stackoverflow.com/questions/17548414/setting-content-type-in-django-httpresponse-object-for-shopify-app

### Answer (Score: 21, Accepted: False)
Try the following:

```
def featured(request):
    content = '<html>test123</html>'

    response = HttpResponse(content, content_type='application/liquid')
    response['Content-Length'] = len(content)

    return response
```

A quick tip, you could add this into the `http` or `server` block part of your NGINX configuration so you don't have to specify the encoding within views and other Django code:

```
charset utf-8;
charset_types text/css application/json text/plain application/liquid;
```

### Answer (Score: 6, Accepted: False)
So this worked for me:

```
def featured(request):
  response = HttpResponse(content_type="application/liquid; charset=utf-8")
  response['Content-Length'] = len(content.encode('utf-8'))
  response.write('<html>test123</html>')
  return response
```

Thanks, everyone, for the help!

---

## Q: How can I split a string by newline in Shopify?
**Score:** 22 | https://stackoverflow.com/questions/27694610/how-can-i-split-a-string-by-newline-in-shopify

### Answer (Score: 51, Accepted: True)
Try this:

```
{% assign paragraphs = settings.intro | newline_to_br | split: '<br />' %}
{% for paragraph in paragraphs %}<p>{{ paragraph }}</p>{% endfor %}
```

### Answer (Score: 6, Accepted: False)
If you do, in fact, need Shopify to split by newlines for any reason where you don't iterate with a for loop afterwards, it is indeed possible:

```
{% assign paragraphs = settings.intro | split: '
' %}
{% for paragraph in paragraphs %}
    <p>
        {{ paragraph }}
    </p>
{% endfor %}
```

ie. you need to type an explicit newline into your source code.

This is due to the way Liquid works, quoting from the documentation about [Types](https://shopify.github.io/liquid/basics/types/):

> Liquid does not convert escape sequences into special characters.

---

## Q: Shopify - New order using the Shopify API - how to know tax and shipping?
**Score:** 21 | https://stackoverflow.com/questions/43311968/shopify-new-order-using-the-shopify-api-how-to-know-tax-and-shipping

### Answer (Score: 5, Accepted: True)
This answer is a little bit late, but i hope, i can help others that are struggling with the same issue.

First i would recommend to set up all Shipping Rates and Taxes in Shopify. There are plenty of manuals to achieve this:

<https://help.shopify.com/manual/taxes#general-process-to-set-up-taxes>
<https://help.shopify.com/manual/shipping/rates-and-methods/calculated-rates>

After this there are different possibilities to calculate your shipping and tax cost.

Your shipping cost can you get via the active\_shipping API, which can be found here:
<https://github.com/Shopify/active_shipping>

Or the following Shopify Application: <https://apps.shopify.com/boxify>

However, you may need to know size and storage location for theese solutions.

The taxes can you get via the country in the Admin API, there is a specific key-value pair for this:
<https://help.shopify.com/api/reference/country>

I hope that's enough information to get closer to solving the issue, for at least someone.

---

## Q: python requests - encoding with &#39;idna&#39; codec failed (UnicodeError: label empty or too long) error
**Score:** 20 | https://stackoverflow.com/questions/51901399/python-requests-encoding-with-idna-codec-failed-unicodeerror-label-empty-o

### Answer (Score: 23, Accepted: False)
It seems this is an issue from the `socket` module. It fails when the URL exceeds 64 characters. This is still an open issue <https://bugs.python.org/issue32958>

> The error can be consistently reproduced when the first substring of the url hostname is greater than 64 characters long, as in "0123456789012345678901234567890123456789012345678901234567890123.example.com". This wouldn't be a problem, except that it doesn't seem to separate out credentials from the first substring of the hostname so the entire "[user]:[secret]@XXX" section must be less than 65 characters long. This is problematic for services that use longer API keys and expect their submission over basic auth.

**There is an alternative solution**:

It seems you're trying to use the Shopify API so I'll take it as an example.

Encode `{api_key}:{password}` in `base64` and send this value in the headers of your request eg. `{'Authorization': 'Basic {token_base_64}'}`

See the example below:

```
import base64
import requests

auth = "[API KEY]:[PASSWORD]"
b64_auth = base64.b64encode(auth.encode()).decode("utf-8")

headers = {
    "Authorization": f"Basic {b64_auth}"
}

response = requests.get(
    url="https://[YOUR-SHOP].myshopify.com/admin/[ENDPOINT]",
    headers=headers
)
```

---

## Q: Get shopify Metafields for products in one call
**Score:** 20 | https://stackoverflow.com/questions/11019763/get-shopify-metafields-for-products-in-one-call

### Answer (Score: 2, Accepted: False)
It would be nice if it was mentioned in the API doc though. Nothing about

> Receive a list of all Metafields GET /admin/metafields.json?since\_id=721389482

indicates it will only return shop metafields.

### Answer (Score: 1, Accepted: False)
We have had a lot of requests for getting metafields for multiple resources in the same request. However, a lot of them could be handled by keeping the information at the applications side (e.g. in a database), along with the id of the resource. This way the data is closer to where it is being used.

There are two very good reasons for using metafields

* Storing metadata to use from liquid templates
* Shared storage between applications

Metafields for liquid templates is great because the data is close to where it will be used for page rendering. This makes rendering fast and more customizable, because custom fields can be provided by apps and rendered in the storefront.

Shared storage between applications is another good reason to use metafields, but it doesn't appear to be a common reason metafields are used. In this case the metafields API is currently lacking a way to access metafields on multiple resources at once.

Returning metadata along with products, however, is not a very good option. This is because other applications may store data in metafields that your application might not care about, so one application could end up slowing down a lot of other applications that don't even use metafields. This is why the metafields API has query parameters to restrict what metafields being retrieved, so metafields for other applications aren't returned unnecessarily.

---

## Q: Shopify App development tutorials
**Score:** 20 | https://stackoverflow.com/questions/29456778/shopify-app-development-tutorials

### Answer (Score: 2, Accepted: False)
The first thing I would recommend is looking at the Shopify API libraries available. For example the [Shopify API Gem](https://github.com/Shopify/shopify_api) in Ruby.

to get your app connected you need to do the following:

1) Get a developer's account on Shopify (partner account) and create an app.

2) Grab your API and secret key

3) follow the instruction on the API libraries like in the link provided (steps 1-7) and you should be able to get your app started.

(Essentially, grab the permanent token from Shopify and you will be able to make API calls and get all the data from the store you want).

### Answer (Score: 0, Accepted: False)
Check the [shopify application proxy](https://docs.shopify.com/api/uiintegrations/application-proxies).

According to the doc, "an application proxy allows your application to add functionality to the frontend of a shop".

---

## Q: Tampermonkey ignores @exclude
**Score:** 19 | https://stackoverflow.com/questions/25864833/tampermonkey-ignores-exclude

### Answer (Score: 22, Accepted: True)
`@exclude` is very precise. You need to put a trailing asterisk on each of the exclude lines. EG:

```
// @exclude    https://*.myshopify.com/admin/products*
// @exclude    https://*.myshopify.com/admin/collections*
// @exclude    https://*.myshopify.com/admin/blogs*
// @exclude    https://*.myshopify.com/admin/pages*
// @exclude    https://*.myshopify.com/admin/themes*
```

---

Consider (and install) this Tampermonkey script:

```
// ==UserScript==
// @name     _match and exclude testing
// @match    http://*.stackexchange.com/*
//
// @exclude  http://*.stackexchange.com/questions*
// @exclude  http://*.stackexchange.com/tags
// @require  http://ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js
// @grant    GM_addStyle
// ==/UserScript==

$("body").prepend ('<h1 style="background: yellow;">Match Script fired on this page.</h1>');
```

If you then visit [arduino.stackexchange.com/tags](https://arduino.stackexchange.com/tags), the script won't fire, but when visiting:

* [arduino.stackexchange.com/tags/](https://arduino.stackexchange.com/tags/)  
  or
* [arduino.stackexchange.com/tags?foo=bar](https://arduino.stackexchange.com/tags?foo=bar)

it will!

Changing the second exclude line to:

```
// @exclude  http://*.stackexchange.com/tags*
```

fixes the problem.

---

If you still have difficulty, specify your versions of Chrome, Tampermonkey, and operating system. And, provide target page(s) that demonstrate the problem.

### Answer (Score: 1, Accepted: False)
what always trips me up with @exclude in Tampermonkey:

`@match *://*.somewebsite.com` works well enough even when the website's `window.location.href` reports without a subdomain, like `https://somewebsite.com`.

but `@exclude *://*.somewebsite.com/*` does NOT recognize it. I would have to modify the @exclude to remove the subdomain as well, like `@exclude *://somewebsite.com/*`. only then does Tampermonkey realize that the script shouldn't actually run.

---

## Q: Overriding difficult view model
**Score:** 18 | https://stackoverflow.com/questions/32252575/overriding-difficult-view-model

### Answer (Score: 3, Accepted: False)
Well, there is a kind of a dirty solution...

First of all you'll need a [sendkeys](http://bililite.com/blog/2011/01/23/improved-sendkeys/) plugin. In fact that means you'll need to include [this](https://github.com/dwachss/bililiteRange/blob/master/bililiteRange.js) and [this](https://github.com/dwachss/bililiteRange/blob/master/jquery.sendkeys.js) JS libraries (you can just copy-paste them in the console to test). If you don't want to use the first library (I personally find it quite big for such a small thing) you can extract only the key things out of it and use only them.

The next step is creating the function which is going to act like a real user:

```
function input(field, desiredValue) {
  // get the currency symbol while value is still pristine
  var currency = field.val()[0];

  // move focus to the input
  field.click().focus();

  // remove all symbols from the input. I took 10, but of course you can use value.length instead
  for (var i = 0; i < 10; i++) field.sendkeys("{backspace}");

  // send the currency key
  field.sendkeys(currency);

  // send the desired value symbol-by-symbol
  for (var i = 0; i < desiredValue.length; i++) field.sendkeys(desiredValue[i]);
}
```

Then you can simply call it with the value you wish to assign:

```
input($("#product_variants__price").next(), "123.00");
```

I did not really manage to fake the blur event because of lack of the time; that is why I was forced to read the currency and pass `.00` as a string. Anyway you already have a way to go and a quite working solution.

### Answer (Score: 3, Accepted: True)
Try this:

```
var old = Shopify.EditVariantPrice.prototype.onFocus;
Shopify.EditVariantPrice.prototype.onFocus = function(t) { 
  this.price = '50.00'; // Use the price you want here
  old.call(this, t); 
};
jQuery('#product_variants__price').siblings().triggerHandler("focus");
jQuery('#product_variants__price').siblings().triggerHandler("blur");
```

If it works for you, it's possible that the following will be sufficient:

```
Shopify.EditVariantPrice.prototype.onFocus = function(t) { 
  this.price = '50.00'; // Use the price you want here
};
```

---

## Q: Format liquid(Shopify) code in visual studio code
**Score:** 18 | https://stackoverflow.com/questions/50384369/format-liquidshopify-code-in-visual-studio-code

### Answer (Score: 7, Accepted: True)
The [VSCode Liquid](https://github.com/panoply/vscode-liquid) extension provides formatting and syntax highlighting. Also has intellisense and ton of other features.

### Answer (Score: -3, Accepted: False)
```
<div class="page-width">
  {% if section.settings.title != blank %}
    <header class="section-header">
      <h2 class="section-header__title">
        {{section.settings.title}}
      </h2>
    </header>
  {% endif %}

  <div class="popup-gallery">
    {%- for media in product.media -%}
    {%- liquid
      assign has_video = false
      assign video_type = ''

      case media.media_type
        when 'external_video'
          assign has_video = true
          assign video_type = media.host

          if media.host contains 'youtube'
            assign video_id = media.external_id
          endif
        when 'video'
          assign has_video = true
          assign video_type = 'mp4'
      endcase -%}

      <div
        href="{%- if has_video -%}
          {%- if media.media_type=='video' -%}
            {%- for source in media.sources -%}
              {{- source.url -}}
            {%-endfor-%}
          {%- else -%}
            {%- assign video_url = media | external_video_url -%}                
            {%- if video_url contains "youtube" -%}
              https://www.youtube.com/watch?v={{- media.external_id -}}              
            {%- else -%}
              https://vimeo.com/{{- media.external_id -}}
            {%- endif -%}
          {%- endif -%}
        {%- else -%}
          {{- media | image_url -}}
        {%- endif -%}"
      class="
        {% if has_video %}
          video
        {% else %}
          image
        {% endif %}"
      title="
        {% if has_video %}
          This is a video
        {% else %}
          This is a image
        {% endif %}
      ">
        {%- assign img_url = media.preview_image | img_url: '1x1' | replace: '_1x1.', '_{width}x.' -%}
        <img
          class="lazyload"
          data-src="{{ img_url }}"
          data-widths="[120, 360, 540, 720]"
          data-aspectratio="{{ media.preview_image.aspect_ratio }}"
          data-sizes="auto"
          alt="GALLERY"
        >
          <noscript>
            <img
              class="lazyloaded"
              src="{{ media | img_url: '400x' }}"
              alt="GALLERY"
            >
          </noscript>
        </div>
      {%- endfor -%}
    </div>
  </div>
    
  {{ 'magnific-popup.min.css' | asset_url | stylesheet_tag }}
    
  <script
    type="text/javascript"
    src="{{ 'jquery.min.js' | asset_url }}"
  ></script>
  <script
    type="text/javascript"
    src="{{ 'magnific-popup.min.js' | asset_url }}"
  ></script>

  <script type="text/javascript">
    $(".popup-gallery").magnificPopup({
      delegate: "div",
      type: "image",
      gallery: {
        enabled: true,
        navigateByImgClick: true,
        preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
      },
      callbacks: {
        elementParse: function (item) {
          console.log(item.el[0].className);
          if (item.el[0].className == "video") {
            (item.type = "iframe"),
            (item.iframe = {
              patterns: {
                youtube: {
                  index: "youtube.com/", // String that detects type of video (in this case YouTube). Simply via url.indexOf(index).
                  id: "v=", // String that splits URL in a two parts, second part should be %id%                 // Or null - full URL will be returned                 // Or a function that should return %id%, for example:
                  // id: function(url) { return 'parsed id'; }
                  src: "//www.youtube.com/embed/%id%?autoplay=1" // URL that will be set as a source for iframe.
                  },
                  vimeo: {
                    index: "vimeo.com/",
                    id: "/",
                    src: "//player.vimeo.com/video/%id%?autoplay=1"
                  },
                  gmaps: {
                    index: "//maps.google.",
                    src: "%id%&output=embed"
                  }
                }
              });
            } else {
              (item.type = "image"),
              (item.tLoading = "Loading image #%curr%..."),
              (item.mainClass = "mfp-img-mobile"),
              (item.image = {
                tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
              });
            }
          }
        }
      });
  </script>
  {% schema %}
    {
      "name": "Product gallery",
      "class": "product-gallery-section",
      "settings": [
        {
          "type": "text",
          "id": "title",
          "label": "Heading"
        }
      ]
    }
  {% endschema %}
```

---

## Q: Web API 2 return OK response but continue processing in the background
**Score:** 16 | https://stackoverflow.com/questions/27060447/web-api-2-return-ok-response-but-continue-processing-in-the-background

### Answer (Score: 16, Accepted: True)
I have managed to solve my problem by running the processing asynchronously by using `Task`:

```
    // PUT: api/Afilliate/SaveOrder
    public IHttpActionResult WebHook(ShopifyOrder order)
    {
        // this should process the order asynchronously
        var tasks = new[]
        {
            Task.Run(() => ProcessOrder(order))
        };

        // without the await here, this should be hit before the order processing is complete
        return Ok("ok");
    }
```

### Answer (Score: 6, Accepted: False)
There are a few options to accomplish this:

1. Let a task runner like `Hangfire` or `Quartz` run the actual processing, where your web request just kicks off the task.
2. Use queues, like `RabbitMQ`, to run the actual process, and the web request just adds a message to the queue... be careful this one is probably the best but can require some significant know-how to setup.
3. Though maybe not exactly applicable to your specific situation as you are having another process wait for the request to return... but if you did not, you could use `Javascript AJAX` kick off the process in the background and maybe you can turn retry off on that request... still that keeps the request going in the background so maybe not exactly your cup of tea.

---

## Q: Shopify order webhooks
**Score:** 16 | https://stackoverflow.com/questions/12738309/shopify-order-webhooks

### Answer (Score: 14, Accepted: True)
I'd say for sake of keeping the code easier to understand it would be in your best interest to handle the appropriate webhooks just to keep the code easier to understand.

If all you're doing is tracking really general stuff, it's probably fine.

Also, on all state changes of an order the `orders/updated` webhook is fired.

---

## Q: Shopify: get current logged in user ID in JavaScript
**Score:** 15 | https://stackoverflow.com/questions/25501391/shopify-get-current-logged-in-user-id-in-javascript

### Answer (Score: 20, Accepted: False)
You can try `__st.cid` in JavaScript for getting customer id.

### Answer (Score: 19, Accepted: False)
I've found the `__st` variables unreliable (`__st_uniqToken` for one).
I believe the proper way to do this in Javascript is using the following call:

`ShopifyAnalytics.lib.user().id()`

You can also get the unique user id (non-logged in id) with:

`ShopifyAnalytics.lib.user().properties().uniqToken`

This is also the only reliable way to get it on the checkout page. I previously used `__st_uniqToken`, but it has since stopped working.

**NOTE** This is no longer 100% fool-proof. Shopify have **AGAIN** changed how their site works on the landing and thank-you pages.
I've had to resort to the following function to get a user id 'reliably'.

```
var user_id = function() {
    try {
        return ShopifyAnalytics.lib.user().id();
    } catch(e) {}
    try {
        return ShopifyAnalytics.lib.user().properties().uniqToken;
    } catch(e) {}
    try {
        return ShopifyAnalytics.lib.user().anonymousId();
    } catch(e) {}
    return __st_uniqToken;
};
```

Developing for Shopify is a true nightmare. I spend 50% of my time un-breaking my product every few weeks because them.

---

## Q: Custom made sections not appearing with Shopify&#39;s new theme editor
**Score:** 15 | https://stackoverflow.com/questions/39865010/custom-made-sections-not-appearing-with-shopifys-new-theme-editor

### Answer (Score: 57, Accepted: True)
You're almost there, just missing one thing. Sections will only show up as options to be added if they have a preset defined.

This update will make it show up:

```
{% schema %}
{
  "name": "Call to Actions",
  "class": "index-section index-section--flush",
  "settings": [
    {
      "id": "cta_1_title",
      "type": "text",
      "label": "CTA 1 Title",
      "default": "Dryups Specials"
    }
  ],
  "presets": [{
    "name": "Call to Actions",
    "category": "Text"
  }]
}
{% endschema %}
```

Note the category. If omitted, it'll end up under Miscellaneous.

---

## Q: How to catch the HTTP POST request sent by a Shopify Webhook
**Score:** 15 | https://stackoverflow.com/questions/10937198/how-to-catch-the-http-post-request-sent-by-a-shopify-webhook

### Answer (Score: 32, Accepted: True)
Create a public URL at <http://example.com/whatever.php>, where example.com is your domain name and whatever.php is a PHP file that you can edit.

Then put this code into whatever.php:

```
<?php
$webhookContent = "";

$webhook = fopen('php://input' , 'rb');
while (!feof($webhook)) {
    $webhookContent .= fread($webhook, 4096);
}
fclose($webhook);

error_log($webhookContent);
?>
```

Then in the Shopify admin you can create a new webhook and point it at <http://example.com/whatever.php>, and when you click the 'test webhook' button in the Shopify admin, Shopify will POST to your script above, which should in turn write the body of the webhook to your PHP error log.

### Answer (Score: 4, Accepted: False)
Sorry, I don't have enough reputation to post comments, but here is the contents of the dead link from Edward Ocampo-Gooding's answer:

> **PHP Example w/ SimpleXML (PHP 5+)**
>
> The script below shows you how to get the XML data in from Shopify into your script, archive the file, and send the proper headers ...
>
> Given that the new order subscription setup in the admin for the webhook is: <http://example.com/some-script.php?key=123456789>
>
> Contents of some-script.php on <http://example.com/>:

```
<?     
// Protect URL from rogue attacks/exploits/spiders
// Grab from GET variable as given in Shopify admin URL
// for the webhook
//
// NOTE: This is not necessary, just a simple verification
//
// A digital signature is also passed along from Shopify,
// as is the shop's domain name, so you can use one or both of those
// to ensure a random person isn't jacking with your script (or some
// spider just randomly hitting it to see what's there).
//
// If $key doesn't matched what should be passed in from the
// webhook url, the script simply exits
$key = $_GET['key']; 

if ($key != '123456789') {
  header('HTTP/1.0 403 Forbidden');
  exit();
}

// Variables used for processing/saving
$xmlString = ;  // Used to get data from Shopify into script
$name = ;  // Saves the billing address name to be used for later ...
$email = ;  // Save the email address of the user to be used for later ...
$productTitles = array();  // Saves all titles of products purchased to be used for later ... 

// Get XML data and read it into a string for use with SimpleXML
// Thanks to David Oxley (http://www.numeriq.co.uk) for help with this
$xmlData = fopen('php://input' , 'rb'); 
while (!feof($xmlData)) { $xmlString .= fread($xmlData, 4096); }
fclose($xmlData);

// Save order XML in file in orders directory
// This creates a file, write the xml for archival purposes, and closes the file ...
// If the file already exists, it appends the data ... this should create a separate
// file for every order but if two orders are processed the same second, they'll both
// be in the same file
file_put_contents('orders/order' . date('m-d-y') . '-' . time() . '.xml', $xmlString, FILE_APPEND);

// Use SimpleXML to get name, email, and product titles
// SimpleXML allows you to use the $xml object to easily
// retrieve the data ...
// Please note, if hyphens are used in the xml node, you must
// surround the call to that member with {'member-name'} as is
// shown below when getting the billing-address name & the
// line items
$xml = new SimpleXMLElement($xmlString);

$name = trim($xml->{'billing-address'}->name);
$email = trim($xml->email);

// Create productTitles array with titles from products
foreach ($xml->{'line-items'}->{'line-item'} as $lineItem) {
  array_push($productTitles, trim($lineItem->title));
}

// You would then go on using $name, $email, $productTitles in your script
// to do whatever the heck you please ...

// Once you are done doing what you need to do, let Shopify know you have 
// the data and all is well!
header('HTTP/1.0 200 OK');
exit();

// If you want to tell Shopify to try sending the data again, i.e. something
// failed with your processing and you want to try again later
header('HTTP/1.0 400 Bad request');
exit();
?>
```

---

## Q: An error occurred while installing pg (0.21.0), and Bundler cannot continue
**Score:** 15 | https://stackoverflow.com/questions/46913424/an-error-occurred-while-installing-pg-0-21-0-and-bundler-cannot-continue

### Answer (Score: 15, Accepted: False)
Actually this worked for me

```
sudo apt-get install libpq-dev ruby-dev
```

It required me to install two packages `libpq-dev` and `ruby-dev`

### Answer (Score: 10, Accepted: False)
I think you don't have postgresql installed. Try:

```
brew install postgresql
```

---

## Q: Date comparison Logic / in Liquid Template Filter
**Score:** 15 | https://stackoverflow.com/questions/47577336/date-comparison-logic-in-liquid-template-filter

### Answer (Score: 32, Accepted: True)
You can't compare strings this way. (The dates are strings.)

You have to use the `%s` date filter instead.

So it will become:

```
{% assign today_date = 'now' | date: '%s' %}
{% assign pre_date = product.metafields.Release-Date.preOrder | date: '%s' %}
{% if today_date > pre_date %}
```

We use `%s` because it will return the current unix timestamp number instead of a string. This way you will be able to compare the different timestamps.

---

## Q: Using vue.js in Shopify liquid templates
**Score:** 15 | https://stackoverflow.com/questions/43505094/using-vue-js-in-shopify-liquid-templates

### Answer (Score: 19, Accepted: True)
Apparently with Shopify, you can't put these delimiters in the tag attributes at all so for those use v-bind: (the shorthand won't work). Also you have to use a single curly brace for your custom delimiter or it will still try to parse with liquid, for example:

```
delimiters: ['${', '}']
```

will work with:

```
<span class="title">${ product.title }</span>
```

### Answer (Score: 3, Accepted: False)
Adding on a bit from where Kevin Compton left off, this is where you put the "delimiters" parameter:

```
const ConditionalRendering = {
  data() {
    return {
      seen: true,
      someMessage: "My message"
    }
  },

  delimiters: ['${', '}']
  
}


Vue.createApp(ConditionalRendering).mount('#conditional-rendering')
```

---

## Q: Delete the store details from PHP Application after uninstalling app from Shopify Store
**Score:** 15 | https://stackoverflow.com/questions/43488731/delete-the-store-details-from-php-application-after-uninstalling-app-from-shopif

### Answer (Score: 5, Accepted: True)
Your example code is registering a callback that will be accessed by the shopify uninstall webhook which will run when your app is uninstalled via the shopify admin UI. Make sure that "address" property is a public url to your applications uninstall callback.

Yes, you can register a callback for webhook at anytime.

When the app is uninstalled, shopify will send a POST request to the address you specified in the 'address' property with a [json payload](https://help.shopify.com/api/reference/webhook) that has the customers details.

Take care to collect the [X-Shopify-Hmac-SHA256](https://help.shopify.com/api/getting-started/webhooks#verify-webhook) header and verify this is a genuine request before your callback deletes customer data.

[Make sure you have all the data you need before the uninstall hook is run.](https://help.shopify.com/api/getting-started/authentication/oauth/uninstalling-applications)
Uninstall revokes account tokens, removes registered webhooks and app data from shopify.

### Answer (Score: 4, Accepted: False)
Without knowing the schema it's hard to tell what data you are trying to remove. If you're able to provide an example of what data you're inserting and what sort of columns are available we may be able to provide a bit more assistance.

Having said all that, it's fairly straight forward to delete a row from a database. I assume you are looking for a script to delete something from a database, the below will do that. You need to update the SQL query to reflect your schema.

```
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

// sql to delete a record
$sql = "DELETE FROM MyGuests WHERE id=3";

if ($conn->query($sql) === TRUE) {
    echo "Record deleted successfully";
} else {
    echo "Error deleting record: " . $conn->error;
}

$conn->close();
?>
```

---

## Q: How can I get the URL for product&#39;s page using the Shopify API?
**Score:** 14 | https://stackoverflow.com/questions/11896661/how-can-i-get-the-url-for-products-page-using-the-shopify-api

### Answer (Score: 25, Accepted: True)
You can do it as 'products/< product.handle >'. I'm not sure if there is a better way of doing it, but it works.

### Answer (Score: 4, Accepted: False)
I usually add this in `config/initializers/shopify_api.rb`:

```
module ShopifyAPI
  class Shop
    def store_url_for(entity)
      return "http://#{self.domain}/#{entity.class.element_name}/#{entity.handle}"
    end
  end
end
```

---

## Q: Shopify: How can I handle an uninstall followed by an instant re-install?
**Score:** 14 | https://stackoverflow.com/questions/14418415/shopify-how-can-i-handle-an-uninstall-followed-by-an-instant-re-install

### Answer (Score: 21, Accepted: True)
I've had this problem with my apps as well lately. Webhooks only started getting delayed in the last 2 months, and I'd be surprised if most apps out there weren't suffering from this regression bug now.

The way I deal with it is - when the user is redirected to the app and the old db object/token is still present in the database, try calling a dummy API call to the Shopify API (something like get shop details) with the token you have. If you get a 403 Unauthorized response, invalidate the user session and refresh the stored token.

Another problem is that after a minute or two when the original uninstall webhook does fire, do the same procedure - check for a 403 response. If you **DON'T** get a 403, then you know that the webhook is old and shouldn't be acted upon, because if you get a 200 OK it means that your token is good and that the app is still installed.

It's a bit convoluted and it added a fair bit of code to my apps, but it's the only thing I could think of on a short notice - because merchants do uninstall/re-install quickly fairly often.

---

## Q: How to define global variables in Liquid?
**Score:** 14 | https://stackoverflow.com/questions/35094919/how-to-define-global-variables-in-liquid

### Answer (Score: 6, Accepted: False)
It seems the templates are loaded before the theme, so variables set in your layout/theme file wont be present in templates. Frustrating. However you can set them via a snippet, and include this snippet in your templates, layout, etc

### Answer (Score: 5, Accepted: False)
For Liquid you can pass a variable in the include

```
{%- assign global_var = "VALUE" -%}
{%- include 'YOUR_FILE' global_var: global_var  -%}
```

For Shopify liquid you can do the following:

There is a work around this, you can set the global variable in the theme settings as an option `config/settings_schema.json`

```
  {
    "type": "text",
    "id": "global_variable",
    "label": "global variable",
    "default": "Variable value"
  },
```

and you can access it in the liquid files through

```
settings.global_variable
```

But the value is depending on what you enter in the theme settings.

If you need more dynamic way, you can set cart attributes through ajax like:

```
    $.ajax({
      type: 'POST',
      url: '/cart/update.js',
      data: { attributes: {'global_variable': "MY_VALUE"} },
      dataType: 'json',
      success: function(cart) {
        location.reload();
      }
    });
```

And then access it any where in the theme through
cart.attributes.global\_variable
But you have to update it each time the cart is empty

---

## Q: Meteor Shopify API: Post metafield to collection by collection ID
**Score:** 14 | https://stackoverflow.com/questions/30468836/meteor-shopify-api-post-metafield-to-collection-by-collection-id

### Answer (Score: 2, Accepted: False)
I believe you can specify your own calls if they aren't implemented, like so:

```
Shopify.API.define({
   "name": "getCollectionMetafields",
   "method": "GET",
   "path": "/admin/custom_collections/#{id}/metafields.json",
   "returns": "metafield",
   "description": "Get a collection's metafields"
});
```

---

## Q: Incrementing variables in liquid without outputting them
**Score:** 13 | https://stackoverflow.com/questions/36110738/incrementing-variables-in-liquid-without-outputting-them

### Answer (Score: 34, Accepted: False)
If you are using a different logic for incrementing the value than `forloop.index`, you can use the [`plus` filter](https://shopify.dev/docs/themes/liquid/reference/filters/math-filters#plus) to increment the variable:

```
{% assign variable = 0 %}
{% for … %}
  {% assign variable = variable | plus: 1 %}
{% endfor %}
```

I can also recommend that you have a look at the [cheat sheet for Shopify](http://cheat.markdunkley.com/).

### Answer (Score: 8, Accepted: True)
This is by design, at it allows you to increment and display a variable at the same time. See [the documentation](http://shopify.github.io/liquid/tags/variable/#increment).

`assign` only allows you to assign *new* variables (and not modify existing ones), so aside from creating a new tag, the easiest way is to use use `capture` to capture the output:

```
{% capture _ %}{% increment variable %}{% endcapture %}
```

That being said, perhaps it's time to re-consider why exactly you're doing this? Note that you already have `forloop.index` and `forloop.index0` available for the loop index (once again, [see the documentation](https://docs.shopify.com/themes/liquid/objects/for-loops)).

---

## Q: shopify I need to check if current page is a collection page and not a single product page
**Score:** 13 | https://stackoverflow.com/questions/39932190/shopify-i-need-to-check-if-current-page-is-a-collection-page-and-not-a-single-pr

### Answer (Score: 20, Accepted: False)
Use this simple way with [`template`](https://shopify.dev/docs/api/liquid/objects/template):

```
{% if template contains 'collection' %}
    Do something
{% endif %}
```

As Shopify evolves you can now use this:

```
{% if template.name == 'collection' %}
    Do something
{% endif %}
```

As Shopify evolves (bis) you can now use this:

```
{% if page.request_type == 'collection' %}
    Do something
{% endif %}
```

### Answer (Score: 13, Accepted: False)
A safer alternative to avoid rare cases where templates are badly named would be to use `request.page_type` - see [the Shopify docs](https://shopify.dev/docs/themes/liquid/reference/objects/request#request-page_type)

```
{% if request.page_type == 'collection' %}
  Do something
{% endif %}
```

---

## Q: How to check for the existence of an element in a Liquid array (Shopify) without using join
**Score:** 13 | https://stackoverflow.com/questions/50829664/how-to-check-for-the-existence-of-an-element-in-a-liquid-array-shopify-without

### Answer (Score: 24, Accepted: True)
Reading the [documentation](https://shopify.github.io/liquid/basics/operators/#contains) we can see that :

> `contains` can also check for the presence of a string in an array of strings.

So, no `join` is necessary, and this will do the job.

```
{%- if blogs.news.all_tags contains blog_title -%}
...
```

---

## Q: React Hook useCallback not updating State value
**Score:** 13 | https://stackoverflow.com/questions/60911179/react-hook-usecallback-not-updating-state-value

### Answer (Score: 18, Accepted: True)
You are mutating the `values` state, see [this](https://codesandbox.io/s/eloquent-dijkstra-vhn97) sandbox

Change your `handleChange` function to

```
const handleChange = useCallback((newValue, id) => {
  const newProds = { ...values };
  newProds[id] = newValue;
  setValues(newProds);
}, [values]);
```

You can change it further to

```
const handleChange = useCallback((newValue, id) => {
  setValues(prods => ({...prods, [id] : newValue }));
}, [values]);
```

### Answer (Score: 5, Accepted: False)
Try updating `handleChange` to this:

```
const handleChange = useCallback(
    (newValue, id) => {
      console.log("Pre: values:", values);
      console.log(id, newValue);
      setValues(state => ({ ...state, [id]: newValue}));
    },
    [values]
  );
```

---

## Q: GraphQL, Shopify Get All products or totalcount of products
**Score:** 13 | https://stackoverflow.com/questions/66185620/graphql-shopify-get-all-products-or-totalcount-of-products

### Answer (Score: 6, Accepted: True)
You can't get all products with a single GraphQL request either with the StoreFront GraphQL or the Admin GraphQL.

If your products are below 250 you can make a request with `first: 250` but if you have more than 250 products than you need to make recursive request with the cursor pagination for GraphQL. So if you have 1000 products you will need to make 4 request (depending on which API you are using, the storefront or admin graphql api, since they are different)

At the moment there is no way to get all products using a single request via any of the provided APIs from Shopify.

The only way to achieve this is to make a custom template with the following code:

```
[
{% paginate collection.products by 9999 %}
  {% for product in collection.products %}
    {{product | json}}{% unless forloop.last %},{% endunless %}
  {% endfor %}
{% endpagination %}
]
```

Call it something like `collection.ajax.liquid`.

And make a fetch request to it using the view param:

```
fetch('/collections/all?view=ajax').then((response) => handle the response)
```

Have in mind that the more products you have the longer the request to that page will be. If you have 1000 products the request can take up to 10 seconds. So this is not a great solution as well for massive pool of products.

---

As for the total count there is a liquid object for that `{{ collection.all_products_count }}` or if you are doing admin stuff, use the rest api, since there is a method to get the products count, but there is none in the graphql.

### Answer (Score: 2, Accepted: False)
You can get all products using [BULK API](https://shopify.dev/api/admin-graphql/2021-10/objects/BulkOperation) with conjunction to GRAPHQL

---

## Q: Oauth error invalid_request: The redirect_uri is not whitelisted
**Score:** 12 | https://stackoverflow.com/questions/55918320/oauth-error-invalid-request-the-redirect-uri-is-not-whitelisted

### Answer (Score: 36, Accepted: False)
I don't think my answer is going to help many , But i am going to put it here anyway. So i had the same issue recently and i tried everything in stack-overflow and shopify community. And finally the problem was ***i had mistakenly copied my another app's apikey***. So even if the apiKey is wrong the error probably you are going to face is the same "The redirect uri is not whitelisted."

### Answer (Score: 15, Accepted: True)
Yes there is an issue with your callback URL you have to define your app URL and callback URL in your shopify partner account where you create shopify app

[Shopify partner account](https://partners.shopify.com)

You have to do as follow

open apps >> yourapp >> app setup >> Insert In URLs(Whitelisted redirection URL(s))

Once you whitelist your URL there then the issue is solve

---

## Q: Shopify : Errors: [API] This action requires merchant approval for write_themes scope
**Score:** 12 | https://stackoverflow.com/questions/50364356/shopify-errors-api-this-action-requires-merchant-approval-for-write-themes

### Answer (Score: 32, Accepted: True)
Private apps have limited permissions like public apps do. You can fix your app's permissions by opening [the private apps section](https://myshopify.com/admin/apps/private) of the admin and tapping on the name of your app.

Scroll down to the section labelled `ADMIN API PERMISSIONS` and tap on `▼ Review disabled Admin API permissions`. Set `Theme templates and theme assets` to `Read and write` and then save and it should work.

### Answer (Score: 10, Accepted: False)
## The year 2023 answer

Go to your shop admin website
[https://admin.shopify.com/store/{your-website-name}](https://admin.shopify.com/store/%7Byour-website-name%7D)

Go to `Settings` (bottom left corner) -> `Apps and sales channels` -> `Develop apps` -> [select your app] -> `Configuration` tab -> Edit `Admin API integration` -> search for the desired scope.

FYI: Private apps were discontinued, and are now called Custom apps.

---

## Q: Graphql error: &quot;using last without before is not supported&quot;
**Score:** 12 | https://stackoverflow.com/questions/62765178/graphql-error-using-last-without-before-is-not-supported

### Answer (Score: 20, Accepted: True)
After a few moments of playing with the playground ... you can use a **workaround** - `reverse` and `first`

```
{
  orders(first: 10, reverse:true) {
    edges {
      node {
        id
        createdAt
      }
    }
  }
}
```

---

## Q: Using Liquid variables in JavaScript
**Score:** 12 | https://stackoverflow.com/questions/51769347/using-liquid-variables-in-javascript

### Answer (Score: 12, Accepted: False)
You can do something like that:

```
<script>
var myVar = {{yourLiquidVar | json}}
</script>
```

That instruction will convert your liquid var into json format

### Answer (Score: 5, Accepted: False)
you can use `liquid` variable for `js` in single quotes.

Here is an example:

```
{% assign test = 0 %}

// calling liquid variable in js

var testval= '{​{ test }}';
```

If a `liquid` var is an object, then you can use:

```
var productJSON = {{ product | json }};
```

---

## Q: Shopify password update using Shopify API
**Score:** 12 | https://stackoverflow.com/questions/35794258/shopify-password-update-using-shopify-api

### Answer (Score: 10, Accepted: False)
Although the API documentation does not say anything about changing the customer password, you can do actually change the customer password using the PUT /admin/customers/#{id}.json endpoint. Note that my answer is only for customers and not for users.

I have tested it, successfully changed the customer password and log in on the store with the new password. During my tests I used a private app and a normal app both with successful results.

Example:

PUT /admin/customers/5206361102.json

Body:

```
{
  "customer": {
    "id": 5206361102,
    "password": "mypass2",
    "password_confirmation": "mypass2"
  }
}
```

If you need the customer id you can use the the GET /admin/customers/search.json end point to find it.

For example you can get the id from the results of this:

GET /admin/customers/search.json?query=email:customeremail@customerdomain.com

Result:

```
{
  "customer": {
    "id": 5206556238,
    ... other parameters ...
  }
}
```

Thank you to [@spviradiya](https://stackoverflow.com/users/3300870/spviradiya) for the comment that pointed me out to this answer, I have tested it and implemented it into my project.

### Answer (Score: 3, Accepted: True)
The User endpoint is available for Shopify Plus stores, but it is currently read only - no user management is possible via this API

<https://docs.shopify.com/api/reference/user>

---

## Q: Shopify Toggle Cart Button location
**Score:** 12 | https://stackoverflow.com/questions/44480754/shopify-toggle-cart-button-location

### Answer (Score: 5, Accepted: True)
You can use [`events`](https://github.com/Shopify/buy-button-js/blob/master/docs/customization/index.md#events) option inside `toggle` config to define events you need. Use `afterInit` event to move toggle node in another place after initialization:

```
toggle: {
    events: {
        afterInit: function (component) {
            document.getElementById('cart-toggle').appendChild(component.node);
        },
    }
}
```

I assume that you can`t create two `toggle` components within a single Shopify embed. But you may operate on existing one using media queries in JS (i.e. [enquire.js](http://wicky.nillia.ms/enquire.js/)), so when your media query matches/unmatches, you move toggle button wherever you like in the DOM (i.e. inside mobile navigation area)

### Answer (Score: 1, Accepted: False)
Read this on GitHub: [insert toggle in the dom #569](https://github.com/Shopify/buy-button-js/issues/569#issuecomment-447076405)

I needed to do this very same thing. Verified, it worked for me.
You can place a DIV anywhere and use your own CSS to style it.
Yes, remember to set iframe and sticky to false.

---

## Q: Active_Shipping Negotiated Rates for UPS - Ruby on Rails
**Score:** 12 | https://stackoverflow.com/questions/46552755/active-shipping-negotiated-rates-for-ups-ruby-on-rails

### Answer (Score: 5, Accepted: True)
Try assign your UPS account number as `origin_account` in the options.

```
response = carrier.find_rates(origin, destination, packages, {negotiated_rates: true, origin_account: 11111111})
```

<https://github.com/Shopify/active_shipping/blob/master/lib/active_shipping/carriers/ups.rb#L358>

---

## Q: Shopify API: Create a Promotion?
**Score:** 11 | https://stackoverflow.com/questions/13242989/shopify-api-create-a-promotion

### Answer (Score: 14, Accepted: True)
Unfortunately they don't allow it... I resorted to creating an interface to do so, though:

<https://github.com/MartinAmps/Shopify-Private-APIs>

Hope it helps

**Edit**

I also created a [blog post](http://ma.rtin.so/reverse-engineering-shopify-private-apis) about it.

### Answer (Score: 3, Accepted: False)
There is no way to create discounts via the API.

If you want we have made an [application that can be used to create discount codes](http://apps.shopify.com/bulk-discounts).

Otherwise you can use a tool like Mechanize to automate coupon creation for you, but keep in mind theres a good chance that any time in the future it will break since we don't make any promises to keep our admin the same in the future. Any changes have a good chance of breaking whatever script you'd end up writing.

---

## Q: what&#39;s the difference between .js and .js.liquid in shopify?
**Score:** 11 | https://stackoverflow.com/questions/25983518/whats-the-difference-between-js-and-js-liquid-in-shopify

### Answer (Score: 7, Accepted: False)
You can use liquid in `.js.liquid` files, but `.js` files are javascript only.

If you're including a regular js file, use the `.js` extension. If you've got liquid in the file as well, you'll need to use `.js.liquid`.

**EDIT:**

I don't think `order` can be accessed in a `.js.liquid` file. [See here](http://docs.shopify.com/themes/liquid-documentation/objects/order):

> The order object can be accessed in order email templates, the Thank You page of the checkout, as well as in apps such as Order Printer.

Also see [this discussion on the Shopify forums](https://ecommerce.shopify.com/c/ecommerce-design/t/using-liquid-in-javascript-trying-to-get-collection-title-in-jquery-callback-53043#comment-53047):

> You can only use Liquid filters and the global settings object in liquidified assets.
>
> It works like this: whenever you edit a .css.liquid of a .js.liquid file, or whenever you edit your theme settings, a new .css or .js file is created and then stored on our assets servers. Updating your shop in any other way will not update those files...
>
> Given the above, Shopify cannot expose store information (that is likely to change) in those files.

---

## Q: Adding Social Login to Shopify
**Score:** 11 | https://stackoverflow.com/questions/32564480/adding-social-login-to-shopify

### Answer (Score: 4, Accepted: False)
If you are rolling your own you probably want to look at Multipass. It would be the thing to use if you can set up another web service that handles the trusted partner registration process.

---

