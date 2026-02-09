---
source: Stack Overflow - Top Shopify Questions
---

# Top Shopify Questions from Stack Overflow

## 1. What&#39;s the cause of the error &#39;getaddrinfo EAI_AGAIN&#39;?
**Score:** 375 | **Tags:** javascript, node.js, error-handling, dns, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/40182121/whats-the-cause-of-the-error-getaddrinfo-eai-again

My server threw this today, which is a Node.js error I've never seen before:

```
Error: getaddrinfo EAI_AGAIN my-store.myshopify.com:443
    at Object.exports._errnoException (util.js:870:11)
    at errnoException (dns.js:32:15)
    at GetAddrInfoReqWrap.onlookup [as oncomplete] (dns.js:78:26)
```

I'm wondering if this is related to the DynDns DDOS attack which affected Shopify and many other services today. [Here's an article about that.](http://thenextweb.com/security/2016/10/21/massive-ddos-attack-dyn-dns-causing-havoc-online/)

My main question is what does `dns.js` do? What part of node is it a part of? How can I recreate this error with a different domain?

---

## 2. Convert string to integer in Shopify Liquid?
**Score:** 58 | **Tags:** type-conversion, shopify, liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/27198710/convert-string-to-integer-in-shopify-liquid

I just read this related answer:

[How can I convert a number to a string? - Shopify Design — Ecommerce University](https://ecommerce.shopify.com/c/ecommerce-design/t/how-can-i-convert-a-number-to-a-string-185373)

> To convert a string to a number just add 0 to the variable:
>
> {% assign variablename = variablename | plus:0 %}
>
> Not super elegant but it works!

Inelegant or not, the answer given there isn't working for me. What's the right way to do this?

Are the Liquid docs really missing such basic answers or am I just not finding the right place to look?

---

## 3. Enabling Liquid templating syntax highlight in webStorm/phpStorm
**Score:** 48 | **Tags:** syntax-highlighting, shopify, webstorm, liquid, textmatebundles | **Answered:** True
**Link:** https://stackoverflow.com/questions/29123188/enabling-liquid-templating-syntax-highlight-in-webstorm-phpstorm

I wonder if someone managed to enable the [Liquid templating engine](http://liquidmarkup.org/) syntax highlighting in [WebStorm IDE](https://www.jetbrains.com/webstorm/), I work a lot on [Shopify](http://www.shopify.com/) stores and really like using Webstorm for that purpose. Did anyone managed to get this working?

I found some resources regarding this issue on JetBrain's forum though it didn't quite got me anywhere, there is one dude who suggested using '[tmBundle](https://github.com/Shopify/liquid-tmbundle/)' and that might work if you do some dark magic.

The thread is: [RUBY-7210](http://youtrack.jetbrains.com/issue/RUBY-7210)
and the official plugin request: [JetBrain's plugins: Liquid Templating language request](https://plugins.jetbrains.com/wishlist/show?pr=&wid=404)

---

## 4. webpack-merge merge is not a function
**Score:** 42 | **Tags:** reactjs, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/62851934/webpack-merge-merge-is-not-a-function

I have trying to add react in the shopify theme. So configured react, webpack, babel manually.
Webpack.dev.js

```
const merge  = require('webpack-merge');
const common = require("./webpack.common.js")

module.exports = merge(common, {
  mode: "development",
  devtool: "inline-source-map",
  watch: true
})
```

But I am getting error, merge is not a function.
Thanks in advance.

---

## 5. FlashList&#39;s rendered size is not usable
**Score:** 34 | **Tags:** react-native, shopify, react-native-flatlist | **Answered:** True
**Link:** https://stackoverflow.com/questions/73516978/flashlists-rendered-size-is-not-usable

I am migrating from `FlatList` to `FlashList`, i have upgraded my expo sdk from `45.0.0` to `46.0.0` and on implementing the `FlashList` as in the shopify/flashlist documentation i get the following warning

> FlashList's rendered size is not usable. Either the height or width is too small (<2px). Please make sure that the parent view of the list has a valid size. FlashList will match the size of the parent.

It was working fine with `FlatList`, only that it took to much time to load data from api,,,thats why i decided to switch to `FlashList`. Anyone know how to fix this?Any help is appreciated. here is my code

**renderItem function**

```
    const renderItem = ({ item: product }) => {
    return (
      <Product
        category={product.bp_product_category}
        itemname={product.bp_product_name}
        price={product.bp_product_selling_price}
        mass={product.bp_product_mass}
        unitofmass={product.bp_product_unit_of_mass}
        productID={product._id}
      />
    );
    };


      const keyExtractor = useCallback((item) => item._id, []);
      const filteredproducts = products.filter((product, i) =>
      product.bp_product_name.toLowerCase().includes(search.toLowerCase())
       );
```

**FlashList it self**

```
    <View style={{flex:1, width:'100%', height:'100%'}} >
       <FlashList
          keyExtractor={keyExtractor}
          data={filteredproducts}
          renderItem={renderItem}
          estimatedItemSize={200}
          numColumns={2}
          refreshing={refresh}
          onRefresh={Refresh}
          contentContainerStyle={{
            // alignSelf: "flex-start",
            // justifyContent: "space-between",
            // paddingBottom: 120,
          }}
      />
   </View>
```

---

## 6. How do I set up a session value in Capybara?
**Score:** 33 | **Tags:** ruby-on-rails, capybara, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/8546839/how-do-i-set-up-a-session-value-in-capybara

I am developing an app for Shopify and I want to do integration testing.

I need to be able to store some values in the session variable, so that authentication works.

How could I do that?

I use Capybara and Capybara-webkit.

---

## 7. Adding custom CSS and JS to Shopify
**Score:** 29 | **Tags:** javascript, jquery, html, css, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/20467240/adding-custom-css-and-js-to-shopify

I am working on getting vertical tabs for a page on Shopify, using the 'Atlantic' theme.
As this theme does not have vertical tabs by default, I have used the external JS and CSS "jquery-jvert-tabs".

My question is, if I upload the JS and CSS files as assets, how do I link them to the page on which I want to use these and how to make use of these on the page after that, if I have certain style elements available there too?

---

## 8. Shopify Theme with Compass and Sass
**Score:** 29 | **Tags:** sass, compass-sass, liquid, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/11237792/shopify-theme-with-compass-and-sass

Does anyone have a workflow for developing Shopify themes with Compass and Sass? I am really close, I just need to figure out how to not make Sass barf on the CSS liquid tags.

Here's what I've got:

* A sass/compass project in directory (ex:, "/newwebsite/)
* A subdirectory containing my Shopify theme ("/newwebsite/newwebsite-theme/")
* A Compass config.rb that points the css,\_dir images\_dir and javascripts\_dir all to the them's assets folder ("/newwebsite/newwebsite-theme/assets/")
* Compass watch on
* shopify\_theme gem also watch on, uploading theme files to shopify (https://github.com/Shopify/shopify\_theme)
* EDIT Sass interpolations (see anser below)
* EDIT Compass callback to rename to .css.liquid

The problem: Compass barf's when you need to use Shopify's liquid templating tags, for example, a background image - example, background: url( "{{ "splash-1.jpg" | asset\_url }}")

Does anyone know how to instruct Compass / Sass to spit out the liquid template tags as they are into the CSS? If I have that, then I have a solid workflow of editing Sass locally, and realizing the changes momentarily after on the shopify shop.

Thanks

EDIT:
By using Hopper's answer below for the liquid tags in Sass, and renaming the Compass output .css file to .css.liquid, I now have an instantaneous workflow for designing a Shopify theme with Compass and Sass!
Here is the code for the Compass callback that goes in the config.rb:

```
on_stylesheet_saved do |filename|
  s = filename + ".liquid"
  puts "copying to: " + s
  FileUtils.cp(filename, s)
  puts "removing: " + filename
end
```

---

## 9. Accessing API works fine with cURL but not with Fetch API
**Score:** 29 | **Tags:** javascript, curl, shopify, fetch-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/53506848/accessing-api-works-fine-with-curl-but-not-with-fetch-api

I know this has been addressed a *lot* of times on SO, but all the answers are mostly in the vein of "add a certain header to the server". In this case, the API (Shopify) works perfectly fine and can easily be accessed via curl.

I've tried this both with the Axios library and the Fetch API.

* I've tried every value for `referrer`, `mode`, and `referrerPolicy` in the Fetch options.
* I've confirmed my BasicAuth credentials are correct.
* I've tried in multiple browsers.
* I've tried from both localhost, localhost.com (set the value in my /etc/hosts), and from a server with a real domain name.

I can't understand why this would work perfectly fine in cURL, but not with fetch().

Here's a shortened version of my code:

```
const apiKey = 'mykey';
const apiPassword = 'mypass';
const apibase = 'https://my-shop-domain.myshopify.com/admin/';
const endpoint = 'locations.json';

var headers = new Headers({
   "Authorization": "Basic " + btoa( apiKey + ':' + apiPassword ),
});

    fetch( apibase + endpoint {
      method: 'GET',
      headers: headers,
      mode: 'no-cors',
      // cache: "no-store",
      // referrer: "client",
      // referrerPolicy: "origin",
      // credentials: 'include'
    }).then( resp => resp.json().then( resp => {

      console.log( resp );

    })).catch( err => {

      console.error(err);

    });
```

and the error that returns is

> Access to fetch at '<https://my-shop-domain.myshopify.com/admin/locations.json>' from origin '<https://localhost:8080>' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.

If Shopify doesn't include the **Access-Control-Allow-Origin** header, why does the request work fine with cURL? There are node libraries and Ruby libraries to access the Shopify API, so it's hard to believe that they simply don't allow access from javascript at all.

So I guess my question is what can I do to access this API from with javascript?

---

## 10. How do I retrieve a specific product in Shopify Liquid?
**Score:** 28 | **Tags:** product, handle, shopify, liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/13269125/how-do-i-retrieve-a-specific-product-in-shopify-liquid

I have a list of product handles, and I want to fetch the product based on this handle. It seems there is no way to tell Liquid to go and get a single product. I could do this with the API, but if I use the API then I have to use JavaScript, and I would have to copy the HTML which I already have in a snippet, and copy the logic too.

A cut down version of what I am attempting:

```
{% assign handle = 'my-product-handle' %}
{% assign product = products.handle %}
{% include 'snippet-product-item' %}
```

---

## 11. Date Math / Manipulation in Liquid Template Filter
**Score:** 27 | **Tags:** date, shopify, liquid, liquid-layout | **Answered:** True
**Link:** https://stackoverflow.com/questions/21056965/date-math-manipulation-in-liquid-template-filter

I'm constructing an "Integration URL" in Desk.com, which uses the Shopify Liquid Template filter syntax. This URL needs to contain a "start date" and an "end date" for a query where the start date is 7 days ago and the end date is right now.

To achieve this I think I need to subtract 7 days (604800 in Epoch time) from the 'now' object and then apply my formatting but I can't figure out valid syntax for that.

For the current time, this syntax is valid and working:

```
{{'now' | date: "%b %d, %Y %I:%M %p -0500" | uri_encode | replace:"+","%20"}}
```

For 7 days ago, here's the best I could come up with (isn't working):

```
{{'now' | minus : 604800 | date: "%b %d, %Y %I:%M %p -0500" | uri_encode | replace:"+","%20"}}
```

Any suggestions on a valid syntax for "7 days ago" in Liquid? Would greatly appreciate any advice!

---

## 12. Print_r equivalent in Liquid
**Score:** 24 | **Tags:** ruby-on-rails, liquid, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/6174665/print-r-equivalent-in-liquid

In Liquid, how can I find out all the values that a collection contains? Is there a `print_r` function or similar?

The example below will return the item title, but I would like to know what other variables item also holds.

```
item.title
```

Thanks.

---

## 13. How to develop Shopify themes locally?
**Score:** 24 | **Tags:** shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/38803486/how-to-develop-shopify-themes-locally

I'm going to work on a Shopify theme, and I want to figure out how to run/edit it locally. I'd like to be able to the following, if possible:

1. Pull all the Shopify theme code from the site to my local computer (ideally a single command line tool)
2. Make edits locally, and run them locally or in a staging environment
3. Push all the edits to the main Shopify site, again using a command line tool

Is this at all possible?

---

## 14. Setting Content-Type in Django HttpResponse object for Shopify App
**Score:** 23 | **Tags:** python, django, http, httpresponse, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/17548414/setting-content-type-in-django-httpresponse-object-for-shopify-app

I'm working on a Shopify app using Django, which I am hosting on a VPS with nginx and gunicorn.

I am trying to change the Content-Type of an HttpResponse object to `application/liquid`, so that I can use Shopify's [application proxy feature](http://docs.shopify.com/api/tutorials/application-proxies), but it doesn't appear to be working.

Here is what I believe to be the relevant section of my code:

```
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template import RequestContext
import shopify
from shopify_app.decorators import shop_login_required

def featured(request):
   response = HttpResponse()
   response['content_type'] = 'application/liquid; charset=utf-8'
   response['content'] = '<html>test123</html>'
   response['Content-Length'] = len(response.content)
   return response
```

According to the [Django docs](https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponse), I should set `response[''content_type]` in order to set `Content-Type` in the header. Unfortunately, when I go to the URL corresponding to this function in views.py, I get a 200 response but the Content-Type has not changed and Content-Length is 0. Here are my response headers:

```
HTTP/1.1 200 OK
Server: nginx
Date: Tue, 09 Jul 2013 12:26:59 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 0
Connection: keep-alive
X-Request-Id: 2170c81fb16d18fc9dc056780c6d92fd
content: <html>test123</html>
vary: Cookie
content_type: application/liquid; charset=utf-8
P3P: CP="NOI DSP COR NID ADMa OPTa OUR NOR"
```

If I change `response['content_type']` to `response['Content-Type']`, I get the following headers:

```
HTTP/1.1 200 OK
Server: nginx
Date: Tue, 09 Jul 2013 12:34:09 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3097
Connection: keep-alive
X-Request-Id: 76e67e04b753294a3c37c5c160b42bcb
vary: Accept-Encoding
status: 200 OK
x-shopid: 2217942
x-request-id: 6e63ef3a27091c73a9e3fdaa03cc28cb
x-ua-compatible: IE=Edge,chrome=1
p3p: CP="NOI DSP COR NID ADMa OPTa OUR NOR"
content-encoding: gzip
P3P: CP="NOI DSP COR NID ADMa OPTa OUR NOR"
```

Any ideas on how I can change the Content-Type of the response? Might this be a problem with my nginx or gunicorn configurations?

Thanks for your help!

---

## 15. How can I split a string by newline in Shopify?
**Score:** 22 | **Tags:** shopify, liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/27694610/how-can-i-split-a-string-by-newline-in-shopify

I have a field in my `settings.html` where I am expecting the user to input multiple paragraphs separated by two newline characters. I would like to split this string of input into an array of strings, each representing a paragraph.

I would like to do something like this:

```
{% assign paragraphs = settings.intro | split: '\n' %}
{% for paragraph in paragraphs %}
    <p>
        {{ paragraph }}
    </p>
{% endfor %}
```

I can't seem to figure out how to refer to the newline character in Liquid. How can I go about doing this? Is there some kind of work around?

---

## 16. Shopify - New order using the Shopify API - how to know tax and shipping?
**Score:** 21 | **Tags:** shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/43311968/shopify-new-order-using-the-shopify-api-how-to-know-tax-and-shipping

We have built an e-commerce web application (`Node` backend, `Vue` frontend). We process the payment using Stripe, but many brands have asked us if the order and inventory control can be done in Shopify. We are trying to figure out the best way integrate a payment module into Shopify so that the brand can manage the fulfilment and inventory through Shopify.

It seems we should use the Order API to create an order and mark it as paid. But how do we know that the product is in stock, and what are the cost for shipping and tax from Shopify when creating the order? I think we can use the Product API to get inventory levels, but where is the shipping and tax endpoints?

**If I understand the Order API correctly, we need to tell Shopify what are the shipping costs and tax costs, when a new order is created. Is that right? How could we possibly know those figures? Seems like there should be an endpoint to calculate shipping costs and get a product's tax rates so that we can then pass those figures back into the Order API. Am I missing something?**

I thought maybe we are supposed to create an order that has `financial_status: pending` first to get shipping and tax rates back (does it even give you those?), then update the order to either `cancel_reason: customer` or `cancel_reason: inventory` if those rates are too expensive and the order is declined? But surely we need to know what shipping methods are available to the customer in order to tell Shopify which one to use, right? Or does it by default choose the cheapest one when creating an order?

**Notes:**

* We know the customers shipping address
* We don't know where the product is warehoused (Shopify does I think)
* We don't know the weights or dimensions of the product (Shopify does I think)

---

## 17. python requests - encoding with &#39;idna&#39; codec failed (UnicodeError: label empty or too long) error
**Score:** 20 | **Tags:** python, request, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/51901399/python-requests-encoding-with-idna-codec-failed-unicodeerror-label-empty-o

An api call I have been using with the requests package is suddenly returning the following error:
"UnicodeError: encoding with 'idna' codec failed (UnicodeError: label empty or too long)"

and I have no clue how to fix this. My code looks like the following, with certain credentials faked for this example:

```
api_key= '123abc'
password = '12345' #password that only idiots use on their luggage
shop_name = 'myshopname'
shop_url = 'https://%s:%s@%s.myecommercesite.com/admin/customers/1234567.json' %(api_key, password, shop_name)

a = requests.get(shop_url)
```

when I print the shop\_url and paste it into my browser, I get the data returned that I am expecting in a json. But when I run this request, I get the idna codec error.

This used to work without problem, but something changed somewhere apparently, and I'm not sure if it is with the ecommerce site or with requests or what that is causing this.

Has anyone encountered this type of error or know how to fix it?

if I print the url, it would look like:
https://123abc:12345@myshopname.myecommercesite.com/admin/customers/1234567.json

edit2:
forgot to include %(api\_key, password, shop\_name) on my code example
edit:
entire error message below:

```
UnicodeError                              Traceback (most recent call last)
~/anaconda3/lib/python3.6/encodings/idna.py in encode(self, input, errors)
    164                 if not (0 < len(label) < 64):
--> 165                     raise UnicodeError("label empty or too long")
    166             if len(labels[-1]) >= 64:

UnicodeError: label empty or too long

The above exception was the direct cause of the following exception:

UnicodeError                              Traceback (most recent call last)
<ipython-input-15-f834b116b751> in <module>()
----> 1 a = requests.get(shop_url)

~/anaconda3/lib/python3.6/site-packages/requests/api.py in get(url, params, **kwargs)
     70 
     71     kwargs.setdefault('allow_redirects', True)
---> 72     return request('get', url, params=params, **kwargs)
     73 
     74 

~/anaconda3/lib/python3.6/site-packages/requests/api.py in request(method, url, **kwargs)
     56     # cases, and look like a memory leak in others.
     57     with sessions.Session() as session:
---> 58         return session.request(method=method, url=url, **kwargs)
     59 
     60 

~/anaconda3/lib/python3.6/site-packages/requests/sessions.py in request(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)
    497 
    498         settings = self.merge_environment_settings(
--> 499             prep.url, proxies, stream, verify, cert
    500         )
    501 

~/anaconda3/lib/python3.6/site-packages/requests/sessions.py in merge_environment_settings(self, url, proxies, stream, verify, cert)
    670             # Set environment's proxies.
    671             no_proxy = proxies.get('no_proxy') if proxies is not None else None
--> 672             env_proxies = get_environ_proxies(url, no_proxy=no_proxy)
    673             for (k, v) in env_proxies.items():
    674                 proxies.setdefault(k, v)

~/anaconda3/lib/python3.6/site-packages/requests/utils.py in get_environ_proxies(url, no_proxy)
    690     :rtype: dict
    691     """
--> 692     if should_bypass_proxies(url, no_proxy=no_proxy):
    693         return {}
    694     else:

~/anaconda3/lib/python3.6/site-packages/requests/utils.py in should_bypass_proxies(url, no_proxy)
    674     with set_environ('no_proxy', no_proxy_arg):
    675         try:
--> 676             bypass = proxy_bypass(netloc)
    677         except (TypeError, socket.gaierror):
    678             bypass = False

~/anaconda3/lib/python3.6/urllib/request.py in proxy_bypass(host)
   2610             return proxy_bypass_environment(host, proxies)
   2611         else:
-> 2612             return proxy_bypass_macosx_sysconf(host)
   2613 
   2614     def getproxies():

~/anaconda3/lib/python3.6/urllib/request.py in proxy_bypass_macosx_sysconf(host)
   2587     def proxy_bypass_macosx_sysconf(host):
   2588         proxy_settings = _get_proxy_settings()
-> 2589         return _proxy_bypass_macosx_sysconf(host, proxy_settings)
   2590 
   2591     def getproxies_macosx_sysconf():

~/anaconda3/lib/python3.6/urllib/request.py in _proxy_bypass_macosx_sysconf(host, proxy_settings)
   2560             if hostIP is None:
   2561                 try:
-> 2562                     hostIP = socket.gethostbyname(hostonly)
   2563                     hostIP = ip2num(hostIP)
   2564                 except OSError:

UnicodeError: encoding with 'idna' codec failed (UnicodeError: label empty or too long)
```

---

## 18. Get shopify Metafields for products in one call
**Score:** 20 | **Tags:** php, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/11019763/get-shopify-metafields-for-products-in-one-call

I have been trying to get metafields for over 100 products and that means I have to make separate 100 api calls for each product. If there is a way to grab all metafields for all products just in one xml file like the way variants are attached to products. So that with one api call, i grab all 100 products instead of making 100 separate api call for each product. Any help is appreciated.

---

## 19. Shopify App development tutorials
**Score:** 20 | **Tags:** shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/29456778/shopify-app-development-tutorials

I'm not sure if this is the right forum since I do not have a specific development question - but here goes :)

I'm looking into creating a Shopify app to use on my Shopify shop's frontend.
I've been looking through the Shopify documentation and the API seems great - and it looks like a breeze to get up and running with an app (a private app at least).

But how do I use the app after I've created it?
Let's say I create a new ASP.NET MVC site with a single controller (Home -> Index) that returns a view that simply says "Hello World". (in the future the controller would of course call the API and the View would do amazing stuff with the data etc.)

Now I would like to use this amazing site as an app on my Shopify shop's frontend.
How in the world do I do this? :)

I can find a lot of tutorials about how to call the API and how to setup a private app in the Shopify admin - but how do I actually use this app on my frontend?
I'm not looking for an explanation about public apps and OAuth etc. (although a tutorial for this would be great too) - but for starters just a tutorial on creating and using a private app.

Any great tutorials / Udemy courses / Pluralsight videos etc. out there I've missed?

Thanks guys.

---

## 20. Tampermonkey ignores @exclude
**Score:** 19 | **Tags:** javascript, google-chrome, shopify, tampermonkey | **Answered:** True
**Link:** https://stackoverflow.com/questions/25864833/tampermonkey-ignores-exclude

I'm working on the translation of the dashboard/admin of [Shopify](http://www.shopify.com/?ref=microapps) using Tampermonkey.

For security purposes, there's some parts of the [Shopify](http://www.shopify.com/?ref=microapps) Admin Dashboard I don't want Tampermonkey to work with.
There's text created by the merchant (in products, pages, collections, templates...) which Tampermonkey would replace which is really dangerous.

There's 2 approaches to solve this:

1. "Instruct" Tampermonkey not to translate the content inside forms. (which seems to be the best approach)
2. Use the `@exclude` directive.

I've used the latter but the script is not listening to @exclude. Here is the userscript:

```
// ==UserScript==
// @name       Shopify_Admin_Spanish
// @namespace  http://*.myshopify.com/admin
// @version    0.1
// @description  Tu tienda Shopify, por detrás, en español!
// @exclude    https://*.myshopify.com/admin/products
// @exclude    https://*.myshopify.com/admin/collections
// @exclude    https://*.myshopify.com/admin/blogs
// @exclude    https://*.myshopify.com/admin/pages
// @exclude    https://*.myshopify.com/admin/themes
// @match      https://*.myshopify.com/*
// @copyright  microapps.com
// ==/UserScript==
```

PS. I did all checks using Google Chrome, and am not willing to use any other browser.

---

## 21. Overriding difficult view model
**Score:** 18 | **Tags:** javascript, jquery, html, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/32252575/overriding-difficult-view-model

I am trying to replace some text in an input field using JS but the view model overrides my commands each time. This is the HTML I start with:

```
<td class="new-variants-table__cell" define="{ editVariantPrice: new Shopify.EditVariantPrice(this) }" context="editVariantPrice" style="height: auto;">
    <input type="hidden" name="product[variants][][price]" id="product_variants__price" value="25.00" bind="price" data-dirty-trigger="true">
    <input class="mock-edit-on-hover tr js-no-dirty js-variant-price variant-table-input--numeric" bind-event-focus="onFocus(this)" bind-event-blur="onBlur(this)" bind-event-input="onInput(this)">
</td>
```

I run this JS:

```
jQuery('#product_variants__price').siblings().removeAttr('bind-event-focus');
jQuery('#product_variants__price').siblings().removeAttr('bind-event-input');
jQuery('#product_variants__price').siblings().removeAttr('bind-event-blur');
jQuery('#product_variants__price').siblings().focus()
jQuery('#product_variants__price').siblings().val("34.00");
jQuery('#product_variants__price').val("34.00");
```

And I'm left with the following HTML:

```
<td class="new-variants-table__cell" define="{ editVariantPrice: new Shopify.EditVariantPrice(this) }" context="editVariantPrice" style="height: auto;">
    <input type="hidden" name="product[variants][][price]" id="product_variants__price" value="34.00" bind="price" data-dirty-trigger="true">
    <input class="mock-edit-on-hover tr js-no-dirty js-variant-price variant-table-input--numeric">
</td>
```

The problem is that each time I click the input field the value is reverted to what it was when the page loaded.

I've also tried running the command in the parent td along with my value change, to simulate the editing of a variant and preventing default with no success:

```
jQuery('#product_variants__price').siblings().bind('input', function (e) {
    e.preventDefault();
    return false;
});
jQuery('#product_variants__price').siblings().bind('focus', function (e) {
    e.preventDefault();
    return false;
});
jQuery('#product_variants__price').siblings().focus()
jQuery('#product_variants__price').siblings().val("£34.00");
jQuery('#product_variants__price').val("£34.00");
jQuery('#product_variants__price').siblings().keydown()
```

Parent td function:

```
new Shopify.EditVariantPrice(jQuery('#product_variants__price').parent())
```

**So how can I successfully edit this value in the inputs and also update the Shopify view model?**

You can try this for yourself by going here:

> <https://jebus333.myshopify.com/admin/products/2521183043>
>
> login jebus333@mailinator.com
> password shop1

EDIT: I've tried to find the view model on the page but with no success. Plus, there are no network calls when editing the values in the input fields, leading me to believe the values are being pulled back from somewhere on page.

---

## 22. Format liquid(Shopify) code in visual studio code
**Score:** 18 | **Tags:** visual-studio, shopify, liquid, code-formatting | **Answered:** True
**Link:** https://stackoverflow.com/questions/50384369/format-liquidshopify-code-in-visual-studio-code

How to format .liquid (Shopify liquid) code in Visual Studio.
By settings language as HTML I can do it but at the same time, I can't use Shopify autocomplete. When I switch to liquid.html then I can use the autocomplete but I can't format code. Is there any way I can use another language and format code as another language in visual studio?

---

## 23. Web API 2 return OK response but continue processing in the background
**Score:** 16 | **Tags:** asp.net-mvc-4, shopify, asp.net-web-api2 | **Answered:** True
**Link:** https://stackoverflow.com/questions/27060447/web-api-2-return-ok-response-but-continue-processing-in-the-background

I have create an mvc web api 2 webhook for shopify:

```
public class ShopifyController : ApiController
{
    // PUT: api/Afilliate/SaveOrder
    [ResponseType(typeof(string))]
    public IHttpActionResult WebHook(ShopifyOrder order)
    {
        // need to return 202 response otherwise webhook is deleted
        return Ok(ProcessOrder(order));
    }
}
```

Where `ProcessOrder` loops through the order and saves the details to our internal database.

However if the process takes too long then the webhook calls the api again as it thinks it has failed. Is there any way to return the `ok` response first but then do the processing after?

Kind of like when you return a redirect in an mvc controller and have the option of continuing with processing the rest of the action after the redirect.

Please note that I will always need to return the ok response as Shopify in all it's wisdom has decided to delete the webhook if it fails 19 times (and processing too long is counted as a failure)

---

## 24. Shopify order webhooks
**Score:** 16 | **Tags:** shopify, webhooks | **Answered:** True
**Link:** https://stackoverflow.com/questions/12738309/shopify-order-webhooks

I looked into the different order webhooks and was wondering when they are triggered. This is what I figured out so far:

1. `orders/updated` is fired whenever an order is changed in any way, including when an order is created (even before it was authorized and `orders/create` is fired), closed or cancelled
2. `orders/create` is fired when the user authorizes the payment
3. `orders/paid` is fired when the merchant accepts the payment
4. `orders/fulfilled` is fired when the merchant fulfills the order
5. `orders/cancelled` is fired when the order is cancelled

Since `orders/updated` is also fired whenever the other hooks are fired, it seems as if adding an update webhook would be good enough for keeping a local datastore synced to the shop data. However, I want to confirm that my understanding of those webhooks is correct, i.e. is it true that `orders/updated` is always fired whenever an order changes in any way. and that the other webhooks are just aimed at more specific use cases?

---

## 25. Shopify: get current logged in user ID in JavaScript
**Score:** 15 | **Tags:** javascript, ajax, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/25501391/shopify-get-current-logged-in-user-id-in-javascript

I'm trying to build an app for shopify and I'm interested if I can get the current logged user ID using javascript api or something similar.
I was looking at the ajax api: <http://docs.shopify.com/support/your-website/themes/can-i-use-ajax-api> and I can see you can get the current products that the current user has added to his shopping cart, but nothing about the user ID.

Is it possible, or am I missing something?

---

## 26. Custom made sections not appearing with Shopify&#39;s new theme editor
**Score:** 15 | **Tags:** themes, shopify, liquid, sections | **Answered:** True
**Link:** https://stackoverflow.com/questions/39865010/custom-made-sections-not-appearing-with-shopifys-new-theme-editor

With the release of the new theme editor I've been assigned to build a new client's website using Shopify's new theme builder framework.

Everything has been going fine except that when I go to create a new 'Section' in the backend it fails to appear within the Theme Editor's 'Sections' area.

Any idea what's going wrong here? Is there another JSON file that is associated with sections that I'm missing?

```
<div id="callToActions">
  <div class="grid grid--no-gutters">
    <div class=""></div>
  </div>
</div>



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
  ]
}
{% endschema %}
```

---

## 27. How to catch the HTTP POST request sent by a Shopify Webhook
**Score:** 15 | **Tags:** php, ruby-on-rails, shopify, webhooks | **Answered:** True
**Link:** https://stackoverflow.com/questions/10937198/how-to-catch-the-http-post-request-sent-by-a-shopify-webhook

I'm somewhat of a noob, and not afraid to admit that, I'm working on this project as a learning experience to get better with php and serverside script/ing handling.

I'm trying to come up with a way to use Shopify and simultaneously update an off server database every time an order is fulfilled from my Shopify cart. So for example, someone buys something from my online store, I want it to update my home databases inventory to show that it now has one less item.

I've come to the conclusion that the best way to do this would be to setup a [webhook notification](http://api.shopify.com/webhook.html) that sends an HTTP POST request to my server, then I'd have my server catch the POST and parse it into an XML. I will then read the XML via a php script that will update my database.

I dont have a problem with the php, but what I can't seem to figure out is how to catch the webhook on my server. Webhook asks me for a URL to send the POST request to, my question to you is; what is the url?

I've done some research and found that you can catch the POST request a number of ways, through html, php, Access-Control-Allow-Origin, etc. However, since I'm still new to this, I don't really understand exactly how to do these. I've tried with an HTML hidden action form but couldn't seem to get it to catch the XML.

All I want to do is have the webhook send its POST request, and have it caught as a .xml. So that I can read the xml at the end of each day, and update the database accordingly.

If you can think of a better or simpler way to do this, by all means please give me your suggestions. I'd like this to be secure, so methods like Access-Control-Allow-Origin are out of the question.

tl;dr:
What do I have to do on my server to catch a webhook notification? What script should I have on my server to give to the webhook? How do I write the callback script?

---

## 28. An error occurred while installing pg (0.21.0), and Bundler cannot continue
**Score:** 15 | **Tags:** ruby, ubuntu, bundle, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/46913424/an-error-occurred-while-installing-pg-0-21-0-and-bundler-cannot-continue

I am trying to follow [this tutorial about Shopify Apps](https://github.com/Shopify/shopify_app/blob/master/docs/Quickstart.md).
First I try:

> bundle install

**But it gives me this error**

```
Gem::Ext::BuildError: ERROR: Failed to build gem native extension.

    current directory: /tmp/bundler20171024-12759-18v2l7apg-0.21.0/gems/pg-0.21.0/ext
/usr/bin/ruby2.3 -r ./siteconf20171024-12759-2yizk4.rb extconf.rb
checking for pg_config... yes
Using config values from /usr/bin/pg_config
You need to install postgresql-server-dev-X.Y for building a server-side extension or libpq-dev for
building a client-side application.
You need to install postgresql-server-dev-X.Y for building a server-side extension or libpq-dev for
building a client-side application.
checking for libpq-fe.h... no
Can't find the 'libpq-fe.h header
*** extconf.rb failed ***
Could not create Makefile due to some reason, probably lack of necessary
libraries and/or headers.  Check the mkmf.log file for more details.  You may
need configuration options.

Provided configuration options:
    --with-opt-dir
    --without-opt-dir
    --with-opt-include
    --without-opt-include=${opt-dir}/include
    --with-opt-lib
    --without-opt-lib=${opt-dir}/lib
    --with-make-prog
    --without-make-prog
    --srcdir=.
    --curdir
    --ruby=/usr/bin/$(RUBY_BASE_NAME)2.3
    --with-pg
    --without-pg
    --enable-windows-cross
    --disable-windows-cross
    --with-pg-config
    --without-pg-config
    --with-pg_config
    --without-pg_config
    --with-pg-dir
    --without-pg-dir
    --with-pg-include
    --without-pg-include=${pg-dir}/include
    --with-pg-lib
    --without-pg-lib=${pg-dir}/lib

To see why this extension failed to compile, please check the mkmf.log which can be found here:

  /tmp/bundler20171024-12759-18v2l7apg-0.21.0/extensions/x86_64-linux/2.3.0/pg-0.21.0/mkmf.log

extconf failed, exit code 1

Gem files will remain installed in /tmp/bundler20171024-12759-18v2l7apg-0.21.0/gems/pg-0.21.0 for
inspection.
Results logged to
/tmp/bundler20171024-12759-18v2l7apg-0.21.0/extensions/x86_64-linux/2.3.0/pg-0.21.0/gem_make.out

An error occurred while installing pg (0.21.0), and Bundler cannot continue.
Make sure that `gem install pg -v '0.21.0'` succeeds before bundling.

In Gemfile:
  pg
```

But if I try:

> gem install pg -v '0.21.0'

**It also gives me error:**

```
Building native extensions.  This could take a while...
ERROR:  Error installing pg:
    ERROR: Failed to build gem native extension.

    current directory: /var/lib/gems/2.3.0/gems/pg-0.21.0/ext
/usr/bin/ruby2.3 -r ./siteconf20171024-12993-1t8i3d6.rb extconf.rb
checking for pg_config... yes
Using config values from /usr/bin/pg_config
You need to install postgresql-server-dev-X.Y for building a server-side extension or libpq-dev for building a client-side application.
You need to install postgresql-server-dev-X.Y for building a server-side extension or libpq-dev for building a client-side application.
checking for libpq-fe.h... no
Can't find the 'libpq-fe.h header
*** extconf.rb failed ***
Could not create Makefile due to some reason, probably lack of necessary
libraries and/or headers.  Check the mkmf.log file for more details.  You may
need configuration options.

Provided configuration options:
    --with-opt-dir
    --without-opt-dir
    --with-opt-include
    --without-opt-include=${opt-dir}/include
    --with-opt-lib
    --without-opt-lib=${opt-dir}/lib
    --with-make-prog
    --without-make-prog
    --srcdir=.
    --curdir
    --ruby=/usr/bin/$(RUBY_BASE_NAME)2.3
    --with-pg
    --without-pg
    --enable-windows-cross
    --disable-windows-cross
    --with-pg-config
    --without-pg-config
    --with-pg_config
    --without-pg_config
    --with-pg-dir
    --without-pg-dir
    --with-pg-include
    --without-pg-include=${pg-dir}/include
    --with-pg-lib
    --without-pg-lib=${pg-dir}/lib

To see why this extension failed to compile, please check the mkmf.log which can be found here:

  /var/lib/gems/2.3.0/extensions/x86_64-linux/2.3.0/pg-0.21.0/mkmf.log

extconf failed, exit code 1

Gem files will remain installed in /var/lib/gems/2.3.0/gems/pg-0.21.0 for inspection.
Results logged to /var/lib/gems/2.3.0/extensions/x86_64-linux/2.3.0/pg-0.21.0/gem_make.out
```

I have read that

> sudo apt-get install libpq-dev

**Should work, but, yes... error:**

```
Building dependency tree       
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 libpq-dev : Depends: libssl-dev but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```

**I am working on Ubuntu 16.04 LTS. (This is the gemfile:)**

```
source 'https://rubygems.org'

git_source(:github) do |repo_name|
  repo_name = "#{repo_name}/#{repo_name}" unless repo_name.include?("/")
  "https://github.com/#{repo_name}.git"
end


# Bundle edge Rails instead: gem 'rails', github: 'rails/rails'
gem 'rails', '~> 5.1.4'
# Use postgresql as the database for Active Record
gem 'pg', '~> 0.18'
# Use Puma as the app server
gem 'puma', '~> 3.7'
# Use SCSS for stylesheets
gem 'sass-rails', '~> 5.0'
# Use Uglifier as compressor for JavaScript assets
gem 'uglifier', '>= 1.3.0'
# See https://github.com/rails/execjs#readme for more supported runtimes
# gem 'therubyracer', platforms: :ruby

# Use CoffeeScript for .coffee assets and views
gem 'coffee-rails', '~> 4.2'
# Turbolinks makes navigating your web application faster. Read more: https://github.com/turbolinks/turbolinks
gem 'turbolinks', '~> 5'
# Build JSON APIs with ease. Read more: https://github.com/rails/jbuilder
gem 'jbuilder', '~> 2.5'
# Use Redis adapter to run Action Cable in production
# gem 'redis', '~> 3.0'
# Use ActiveModel has_secure_password
# gem 'bcrypt', '~> 3.1.7'

# Use Capistrano for deployment
# gem 'capistrano-rails', group: :development

group :development, :test do
  # Call 'byebug' anywhere in the code to stop execution and get a debugger console
  gem 'byebug', platforms: [:mri, :mingw, :x64_mingw]
  # Adds support for Capybara system testing and selenium driver
  gem 'capybara', '~> 2.13'
  gem 'selenium-webdriver'
end

group :development do
  # Access an IRB console on exception pages or by using <%= console %> anywhere in the code.
  gem 'web-console', '>= 3.3.0'
  gem 'listen', '>= 3.0.5', '< 3.2'
  # Spring speeds up development by keeping your application running in the background. Read more: https://github.com/rails/spring
  gem 'spring'
  gem 'spring-watcher-listen', '~> 2.0.0'
end

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw, :jruby]
gem 'shopify_app', '~> 7.0.0'
```

What should I do? Thank you.

---

## 29. Date comparison Logic / in Liquid Template Filter
**Score:** 15 | **Tags:** date, shopify, liquid, liquid-layout | **Answered:** True
**Link:** https://stackoverflow.com/questions/47577336/date-comparison-logic-in-liquid-template-filter

I'm attempting to create a "Pre-Order" Like mechanic where certain elements of my Shopify Liquid Template only show if the current date is more or less than the date specified in a Metafield.

As of current this is what I have including logic:

```
<!-- Check Today is correct -->
<p>Today: {{'now' | date: '%d-%m-%Y' }}</p>

<!-- This is the Metafield Output as a String -->
<p>Release Date: {{ product.metafields.Release-Date.preOrder }}</p>

<!-- Assign Variable "today_date" to the current date -->
{% assign today_date = 'now' | date: '%d-%m-%Y' %}
<!-- Assign Variable "pre_date" to the string of the metafield -->
{% assign pre_date = product.metafields.Release-Date.preOrder %}
{% if today_date > pre_date %}
  Today's date is greater than PreOrder Date
{% else %}
  Today's date is not greater than PreOrder Date
{% endif %}
```

However, even when I set the PreOrder date to 01-01-2018 it still shows the "Is greater than".

How do I correctly query this?

---

## 30. Using vue.js in Shopify liquid templates
**Score:** 15 | **Tags:** vue.js, shopify, liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/43505094/using-vue-js-in-shopify-liquid-templates

This should be simple but despite searching I was unable to find any solution to this. How do you use vue template tags within a liquid file? Since both Vue and liquid use the same curly brackets, I'm unable to render any of my view data:

```
<img src="{{ product.featured_image }}" />
```

results in:

```
<img src>
```

There are 36 products in my parent view component.

When I try to use custom delimiters:

```
new Vue({
  delimiters: ['@{{', '}}'],
```

It won't parse with Vue:

  GET <https://inkkas.com/collections/@> 404 (Not Found)

UPDATE: I'm able to access Vue data with v-bind: but I still need to be able to use delimiters also.

---

## 31. Delete the store details from PHP Application after uninstalling app from Shopify Store
**Score:** 15 | **Tags:** php, arrays, post, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/43488731/delete-the-store-details-from-php-application-after-uninstalling-app-from-shopif

I want the delete the store details from PHP Application after uninstalling the app from Shopify store which are stored in database when Application installed,

Now I got some solution for this like following:

```
$create_webhook = array('webhook'=>array( 
    'topic'=> 'app/uninstalled', 
    'address'=>'{{ mydomainname}}/uninstalled.php',
    'format'=> 'json'
));

$request_update = $shopify('POST /admin/webhooks.json ', array(), $create_webhook);
```

But can we create this webhook at installing time or any other time?

---

## 32. How can I get the URL for product&#39;s page using the Shopify API?
**Score:** 14 | **Tags:** shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/11896661/how-can-i-get-the-url-for-products-page-using-the-shopify-api

I checked out Shopify product API but result doesn't seem to return product page URL. The URL looks like resulted after some transformation on the title. Is there reliable well defined logic for this or any other method to get product page URL?

---

## 33. Shopify: How can I handle an uninstall followed by an instant re-install?
**Score:** 14 | **Tags:** shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/14418415/shopify-how-can-i-handle-an-uninstall-followed-by-an-instant-re-install

I've recently had the case that a user un-installed my Shopify app and instantly re-installed it. This caused a problem because I store all my users in a DB table.

Login/Installing works as follows:

1. The user tells me his shop URL
2. I forward the user to
   example.myshopify.com/admin/oauth/authorize where access is granted
   to my app
3. I check if that shop URL is already stored in my local
   user DB
   * If not: I request a permanent access token and forward the
     user to the plan selection page
   * If yes: I get the stored permanent access token from the user DB and log the user into my app

Uninstalling:

1. The user uninstalls my app in his Shopify backend
2. Shopify sends a webhook to my app
3. I remove that user's data from the user DB

The problem is that the webhooks are sometimes delayed. If an user uninstalls and instantly re-installs, my app will think the install is a login attempt, and will use the now invalid access token stored in the user DB.

I figured I could just check if the redirection from the authorization page contains a temporary access token, and if yes, it would be a new installation, but it seems the access token is returned even if the app has already been installed.

So my question is: How can I handle instant re-installation gracefully? Surely there's something that I'm overlooking, there can't be such a huge "logic bug" in the Shopify API?

---

## 34. How to define global variables in Liquid?
**Score:** 14 | **Tags:** shopify, liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/35094919/how-to-define-global-variables-in-liquid

Right now it seems variables I create can't communicate across files.

---

## 35. Meteor Shopify API: Post metafield to collection by collection ID
**Score:** 14 | **Tags:** javascript, meteor, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/30468836/meteor-shopify-api-post-metafield-to-collection-by-collection-id

Using [froatsnook:shopify](https://github.com/froatsnook/meteor-shopify/)

Trying to get the metafields for a collection. I have the collection ID. According to [Shopify's API Documentation](https://docs.shopify.com/api/metafield#index), I should be able to get metafields for a collection, but I'm not seeing the parameter for it.

Code:

```
getShopifyCollectionMetafields: function(collection_id) {

  // GET /admin/products/#{id}/metafields.json
  var meta = ShopifyAPI.getProductMetafields({id: collection_id});

  console.log(meta)
}
```

Which returns an empty array (which makes sense, I'm trying to pass a collection ID where it expects a product ID - but not sure what to do).

---

## 36. Incrementing variables in liquid without outputting them
**Score:** 13 | **Tags:** shopify, liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/36110738/incrementing-variables-in-liquid-without-outputting-them

I am doing a for loop in shopify, I need to increment a variable.

However, when I do

```
{% increment variable %}
```

besides incrementing it, it shows the output on the screen!

I can't believe it. Is there a way to avoid this?

Thank you

---

## 37. shopify I need to check if current page is a collection page and not a single product page
**Score:** 13 | **Tags:** shopify, liquid, liquid-layout, dotliquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/39932190/shopify-i-need-to-check-if-current-page-is-a-collection-page-and-not-a-single-pr

I am trying to check if my current page is a collection page not a single product page in some collection.

I mean for example if someone goes to collection page of shoes then I can check using collection.handle == 'Shoes' but if I select a product from that page then it will still give me true But I want my condition to be true on if it is collection page.
Thanks for your Help!

---

## 38. How to check for the existence of an element in a Liquid array (Shopify) without using join
**Score:** 13 | **Tags:** shopify, liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/50829664/how-to-check-for-the-existence-of-an-element-in-a-liquid-array-shopify-without

I want to check for array values in an array created from a "split". Is there a way to do it without doing the following:

```
{%- assign blog_tags_string = blogs.news.all_tags | join ' ' -%}

{%- if blog_tags_string contains blog_title -%}
    {%- assign is_tag_page = true -%}
{%- else -%}
    {%- assign is_tag_page = false -%}
{%- endif -%}
```

---

## 39. React Hook useCallback not updating State value
**Score:** 13 | **Tags:** reactjs, shopify, react-hooks | **Answered:** True
**Link:** https://stackoverflow.com/questions/60911179/react-hook-usecallback-not-updating-state-value

I'm new to React Hooks. I have a UI with multiple inputs with values in an object. I create the UI with a loop, so I would like to have a single callback for the updating the inputs.  
  
[![enter image description here](https://i.sstatic.net/ah1PF.png)](https://i.sstatic.net/ah1PF.png)

The code is below. The problem is in the `handleChange` callback.

```
import React, { useCallback, useState, useEffect } from "react";
import { TextField, Form } from "@shopify/polaris";

export default function TextFieldExample() {
  const [values, setValues] = useState({
    "prod-0": "Jaded Pixel",
    "prod-1": "blue diamonds"
  });
  const [shop, setShop] = useState("Joe's house of pancakes");

  const handleChangeShop = useCallback(newName => {
    setShop(newName);
  }, []);

  const handleChange = useCallback((newValue, id) => {
      console.log("Pre: values:", values);
      console.log(id, newValue);
      const newProds = values;
      newProds[id] = newValue;
      setValues(newProds);
      console.log("Post: newProds:", newProds);
    }, [values]);

  useEffect(() => {    // observing if State changes
    console.log("in useEffect: shop:", shop); // this gets called and is updated when changed.
    console.log("in useEffect: values:", values); // this never gets called or updated.
  }, [values, shop]);

  const items = [];
  Object.keys(values).forEach(function(prod) {
    items.push(
      <TextField label={"Product " + prod.substr(5)} id={prod} value={values[prod]} onChange={handleChange} />
    );
  });
  return (
    <Form>
      <TextField label="Shop" id="shop" value={shop} onChange={handleChangeShop}/>
      {items}
    </Form>
  );
}
```

Code Sandbox is here: <https://codesandbox.io/s/fast-tdd-1ip38>

---

## 40. GraphQL, Shopify Get All products or totalcount of products
**Score:** 13 | **Tags:** graphql, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/66185620/graphql-shopify-get-all-products-or-totalcount-of-products

I am brand new to graphQL and I have to retrieve all of the products. I have been looking around, watching tutorials and reading and people seem to return all of a certain type of data they want but I cannot. For example it will throw an error saying you must provide first or last but I want them all or it will say totalCount or count does not exist.

```
 {
  products {
    id
    title
    price
    
  }
}

// or get total count of products

 {
  products {
   totalCount
  }
}
```

I was basically trying to do something like that. I understand I may not receive any help because no one has access to my shopify admin api but maybe even an example or anything that I could see. This is from my graphQL query root of options I have for products.
List of products.

```
ProductConnection!
first: Int
Returns up to the first n elements from the list.

after: String
Returns the elements that come after the specified cursor.

last: Int
Returns up to the last n elements from the list.

before: String
Returns the elements that come before the specified cursor.

reverse: Boolean = false
Reverse the order of the underlying list.

sortKey: ProductSortKeys = ID
Sort the underlying list by the given key.

query: String
Supported filter parameters:

barcode
created_at
delivery_profile_id
error_feedback
gift_card
inventory_total
is_price_reduced
out_of_stock_somewhere
price
product_type
publishable_status
published_status
sku
status
tag
title
updated_at
vendor
See the detailed search syntax for more information about using filters.

savedSearchId: ID
ID of an existing saved search. The search’s query string is used as the query argument.
```

---

## 41. Oauth error invalid_request: The redirect_uri is not whitelisted
**Score:** 12 | **Tags:** node.js, reactjs, shopify, next.js | **Answered:** True
**Link:** https://stackoverflow.com/questions/55918320/oauth-error-invalid-request-the-redirect-uri-is-not-whitelisted

I'm trying to develop an app with React and Node based on this [documentation](https://developers.shopify.com/tutorials/build-a-shopify-app-with-node-and-react):

I followed the tutorial step by step but I'm stuck in testing the app with this URL format:

I replaced the ngrok address and my shopify store but I get the 404 error (This page could not be found.)

I found the same question in this [link](https://community.shopify.com/c/Shopify-APIs-SDKs/Oauth-error-invalid-request-with-React-and-Node/td-p/476014). So I renamed the .env to process.env but I still have the same problem.

Here is the **.env file**:

[![enter image description here](https://i.sstatic.net/90Wlq.jpg)](https://i.sstatic.net/90Wlq.jpg)

**package.json :**

[![enter image description here](https://i.sstatic.net/WArwl.jpg)](https://i.sstatic.net/WArwl.jpg)

**server.js :**

[![enter image description here](https://i.sstatic.net/UpK5v.jpg)](https://i.sstatic.net/UpK5v.jpg)

**The error :**

[![enter image description here](https://i.sstatic.net/R3nI6.jpg)](https://i.sstatic.net/R3nI6.jpg)

---

## 42. Shopify : Errors: [API] This action requires merchant approval for write_themes scope
**Score:** 12 | **Tags:** shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/50364356/shopify-errors-api-this-action-requires-merchant-approval-for-write-themes

I am new to Shopify and I'm trying to setup Shopify themekit locally.

I have created an private app and setup my store, but while trying to access store using theme kit I get this error:

`Errors: [API] This action requires merchant approval for write_themes scope.`

---

## 43. Graphql error: &quot;using last without before is not supported&quot;
**Score:** 12 | **Tags:** javascript, ecmascript-6, graphql, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/62765178/graphql-error-using-last-without-before-is-not-supported

I am using Gatsby + GraphQL + Shopify. I am having an issue retrieving my orders by the last 10.

My query looks like this:

```
query {
   customer(customerAccessToken: "${customerAccessToken}") {
      orders(last: 10) {...}
   }
}
```

And it returns this:

> "message": "using last without before is not supported"

I noticed this issue happening to some other devs: <https://community.shopify.com/c/Shopify-Discussion/How-to-get-customer-s-orders-and-sort-by-date-in-descending/m-p/629133/highlight/false#M151241>

If you check the docs it says nothing about using `before` with `last`:
[https://shopify.dev/docs/admin-api/graphql/reference/object/order?api[version]=2020-07](https://shopify.dev/docs/admin-api/graphql/reference/object/order?api%5Bversion%5D=2020-07)

There is a playground at the bottom where you can test queries.

Anybody else has seen this issue before?

---

## 44. Using Liquid variables in JavaScript
**Score:** 12 | **Tags:** javascript, shopify, liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/51769347/using-liquid-variables-in-javascript

I'm new to using Shopify Liquid, I'm having an issue with trying to use Liquid variables in JavaScript. I have put together an Instagram feed, which I want to use as a Section so that the UserId, ClientId, and accessToken can be easily added and changed from within the CMS, rather than in the code. The problem I've got is the Liquid variables aren't being picked up.

I've added data-settings for the three fields and then added the fields to the script with no effect. The feed works, but only if I manually add the IDs and token to the script and not through Liquid.

Any help with this would be great : )

```
{% if section.settings.insta_enable != blank %}

  {% if section.settings.insta_handle %}
  <div class="ss-handle">
    <h2>be social <a href="https://www.instagram.com/{{ section.settings.insta_handle }}" target="_blank">@{{ section.settings.insta_handle }}</a></h2>
  </div>
  {% endif %}

  <div data-section-id="{{ section.id }}" id="ss-instagram-feed" data-settings='{
  "user_id": {{ section.settings.user_id }},
  "client_id": {{ section.settings.client_id }},
  "access_token": "{{ section.settings.access_token }}"
  }'></div>

<!--
Note:
"user_id": {{ section.settings.instagram_id }}, // numeric (no quotes)
"access_token": "{{ section.settings.instagram_access_token }}", // string in quotes
-->

{% endif %}


{% schema %}
  {
    "name": "Instagram Feed",
    "settings": [
      {
        "type": "header",
        "content": "Feed Configuration"
      },
      {
        "label": "Enable Instagram feed",
        "id": "insta_enable",
        "type": "checkbox"
      },
      {
        "label": "User ID",
        "id": "user_id",
        "type": "text"
      },
      {
        "label": "Client ID",
        "id": "client_id",
        "type": "text"
      },
      {
        "label": "Access Token",
        "id": "access_token",
        "type": "text"
      },
      {
        "label": "Insta Handle (enter without @ symbol)",
        "id": "insta_handle",
        "type": "text"
      }
    ],
    "presets": [
      {
        "name": "Instagram Feed",
        "category": "Image"
      }
    ]
  }
{% endschema %}

{% javascript %}
//<script>

function instafeed_load() {

  // JS goes here
  $(document).ready(function() {

    var settings = $('#ss-instagram-feed').data('settings');

    var feed = new Instafeed({
        clientId: 'settings.client_id', 
        accessToken: 'settings.access_token',
        get: 'user',
        userId: settings.user_id,,
        target: 'ss-instagram-feed',
        limit: 5,
        resolution: 'standard_resolution',
        template: '<li><a class="instagram-image" href="{{link}}" target="_blank"><img src="{{image}}"/></a></li>'
    });
    feed.run();

  });

  $(window).on('load', function() {
    setTimeout(function() {
      $('body, #ss-instagram-feed, h1, h3').addClass('loaded');
    }, 500);
  });

}
function instafeed_unload() {
  // you will want to do clean-up and/or destroy what you created in instafeed_load
}
function instafeed_event_handler(event) {
  // there are cleaner ways to write this, but the below works for me
  if (event.detail.sectionId == '1533732475847') { // 1533732475847 or insta-feed
    if (event.type == 'shopify:section:load') {
      instafeed_load();
    } else if (event.type == 'shopify:section:unload') {
      instafeed_unload();
    }
  }
}

$(document).on('shopify:section:load shopify:section:unload', instafeed_event_handler);
$(document).ready(function() {
  instafeed_load(); // this is to execute on initial page load
});

//</script>
{% endjavascript %}
```

---

## 45. Shopify password update using Shopify API
**Score:** 12 | **Tags:** php, shopify, change-password | **Answered:** True
**Link:** https://stackoverflow.com/questions/35794258/shopify-password-update-using-shopify-api

Can we update password for a User or Customer that already exists in Shopify using the Shopify API?

---

## 46. Shopify Toggle Cart Button location
**Score:** 12 | **Tags:** javascript, jquery, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/44480754/shopify-toggle-cart-button-location

I'm currently using the [Shopify Buy Button](https://www.shopify.com/buy-button).

For the most part, I just copy and pasted the embed code and didn't change much. If you scroll all the way down to `"toggle":{`, you'll notice I made it so **iframe** and **sticky** is set to `false`.

---

# The Issue

When a product is added to a cart, a button that toggle's the shopping cart appears in the body. `.shopify-buy-frame.shopify-buy-frame--toggle`

It normally appears as a fixed `div` on the middle right hand corner of the screen but since my **sticky** option is set to false, it is placed at the bottom of the `body`.

I'd like to be able to assign a parent container that this toggle button ends up in. Ideally, I want to put it in my header somewhere and not have it be generated at the bottom of the body of my page.

**For example:**

```
<body>

    <header>
        <div id="cart-toggle">
            <!-- THIS IS WHERE I WANT IT TO APPEAR -->
        </div>
    <header>

<!-- THIS IS WHERE IT APPEARS -->
</body>
```

**Bonus Points** if I can figure out how to generate a second toggle button for my mobile navigation area.

I've searched the [default compenents](https://github.com/Shopify/buy-button-js/blob/master/src/defaults/components.js) and the [developer section](https://github.com/Shopify/buy-button-js/blob/master/docs/customization/index.md) for the toggle options and can't seem to figure it out.

If anyone could help it would be greatly appreciated.

---

**My Embed Code**

```
<script type="text/javascript">
/*<![CDATA[*/
(function () {
  var scriptURL = 'https://sdks.shopifycdn.com/buy-button/latest/buy-button-storefront.min.js';
  if (window.ShopifyBuy){if(window.ShopifyBuy.UI){ShopifyBuyInit();}else{loadScript();}}else{loadScript();}f
  function loadScript() {var script = document.createElement('script');script.async = true;script.src = scriptURL;(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(script);script.onload = ShopifyBuyInit;}
  function ShopifyBuyInit() {
    var client = ShopifyBuy.buildClient({domain: 'domain.myshopify.com',apiKey: 'apikey',appId: '0'});
    ShopifyBuy.UI.onReady(client).then(function(ui){ui.createComponent('product',{moneyFormat:'%24%7B%7Bamount%7D%7D',
        
  options:{
    "product":{
      "variantId":"all",
      "width":"240px",
      "contents":{
        "img":false,
        "imgWithCarousel":false,
        "title":false,
        "variantTitle":false,
        "price":false,
        "description":false,
        "buttonWithQuantity":false,
        "quantity":false
      },
      "text":{
        "button":"ADD TO BAG"
      },
      "styles":{
        "product":{
          "text-align":"left",
          "@media(min-width:601px)":{
            "max-width":"100%",
            "margin-left":"0",
            "margin-bottom":"50px"
          }
        },
        "button":{
          "background-color":"#393a39",
          "font-family":"Lato,sans-serif",
          "font-size":"13px",
          "padding-top":"14.5px",
          "padding-bottom":"14.5px",
          "padding-left":"35px",
          "padding-right":"35px",
          ":hover":{
            "background-color":"#333433"
          },
          "border-radius":"0px",
          ":focus":{
            "background-color":"#333433"
          },
          "font-weight":"normal"
        },
        "title":{
          "font-size":"26px"
        },
        "price":{
          "font-size":"18px"
        },
        "quantityInput":{
          "font-size":"13px",
          "padding-top":"14.5px",
          "padding-bottom":"14.5px"
        },
        "compareAt":{
          "font-size":"15px"
        }
      },
      "googleFonts":[
        "Lato"
      ]
    },
    "cart":{

      "contents":{
        "button":true
      },
      "text":{
        "title":"Bag"
      },
      "styles":{
        "button":{
          "background-color":"#393a39",
          "font-family":"Lato,sans-serif",
          "font-size":"13px",
          "padding-top":"14.5px",
          "padding-bottom":"14.5px",
          ":hover":{
            "background-color":"#333433"
          },
          "border-radius":"0px",
          ":focus":{
            "background-color":"#333433"
          },
          "font-weight":"normal"
        },
        "footer":{
          "background-color":"#ffffff"
        }
      },
      "googleFonts":[
        "Lato"
      ]
    },
    "modalProduct":{
      "contents":{
        "img":false,
        "imgWithCarousel":true,
        "variantTitle":false,
        "buttonWithQuantity":true,
        "button":false,
        "quantity":false
      },
      "styles":{
        "product":{
          "@media(min-width:601px)":{
            "max-width":"100%",
            "margin-left":"0px",
            "margin-bottom":"0px"
          }
        },
        "button":{
          "background-color":"#393a39",
          "font-family":"Lato,sans-serif",
          "font-size":"13px",
          "padding-top":"14.5px",
          "padding-bottom":"14.5px",
          "padding-left":"35px",
          "padding-right":"35px",
          ":hover":{
            "background-color":"#333433"
          },
          "border-radius":"0px",
          ":focus":{
            "background-color":"#333433"
          },
          "font-weight":"normal"
        },
        "quantityInput":{
          "font-size":"13px",
          "padding-top":"14.5px",
          "padding-bottom":"14.5px"
        }
      },
      "googleFonts":[
        "Lato"
      ]
    },
    "toggle": {
      "iframe":false,
      "sticky":false,
      "contents":{
        "icon":true,
        "title":false
      },
      "styles":{
        "toggle":{
          "font-family":"Lato,sans-serif",
          "background-color":"#393a39",
          ":hover":{
            "background-color":"#333433"
          },
          ":focus":{
            "background-color":"#333433"
          },
          "font-weight":"normal"
        },
        "count":{
          "font-size":"13px"
        }
      },
      "googleFonts":[
        "Lato"
      ]
    },
    "productSet":{
      "styles":{
        "products":{
          "@media(min-width:601px)":{
            "margin-left":"-20px"
          }
        }
      }
    }
  }
}
);});}
})();
/*]]>*/
</script>
```

---

## 47. Active_Shipping Negotiated Rates for UPS - Ruby on Rails
**Score:** 12 | **Tags:** ruby-on-rails, ruby, ruby-on-rails-5, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/46552755/active-shipping-negotiated-rates-for-ups-ruby-on-rails

I've integrated the Shopify active\_shipping gem into my site and I am trying to get negotiated rates from my UPS account (I can get regular rates). I can't find any documentation on the negotiated rates. Can anyone help me out here? I think this line of code should work but it doesn't produce any errors or any different shipping rates.

```
response = carrier.find_rates(origin, destination, packages, {negotiated_rates: true})
```

I ran across this link here but still no luck:

<https://github.com/Shopify/active_shipping/blob/master/lib/active_shipping/carriers/ups.rb>

---

## 48. Shopify API: Create a Promotion?
**Score:** 11 | **Tags:** shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/13242989/shopify-api-create-a-promotion

Using the Shopify API, is there a way to creation promotions for your store? If not, is there a way to programmatically create promotions in Shopify? (short of using CURL posts to the admin)

That is, I can create a promotion by hand using the admin and navigating to the `Promotions` and clicking the `Add a discount code` link. I'd like to be able to do the same thing programmatically, or to know for certain this isn't possible. I don't see any obvious method on the [api list](http://api.shopify.com/), but it seems like something should be an API method.

---

## 49. what&#39;s the difference between .js and .js.liquid in shopify?
**Score:** 11 | **Tags:** shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/25983518/whats-the-difference-between-js-and-js-liquid-in-shopify

In the assets section, there are files with `.js` and `.js.liquid` names.

What is the difference between the 2, which one should I use if I want to include a js file into a theme?

This is inside a .js.liquid file right now. I would like to construct a string made up of liquid variable. when I append this string inside a DOM element, it doesn't seem to show up.

```
var someString = '';
  {%for line in order.line_items%}
  someString += 'q='+{{line.quantity}}+'&p='+{{line.product.id}}+'&pp='+{{line.price}}+'&w='+{{line.grams}}+'&i='+{{line.product.featured_image|product_img_url|url_param_escape}}+'&n='+{{line.product.title|url_param_escape}}+'&';
  {%endfor%}

$('body').append(someString);
```

---

## 50. Adding Social Login to Shopify
**Score:** 11 | **Tags:** security, authentication, shopify | **Answered:** True
**Link:** https://stackoverflow.com/questions/32564480/adding-social-login-to-shopify

I wish to add Social Login feature to a Shopify store that I am building. (I'm using the professional plan.)

I explored a few of the available social-login apps on the Shopify App Store. Upon studying closely as to how they actually work - I have come to the following understanding of the general scheme being followed by all of them.

1. The Shopify shop owner sets up a social app (e.g. Facebook app) with their store identity, but configures the Callback-URL/Redirect-URL to one supplied by the App author (i.e. pointing to their infrastructure).
2. Upon successful login by a shop customer on the social platform (via a link/button inserted on the shop login page), the request gets redirected to the App.
3. The App retrieves the user's email address from the their social profile (that they now have access to).
4. They then lookup their own database to see if this is an existing customer. If so they go directly to step 7 below.
5. If it's a new customer, they use Shopify API to create a new 'customer' on the target Shopify store. They set the customer up with a randomly generated password.
6. At the same time they also make an entry of this customer account (email + generated password) in their own database.
7. They then redirect the request back to the Shopify store's login page but this time with the customer's email address (retrieved from social platform) and their password (from the App's own database) included as part of the data that comes back to the users browser as part of loading the login page.
8. Then the App's javascript embedded on the shop login page uses the customer email address and password to programmatically submit the login form - thus establishing a valid customer session on the Shopify shop.

My questions are as follows:

1. Has someone else also looked closely in to this, and thus can validate if my above understanding is correct or not?
2. If it is correct - is this the only way to achieve social login on Shopify (without using Shopify Plus/Enterprise plan)?

I am trying to understand if this indeed is the only way, because I strongly feel that this method is not at all secure. And thus I'd rather not use this method; or if I just have to - then I'd rather write my own (private) app for this so that at least I am in control of the security of the app/database that holds sensitive users credentials.

Would appreciate any help/thoughts I can get with this, please.

---

## 51. Shopify - prepopulate billing address based on query param
**Score:** 10 | **Tags:** shopify, url-parameters, query-string, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/61508555/shopify-prepopulate-billing-address-based-on-query-param

I am trying to prepopulate the shipping/billing address in Shopify checkout via URL query params. I've found this is easy to do with the shipping address as referenced here:

<https://community.shopify.com/c/Shopify-APIs-SDKs/Autofill-checkout-fields/td-p/318793>

But when I try to do the same with the billing info, the "Same as shipping address" radio is always selected on the payment screen and if I manually select the option for a different address, all values are blank

How can I prepopulate both addresses? I've tried adding the billing query params directly to the checkout payment page URL, but that does not work either. Here is the URL I've been trying:

```
demo-store.myshopify.com/checkout?checkout[email]=fake.name@gmail.com&checkout[shipping_address][first_name]=John&checkout[shipping_address][last_name]=Doe&checkout[shipping_address][address1]=333%20Fake%20St.&checkout[shipping_address][city]=San%20Diego&checkout[shipping_address][province]=CA&checkout[shipping_address][country]=USA&checkout[shipping_address][zip]=92116&checkout[shipping_address][phone]=333-333-3333&checkout[different_billing_address]=true&checkout[billing_address][first_name]=Jane&checkout[billing_address][last_name]=Doe&checkout[billing_address][address1]=444%20Fake%20St%20&checkout[billing_address][city]=San%20Diego&checkout[billing_address][province]=CA&checkout[billing_address][country]=USA&checkout[billing_address][zip]=92121&checkout[billing_address][phone]=444-444-4444
```

Also, bonus question, the shipping state always seems to be populated based on IP address, so even if I pass it a value, it shows the state I'm in. How can I get it to always reflect the value of the query param?

---

## 52. Can not remove ERR_NGROK_6024 when using Shopify App Proxy get call
**Score:** 10 | **Tags:** shopify, shopify-app, ngrok | **Answered:** True
**Link:** https://stackoverflow.com/questions/75518334/can-not-remove-err-ngrok-6024-when-using-shopify-app-proxy-get-call

I am trying to send data using app proxy, from the localhost, I am using ngrok but not able to visit the page.

Also not able ( Or probably not knowing how to ), pass request hedges "ngrok-skip-browser-warning"

[![enter image description here](https://i.sstatic.net/82UE8.png)](https://i.sstatic.net/82UE8.png)

---

## 53. How to get the current shop in shopify when using NodeJS (Public App)?
**Score:** 10 | **Tags:** javascript, node.js, shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/69168644/how-to-get-the-current-shop-in-shopify-when-using-nodejs-public-app

I am new to Shopify App Devlopment, especially the Shopify API.

I create a working app with the Shopify CLI and now want to communicate with the API.

I try to access following endpoint: `https://{my_shop]/admin/api/2021-07/shop.json`

I learned that I need some access token and the shop name to access this endpoint.

I created an access token under my private apps section.

But I dont know how to get the currently logged in store.

For example, when clicking a button in my frontend, I would like to call my endpoint, which in turn calls the Shopify API endpoint and retrieves the information. How do I do this the right way? And how do I get the currently logged in shop?

This is my code so far:

```
import "@babel/polyfill";
import dotenv from "dotenv";
import "isomorphic-fetch";
import createShopifyAuth, { verifyRequest } from "@shopify/koa-shopify-auth";
import Shopify, { ApiVersion } from "@shopify/shopify-api";
import Koa from "koa";
import next from "next";
import Router from "koa-router";
import axios from 'axios';

dotenv.config();
const port = parseInt(process.env.PORT, 10) || 8081;
const dev = process.env.NODE_ENV !== "production";
const app = next({
  dev,
});
const handle = app.getRequestHandler();

Shopify.Context.initialize({
  API_KEY: process.env.SHOPIFY_API_KEY,
  API_SECRET_KEY: process.env.SHOPIFY_API_SECRET,
  SCOPES: process.env.SCOPES.split(","),
  HOST_NAME: process.env.HOST.replace(/https:\/\//, ""),
  API_VERSION: ApiVersion.October20,
  IS_EMBEDDED_APP: true,
  // This should be replaced with your preferred storage strategy
  SESSION_STORAGE: new Shopify.Session.MemorySessionStorage(),
});

// Storing the currently active shops in memory will force them to re-login when your server 
restarts. You should
// persist this object in your app.
const ACTIVE_SHOPIFY_SHOPS = {};

app.prepare().then(async () => {
  const server = new Koa();
  const router = new Router();
  server.keys = [Shopify.Context.API_SECRET_KEY];
  server.use(
    createShopifyAuth({
      async afterAuth(ctx) {
        // Access token and shop available in ctx.state.shopify
        const { shop, accessToken, scope } = ctx.state.shopify;
        const host = ctx.query.host;
        ACTIVE_SHOPIFY_SHOPS[shop] = scope;

        const response = await Shopify.Webhooks.Registry.register({
          shop,
          accessToken,
          path: "/webhooks",
          topic: "APP_UNINSTALLED",
          webhookHandler: async (topic, shop, body) =>
            delete ACTIVE_SHOPIFY_SHOPS[shop],
        });

        if (!response.success) {
          console.log(
            `Failed to register APP_UNINSTALLED webhook: ${response.result}`
          );
        }

        // Redirect to app with shop parameter upon auth
        ctx.redirect(`/?shop=${shop}&host=${host}`);
      },
    })
  );

  router.get("/test2", verifyRequest(), async(ctx, res) => {
    const {shop, accessToken } = ctx.session;
    console.log(shop);
    console.log(accessToken);
  })

  router.get("/test", async (ctx) => {

    const config = {
      headers: {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': 'shppa_XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
      }
    }

    await axios.get('${the_store_name_belongs_here}/admin/api/2021-07/shop.json', config).then(res => {
      ctx.body = res.data;
    });
  });

  const handleRequest = async (ctx) => {
    await handle(ctx.req, ctx.res);
    ctx.respond = false;
    ctx.res.statusCode = 200;
  };

  router.post("/webhooks", async (ctx) => {
    try {
      await Shopify.Webhooks.Registry.process(ctx.req, ctx.res);
      console.log(`Webhook processed, returned status code 200`);
    } catch (error) {
      console.log(`Failed to process webhook: ${error}`);
    }
  });

  router.post(
    "/graphql",
    verifyRequest({ returnHeader: true }),
    async (ctx, next) => {
      await Shopify.Utils.graphqlProxy(ctx.req, ctx.res);
    }
  );

  router.get("(/_next/static/.*)", handleRequest); // Static content is clear
  router.get("/_next/webpack-hmr", handleRequest); // Webpack content is clear
  router.get("(.*)", async (ctx) => {
    const shop = ctx.query.shop;

    // This shop hasn't been seen yet, go through OAuth to create a session
    if (ACTIVE_SHOPIFY_SHOPS[shop] === undefined) {
      ctx.redirect(`/auth?shop=${shop}`);
    } else {
      await handleRequest(ctx);
    }
  });


  server.use(router.allowedMethods());
  server.use(router.routes());
  server.listen(port, () => {
    console.log(`> Ready on http://localhost:${port}`);
  });
});
```

Please have a look at my attempts - endpoint `/test` and endpoint `/test2`.
test2 is not working. ctx.session is null. ctx itself is null. Why?

`test1` is working when I hard code my shops name into the url, then I get the desired data. But how do I put a shop variable inside? That's my struggle.

---

## 54. Error: write EPIPE trying to setup shopify app
**Score:** 9 | **Tags:** node.js, next.js, shopify, shopify-app, ngrok | **Answered:** False
**Link:** https://stackoverflow.com/questions/66076191/error-write-epipe-trying-to-setup-shopify-app

I tried to install a shopify app in my development store. I used both the manual way (<https://shopify.dev/tutorials/build-a-shopify-app-with-node-and-react/embed-your-app-in-shopify>) as the CLI way (<https://shopify.github.io/shopify-app-cli/getting-started/>).

I keep getting this `Error: write EPIPE at WriteWrap.onWriteComplete [as oncomplete] (internal/stream_base_commons.js:94:16)`

I don't know what I'm doing wrong and why I can't find any solution on that error. Am I really the only one facing this problem?

---

## 55. How to run Python 3 function even after user has closed web browser/tab?
**Score:** 8 | **Tags:** python, python-3.x, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/61791651/how-to-run-python-3-function-even-after-user-has-closed-web-browser-tab

I am having an issue at work with a python project I am working on (I normally use PHP/Java so am lacking a bit of knowledge).
Bascially I have a python program that I have built using Flask that connects an inventory management system to Shopify using the Shopify Python API.

When the user triggers a function via an AJAX request, I need to start a function/process that updates products in the client's Shopify store via the Shopify API. This takes about 2 hours (~7000 products plus have to pull them first from the inventory management system).
The issue is that I need a way that I can trigger this function/process, and even if the client closes their browser the function/process will continue running.

If there is any way I could update the front end with the current progress of this background function/process as well that would be swell.

If anyone knows of any library or resources for accomplishing this it would be much appreciated.
I have had a google, but all the solutions I can find seem to be for CLI scripts not Web scripts.

Thanks heaps,
Corey :)

---

## 56. Listen to shopify cart update quantity
**Score:** 8 | **Tags:** shopify, shopping-cart, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/63450607/listen-to-shopify-cart-update-quantity

I am writing a Shopify app and I would want to listen to the shopify cart update event. I know that when user clicks on remove or increase the item quantity. Shopify send a POST request to the backend to update the card. My app calculates the shipping value based on shopify cart item quantity. I add my app script to the shopify via script-tag.

I tried to listen to the quantity input but this event only fires one. I think shopify updates the input DOM after every cart update so it may remove my listener.

```
 $('body').on('change', '.input[name="updates[]"]', function() { console.log('HELLO')});
```

How can I listen to the cart update event? It seems to be a simple question but I really cannot find any answer regarding to Shopify!

---

## 57. How to integrate third party API in Shopify?
**Score:** 8 | **Tags:** shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/54859491/how-to-integrate-third-party-api-in-shopify

I have created a Shopify store and now I want to send orders to the third party e-commerce website. I have third party API but I don't know how to integrate it in my Shopify store. Could anyone explain to me the steps to make an app to integrate third party API?

PS: I am new to Shopify

---

## 58. BullMQ - Persistence job queuing &amp; managing jobs between server restart
**Score:** 8 | **Tags:** node.js, redis, shopify-app, bullmq | **Answered:** True
**Link:** https://stackoverflow.com/questions/66005917/bullmq-persistence-job-queuing-managing-jobs-between-server-restart

Little background of the task-
I'm building abandoned cart recovery system for Shopify. After an user makes a checkout, Shopify calls our webhook and the webhook enqueues that request as job with delay of 5mins in a queue A. When worker starts processing that job, it checks if that checkout has been paid yet or not. If it isn't paid yet then it sends cart recovery message to user.

I'm using Node.js, Express.js, Redis & BullMQ to implement the server and queuing system.
I have tried to go through basic examples of BUllMQ. On the web, Couldn't find some advanced examples around it to how to use this in production level system.

Right now, I'm stuck with these following questions -

1. Since, Redis is in-memory database, I must save every incoming job in my MongoDB collection, initially with status of PENDING and listen for completion event to change that status to COMPLETED in the database. Whenever my server restarts, I fetch all the jobs with PENDING status and add them to the queue. This way we can recover our jobs, even if Redis goes down or restarts. My questions are -
   **Does it make sense to do such thing in production level application?, Should I'be saving jobs in MongoDB? & What other caution should I be taking to implement this flow?**
2. Right now, Bull queue(let's name that 'A') is getting initialized in express server. Every time server restarts, queue A also gets initialized. My questions are -
   **Does re-initialization of queue A, removes old queue A on Redis ? What other things I can do around this problem?**

I would be very thankful for any help on this.

---

## 59. How to inject custom js to shopify via app
**Score:** 7 | **Tags:** javascript, laravel, shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/63842397/how-to-inject-custom-js-to-shopify-via-app

Hello I'm pretty new to shopify app development.
I created the shopify app with laravel and now I generated a js file with content. What I want is to inject this code automatically to the shopify store, so every user which installed the app the code will be added to his store autmatically. I currently read about script tags and probablly is the best way to insert with them, but it's not clear for me. I want information which will help me to figure this out. Thanks in advance

---

## 60. Nextjs: 405 when form submit POST
**Score:** 7 | **Tags:** javascript, reactjs, next.js, shopify, shopify-app | **Answered:** False
**Link:** https://stackoverflow.com/questions/70452719/nextjs-405-when-form-submit-post

Following this [tutorial](https://nextjs.org/blog/forms), I'm trying to submit a form in Nextjs but get a 405 error when trying to POST to my api route. I've tried using both axios and the fetch api. This seems like it should be simple to do but I'm not sure where I'm going wrong. Anything obvious I'm missing? Thanks!

**/survey/create**

```
const handleSubmit = async (event) => {
    event.preventDefault();

    const testData = {
      title: surveyTitle,
    };

    const res = await fetch("/api/survey", {
      method: "POST",
      body: JSON.stringify({
        dataName: testData,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
  };
```

**/api/survey**

```
export default function handler(req, res) {
  console.log(req.body);
  res.status(200).json(JSON.stringify({ name: 'Success' }))
}
```

---

## 61. Filter Products using Storefront API in shopify
**Score:** 7 | **Tags:** shopify, shopify-app, storefront | **Answered:** False
**Link:** https://stackoverflow.com/questions/51858870/filter-products-using-storefront-api-in-shopify

We are developing filters functionality using Storefront API. We can write query with operators as given below to search within parent key such as "product\_type" but we couldn't find way to search within child key.

```
.products(first: 10, query: "tag:blue AND product_type:sneaker") { $0
  ...
}
```

So can anyone help us to search within child key's such as variant selected options?

We are expecting query format like:

```
.products(first: 10, query: "selectedProductVarient.option1:M") { $0
  ...
}
```

---

## 62. Shopify API Node/Express Cannot read properties of undefined (reading &#39;Rest&#39;)
**Score:** 6 | **Tags:** node.js, express, shopify, shopify-app, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/69920772/shopify-api-node-express-cannot-read-properties-of-undefined-reading-rest

Just starting off with Shopify, and trying to get an order. Following the Shopify API documentation, here is my code:

```
const Shopify = require('@shopify/shopify-api');

const client = new Shopify.Clients.Rest('my-store.myshopify.com', 
process.env.SHOPIFY_KEY);

module.exports.getShopifyOrderById = async (orderId) => {
return await client.get({ 
    path: `orders/${orderId}`,
  });
}
```

I get the following error when I execute this code:

`TypeError: Cannot read properties of undefined (reading 'Rest')`

Can't seem to figure out what the issue is.

---

## 63. How To Pass Data Between Shopify &quot;THEME-APP-EXTENSION&quot; And The Backend Of The App?
**Score:** 6 | **Tags:** shopify, shopify-app, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/73873170/how-to-pass-data-between-shopify-theme-app-extension-and-the-backend-of-the-ap

I am trying to figure out how to pass data between the theme-app-extension and the backend of the application that the theme-app-extension is connected to. The theme-app-extension is all liquid, css, and javascript so I wasn't sure if there was a built in way to pass data between the two. For example is there a suggested method to pull data into the theme-app-extension from the database and is there a suggested way to send data to the database from the code running the theme-app-extension? I am fairly new to doing anything with theme-app-extensions as well as building Shopify applications. I have built Shopify applications that was admin facing or just cosmetic, this is my first time building a Shopify application that takes user input and sends it to the database and retrieves that data for the end-user to see.

Any suggestions would be greatly appreciated.

Thank You.

---

## 64. How to get app subscription status from Shopify API
**Score:** 6 | **Tags:** graphql, shopify, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/67382310/how-to-get-app-subscription-status-from-shopify-api

Is there a way to determine the subcsription status of an app via the Shopify node client or in the GraphQL API?

Given a user has signed up to our public app, when they log in. then I should be able to check if their Shopify subscription to our app is still active.

I can see via the GraphQL API I can query

```
currentAppInstallation {
   activeSubscriptions {
     id
     name
     test
   }
}
```

This seems to return an empty array, implying my test store I doesn't have any active subscriptions. This may be due to my app and shop being in test mode though.

Does anybody know if this is the case or is there another way to get the subscription status?
Also, it would be good to do via the Shopify client if that is possible?

---

## 65. Digital Ocean Spaces TypeError [ERR_INVALID_URL]: Invalid URL
**Score:** 6 | **Tags:** express, serverless, shopify-app, digital-ocean-spaces, aws-s3-client | **Answered:** True
**Link:** https://stackoverflow.com/questions/73802420/digital-ocean-spaces-typeerror-err-invalid-url-invalid-url

I am creating a Shopify app in the express on the local and getting this error. The same code is working when I use this app on the server. I don't know why is this not working in the local environment.

I am using Digital Ocean Spaces, Node.js v17.0.1, @aws-sdk/client-s3 v3.171.0.

```
import { S3 } from "@aws-sdk/client-s3";
import dotenv from "dotenv";

dotenv.config();

const s3Client = new S3({
    endpoint: process.env.SPACES_ENDPOINT,
    region: process.env.SPACES_REGION,
    credentials: {
        accessKeyId: process.env.SPACES_KEY,
        secretAccessKey: process.env.SPACES_SECRET,
    },
});

export default s3Client;
```

I have already placed valid env variables in the .env file.

[Here is the error](https://i.sstatic.net/9ZIIT.jpg)

```
burhan@burhan:/shopifynode$ shopify app serve
✓ ngrok tunnel running at https://ebb6-2401-4900-1c02-5a90-982c-9e83-1b5e-b9ee.ngrok.io, with account testmail@mail.com
✓ .env saved to project root

⭑ To install and start using your app, open this URL in your browser:
https://ebb6-2401-4900-1c02-5a90-982c-9e83-1b5e-b9ee.ngrok.io/login?shop=my-app-staging.myshopify.com

Running server…

> dev
> cross-env NODE_ENV=development nodemon server/index.js --watch ./server

[nodemon] 2.0.15
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): server/**/*

[nodemon] watching extensions: js,mjs,json
[nodemon] starting `node server/index.js`
node:internal/errors:464
   ErrorCaptureStackTrace(err);
   ^

TypeError [ERR_INVALID_URL]: Invalid URL
   at new NodeError (node:internal/errors:371:5)
   at onParseError (node:internal/url:552:9)
   at new URL (node:internal/url:632:5)
   at parseUrl (/shopifynode/node_modules/@aws-sdk/url-parser/dist-cjs/index.js:7:38)
   at resolveEndpointsConfig (/shopifynode/node_modules/@aws-sdk/config-resolver/dist-cjs/endpointsConfig/resolveEndpointsConfig.js:14:87)
   at new S3Client (/shopifynode/node_modules/@aws-sdk/client-s3/dist-cjs/S3Client.js:22:72)
   at new S3 (/shopifynode/node_modules/@aws-sdk/client-s3/dist-cjs/S3.js:98:1)
   at file:///shopifynode/server/helpers/s3-client.js:6:18
   at ModuleJob.run (node:internal/modules/esm/module_job:185:25)
   at async Promise.all (index 0) {
 input: '"https://fra1.digitaloceanspaces.com"',
 code: 'ERR_INVALID_URL'
}

Node.js v17.0.1
[nodemon] app crashed - waiting for file changes before starting...
```

---

## 66. GraphQL::Client::DynamicQueryError Expected definition to be assigned to a static constant
**Score:** 6 | **Tags:** ruby-on-rails, ruby, graphql, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/50382830/graphqlclientdynamicqueryerror-expected-definition-to-be-assigned-to-a-stati

How to make proper **ShopifyAPI::GraphQL** method in Rails.

Trying the below code in `rails console` works fine.
But when I tried to put that code and make a method in Rails controller/model, i'm getting:

`GraphQL::Client::DynamicQueryError Expected definition to be assigned to a static constant`

```
shopify_client
client = ShopifyAPI::GraphQL.new

SHOP_NAME_QUERY = client.parse <<-'GRAPHQL'
 {
  shop {
   name
  }
 }
GRAPHQL

result = client.query(SHOP_NAME_QUERY)
```

I tried to play around with `variables`
following `https://github.com/github/graphql-client/blob/master/guides/dynamic-query-error.md` **but no success**.

How to make a method using the above function that will not return the mentioned error above.

**Sample Model method**:

```
def trial
  shopify_client
  client = ShopifyAPI::GraphQL.new
  shop_query = client.parse <<-'GRAPHQL'
    {
     shop {
      name
     }
    }
  GRAPHQL

  client.query(shop_query)
end
```

In **Gemfile**: `gem 'shopify_api', git: 'https://github.com/Shopify/shopify_api', branch: 'graphql-support'`

---

## 67. Pages are reloaded instead of routed in shopify next js app
**Score:** 6 | **Tags:** reactjs, next.js, shopify-app, next-router, shopify-app-bridge | **Answered:** True
**Link:** https://stackoverflow.com/questions/63463858/pages-are-reloaded-instead-of-routed-in-shopify-next-js-app

I followed [Shopify's guide](https://shopify.dev/tutorials/build-a-shopify-app-with-node-and-react), until the end of 4th step, to develop a Next JS app and I've setup two pages (embedded app navigation), Home and Page1.
Now, when I click to open both pages, the app is doing a reload instead of routing...

You can see here the flickering issue - <https://youtu.be/45RvYgxC7C0>

Any help on this would be very appreciated.

\_app.js

```
import React from "react";

import App from "next/app";
import Head from "next/head";

import { AppProvider } from "@shopify/polaris";
import { Provider } from "@shopify/app-bridge-react";
import Cookies from "js-cookie";

import "@shopify/polaris/dist/styles.css";
import "../css/styles.css";

import lang from "@shopify/polaris/locales/en.json";

export default class MyApp extends App {
    render() {
        const { Component, pageProps } = this.props;
        const config = { apiKey: API_KEY, shopOrigin: Cookies.get("shopOrigin"), forceRedirect: true };

        return (
            <React.Fragment>
                <Head>
                    <title>My App</title>

                    <meta charSet="utf-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />

                    <link rel="icon" href="favicon.ico" />
                </Head>

                <Provider config={config}>
                    <AppProvider i18n={lang}>
                        <Component {...pageProps} />
                    </AppProvider>
                </Provider>
            </React.Fragment>
        );
    }
}
```

home.js

```
import React from "react";

import { Page, Layout, Card, FooterHelp, Link } from "@shopify/polaris";

export default function Home() {
    return (
        <Page title="Home">
            <Layout>
                <Layout.Section>
                    <Card title="Online store dashboard" sectioned>
                        <p>View a summary of your online store’s performance.</p>
                    </Card>
                </Layout.Section>

                <Layout.Section>
                    <FooterHelp>
                        Learn more about{" "}
                        <Link url="#" external>
                            our app
                        </Link>
                    </FooterHelp>
                </Layout.Section>
            </Layout>
        </Page>
    );
}
```

Page1.js

```
import React from "react";

import { Page, Layout, Card, FooterHelp, Link } from "@shopify/polaris";

export default function Page1() {
    return (
        <Page title="Page1">
            <Layout>
                <Layout.Section>
                    <Card title="Online store dashboard" sectioned>
                        <p>View a summary of your online store’s performance.</p>
                    </Card>
                </Layout.Section>

                <Layout.Section>
                    <FooterHelp>
                        Learn more about{" "}
                        <Link url="#" external>
                            our app
                        </Link>
                    </FooterHelp>
                </Layout.Section>
            </Layout>
        </Page>
    );
}
```

---

## 68. AppBridgeError INVALID_CONFIG: host must be provided
**Score:** 6 | **Tags:** shopify-app, shopify-api-node | **Answered:** True
**Link:** https://stackoverflow.com/questions/67601949/appbridgeerror-invalid-config-host-must-be-provided

I am facing an error while trying to complete the official shopify [tutorial about developing shopify app](https://shopify.dev/tutorials/build-a-shopify-app-with-node-and-react/build-your-user-interface-with-polaris#add-shopify-app-bridge).

I have been following the tutorial step by step but even then ran in to problem where the error is thrown that my config file is invalid as it does not contain the host.

My \_app.js file code is as follow:

```
import React from "react";
import App from "next/app";
import Head from "next/head";
import { AppProvider, Frame } from "@shopify/polaris";
import "@shopify/polaris/dist/styles.css";
import translations from "@shopify/polaris/locales/en.json";
import { Provider } from "@shopify/app-bridge-react";
import ClientRouter from "../components/ClientRouter";

class MyApp extends App {
  render() {
    const { Component, pageProps, shopOrigin } = this.props;
    const config = {
      apiKey: API_KEY,
      shopOrigin,
      forceRedirect: true,
    };
    console.log(config);
    return (
      <React.Fragment>
        <Head>
          <title>Sample App</title>
          <meta charSet="utf-8" />
        </Head>
        <Provider config={config}>
          <ClientRouter />
          <AppProvider i18n={translations}>
            <Frame>
              <Component {...pageProps} />
            </Frame>
          </AppProvider>
        </Provider>
      </React.Fragment>
    );
  }
}
MyApp.getInitialProps = async ({ ctx }) => {
  return {
    shopOrigin: ctx.query.shop,
  };
};
export default MyApp;
```

the console for the config file gives the right shopOrigin.
Ill be thankful if anyone helps

---

## 69. How to access Shopify app owned metafields in theme extension liquid files?
**Score:** 6 | **Tags:** shopify, liquid, shopify-app, shopify-template | **Answered:** True
**Link:** https://stackoverflow.com/questions/72952580/how-to-access-shopify-app-owned-metafields-in-theme-extension-liquid-files

I am having trouble finding the liquid app object. Shopify mentions about this object here <https://shopify.dev/changelog/new-app-liquid-object> but when we click the link within it(<https://shopify.dev/api/liquid/objects#app>) to go to the object nothing appears. I am trying to access App-owned metafields in the theme app extension liquid file. Even if I mention app object in the liquid file it throws an error(Undefined object "app"). Can somebody please let me know how I can access App owned metafields in Theme Extension?

---

## 70. Where do I get the value for `shopOrigin` when using Shopify app bridge?
**Score:** 6 | **Tags:** shopify-app, shopify-app-bridge | **Answered:** False
**Link:** https://stackoverflow.com/questions/58370380/where-do-i-get-the-value-for-shoporigin-when-using-shopify-app-bridge

Throughout the documentation for the new App Bridge, Shopify refers to the `shopOrigin` value and how it's used to configure the Provider from `app-bridge-react` but they never specify how to get this value?

[![enter image description here](https://i.sstatic.net/M5VX5.png)](https://i.sstatic.net/M5VX5.png)

The react app is loaded inside of an iframe and the src includes the `shopOrigin` value as a query string param called `shop`, but when I try the following code I get the error `window is not defined`:

```
const params = queryString.parse(window.location.search);
const config = {
  apiKey: process.env.SHOPIFY_API_KEY,
  shopOrigin: params.shop,
};
```

1) Why would I be getting `window is not defined` in javascript code running in a browser?! This makes no sense to me
2) If this value can be read from of the provided libraries such as `@shopufy/app-bridge-react` please tell me how

---

## 71. @shopify/shopify-api jws dependence is not working
**Score:** 5 | **Tags:** shopify, shopify-app, shopify-api, shopify-api-node | **Answered:** False
**Link:** https://stackoverflow.com/questions/72118603/shopify-shopify-api-jws-dependence-is-not-working

I'm new in Shopify, I'm having a problem when I try to use the @shopify/shopify-api.
I'm importing this property from the API.

```
import Shopify from '@shopify/shopify-api'
```

When I do the import I get the next error.

```
Uncaught TypeError: util.inherits is not a function
at node_modules/jsonwebtoken/node_modules/jws/lib/data-stream.js (data-stream.js:39:6)
at __require (chunk-IGMYUX52.js?v=cd28f3b3:40:50)
at node_modules/jsonwebtoken/node_modules/jws/lib/sign-stream.js (sign-stream.js:3:18)
at __require (chunk-IGMYUX52.js?v=cd28f3b3:40:50)
at node_modules/jsonwebtoken/node_modules/jws/index.js (index.js:2:18)
at __require (chunk-IGMYUX52.js?v=cd28f3b3:40:50)
at node_modules/jsonwebtoken/decode.js (decode.js:1:11)
at __require (chunk-IGMYUX52.js?v=cd28f3b3:40:50)
at node_modules/jsonwebtoken/index.js (index.js:2:11)
at __require (chunk-IGMYUX52.js?v=cd28f3b3:40:50)
```

So I went to the line in the file where is happening the error:

```
node_modules/jsonwebtoken/node_modules/jws/lib/data-stream.js
```

[And I discovered that error is a property in a node package](https://i.sstatic.net/73Wp8.png)

if you can't see the image here the code line.

```
util.inherits(DataStream, Stream);
```

[So I went to the node documentation](https://i.sstatic.net/ovFlc.png) and I found that method is discouraged, but is not deprecated, therefore it should be working.

here is the description of the method if you can't see the image.

> Usage of `util.inherits()` is discouraged. Please use the ES6 class and extends keywords to get language level inheritance support. Also
> note that the two styles are semantically incompatible.
>
> Inherit the prototype methods from one constructor into another. The prototype of constructor will be set to a new object created from
> `superConstructor`.
>
> This mainly adds some input validation on top of `Object.setPrototypeOf(constructor.prototype, superConstructor.prototype)`. As an additional convenience,
> `superConstructor` will be accessible through the `constructor.super_`
> property.

The package in question is named jws, I'm not so sure the purpose of this package, I had the idea to modify the file and use prototypical inheritance replacing that code line but I don't know how good an idea it is do that. furthermore I would have to do that for each file that has that problem, i haven't found any information about this on the intenet.

---

## 72. Consuming RESTful pagination information from Link header RFC8288
**Score:** 5 | **Tags:** java, c#, pagination, restful-url, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/62382062/consuming-restful-pagination-information-from-link-header-rfc8288

I am interfacing with Shopify and they use RESTful API. When I request a resource that returns an array of items, they use RFC8288 pagination format.

For example, <https://example.com/api/inventory_levels.json?limit=10> returns 10 entities along with the following response header:

```
Link: <https://example.com/api/inventory_levels.json?limit=10&page_info=eyJs9pZHMiO>; 
rel="previous", <https://example.com/api/inventory_levels.json?limit=10&page_info=MiZHeyJs9pO>; rel="next"
```

Appearantly if I want to retrieve all entites from that resource I need to iterate through the 'next' URL until there's no more 'next' returning. But how am I going to parse these info using JAVA or C# code? I could use a regular expression like `<(?<next_url>.*)>; rel="next"` to retrieve the 'next\_url' from it. But it feels like re-inventing the wheel and not robust.

If this is a well-defined feature, shouldn't there be a readily available library/infrastructure that could be used? I just don't want to be caught by surprise if one day the formatting shows up different (like having an extra space and such) and, whilst abiding to the RFC defination, breaks my hastily scrambled up RegEx solution.

Suggestion welcome for Java or C#.

---

## 73. &quot;There’s no page at this address&quot; error on Shopify Embedded App installation
**Score:** 5 | **Tags:** laravel, shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/65611022/there-s-no-page-at-this-address-error-on-shopify-embedded-app-installation

I am facing a strange issue, When I install app first time on test store, installation goes smooth but after re-installation after OAuth, Shopify show me "*There’s no page at this address*" error.

My app submission was rejected due to this reason. I am using <https://github.com/osiset/laravel-shopify> library.

[![This is image of error.](https://i.sstatic.net/yleYe.png)](https://i.sstatic.net/yleYe.png)

---

## 74. Is there an AliExpress API that can submit dropship orders instead of using Oberlo?
**Score:** 5 | **Tags:** shopify, shopify-app, aliexpress | **Answered:** True
**Link:** https://stackoverflow.com/questions/46121345/is-there-an-aliexpress-api-that-can-submit-dropship-orders-instead-of-using-ober

Currently I am using the Shopify app Oberlo with it's chrome extension to manually send over dropship orders one by one.

This works find but I have between 100 to 1000 orders daily during testing.

Can anybody recommend a way to automate this using either an API directly from AliExpress (which the affiliate API is all I have been able to find) or possibly a laravel wrapper integrated with Shopify that has the ability to post dropship orders automatically.

Much appreciated!

---

## 75. Building Shopify Ap with React and Node issue
**Score:** 5 | **Tags:** javascript, node.js, shopify, shopify-app, shopify-api-node | **Answered:** True
**Link:** https://stackoverflow.com/questions/66523481/building-shopify-ap-with-react-and-node-issue

i am following along with the Shopify app dev how-to provided by shopify but keep getting an error with my localhost saying - external server error, the cause in terminal says 'Context has not been properly initialized. Please call the .initialize() method to setup your app context object.' but not sure how to do this in my server.js file below;

```
require('isomorphic-fetch');
const dotenv = require('dotenv');
const Koa = require('koa');
const next = require('next');
const { default: createShopifyAuth } = require('@shopify/koa-shopify-auth');
const { verifyRequest } = require('@shopify/koa-shopify-auth');
const session = require('koa-session');

dotenv.config();

const port = parseInt(process.env.PORT, 10) || 3000;
const dev = process.env.NODE_ENV !== 'production';
const app = next({ dev });
const handle = app.getRequestHandler();

const { SHOPIFY_API_SECRET_KEY, SHOPIFY_API_KEY } = process.env;

app.prepare().then(() => {
  const server = new Koa();
  server.use(session({ secure: true, sameSite: 'none' }, server));
  server.keys = [SHOPIFY_API_SECRET_KEY];

  server.use(
    createShopifyAuth({
      apiKey: SHOPIFY_API_KEY,
      secret: SHOPIFY_API_SECRET_KEY,
      scopes: [
        'read_products',
        'write_products',
        'read_script_tags',
        'write_script_tags'
      ],
      afterAuth(ctx){
        const { shop, accessToken } = ctx.session;

        ctx.redirect('/');
      },
    }),
  );

  server.use(verifyRequest());
  server.use(async (ctx) => {
    await handle(ctx.req, ctx.res);
    ctx.respond = false;
    ctx.res.statusCode = 200;
    return
  });

  server.listen(port, () => {
    console.log(`> Ready on http://localhost:${port}`);
  });
});
```

---

## 76. App dev - Storing Shopify data in local DB
**Score:** 5 | **Tags:** shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/11715131/app-dev-storing-shopify-data-in-local-db

Is it normal for Shopify apps to store some or all data they need for their app in their local database and only fetch data via the Shopify API when the client logs in to update the data?

I know this has a lot of scenarios possible depending on the type of app.

Is anyone willing to share their experience and pros/cons of storing data locally vs accessing it via Shopify at all times?

---

## 77. Shopify - Get shop domain inside a app
**Score:** 5 | **Tags:** shopify, shopify-app, polaris | **Answered:** True
**Link:** https://stackoverflow.com/questions/47432209/shopify-get-shop-domain-inside-a-app

I'm new to Shopify app developing and I'm using Node,Express for the back-end and react with polaris libaray.

My question is how to get the shop's domain the request is initiating throug h the app. When I searched I could only found one used in Ruby `ShopifyAPI::Shop.current` and I'm looking for the similar thing to use in node?

---

## 78. Calling shopify API from Postman
**Score:** 5 | **Tags:** php, shopify, webhooks, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/53153019/calling-shopify-api-from-postman

I need to create a webhook in shopify using Postman.
I have entered following:

**Method**: POST

**URL**: `https://{{api_key}}:{{api_password}}@{{store_name}}.myshopify.com/admin/webhooks.json`

**Parameters**:

```
{
    "topic": "order/creation",
    "address": "https://example.com/shopify_app/order_created.php"
}
```

**Headers**:
`[{"key":"Content-Type","value":"application/json","description":""}]`

I have replaced `{{api_key}}` with API key created while creating the app, and `{{api_password}}` with the access\_token.

When I hit this, I get "Please log in" screen. Please check below image:

[![enter image description here](https://i.sstatic.net/GwfYt.png)](https://i.sstatic.net/GwfYt.png)

---

## 79. Shopify GraphQL Admin API rate limiting cost and sleep time
**Score:** 5 | **Tags:** php, laravel, graphql, shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/53469612/shopify-graphql-admin-api-rate-limiting-cost-and-sleep-time

I am trying to consume Shopify GraphQL API for Admin in PHP ( Laravel ).  
Rate limiting and throttling works differently in GraphQL api as compared to REST api, its calculated based on the **cost** of the query.  
  
[![Cost of Shopify GraphQL query](https://i.sstatic.net/7ERr1.png)](https://i.sstatic.net/7ERr1.png)

Few points to keep in mind:

* Maximum available cost is 1000 for one api call (query).
* If you have consumed some points from 1000, every second, 50 points will be restored.
* If you have less points of cost in your bucket, and you make a query of cost higher than that, it will throttle.

The query that I am passing to api has an estimated cost of **502**, represented by **requestedQueryCost**. Whereas, **actualQueryCost** represents the actual **response** returned by the api for a specific shop.   
  
In above snapshot, its the worst case scenario, **requestedQueryCost** is equal to **acutalQueryCost** for a store with heavy number of orders.  
  
Now, when this query is executed I have consumed 502 points, 498 left, 1 second elapsed, 50 points added = **548** , and I can make a second api call to fetch second page of data. After second api call I will have less points left, so I will have to put **sleep** for 1 or 2 seconds to gain the points to make api call.   
  
In the case shown in snapshot, i had to put **10 seconds** sleep wait in order to restore **500 points** to make next api call.  
  
**Problem:** How to best decide sleep (wait) time for different shops? We don't want all shops to wait for 10 seconds even if they have less query cost.  
  
**Note:** For code reference, see my answer below.

---

## 80. Call Shopify API from React
**Score:** 5 | **Tags:** ruby-on-rails, ruby, shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/48254945/call-shopify-api-from-react

# What I managed to do so far

I followed this guide to setup a Shopify app with a Rails backend + React:
<https://medium.com/@esimonian16/setting-up-a-shopify-app-with-rails-5-1-webpack-react-and-polaris-b8535d911275>

Everything seems to work fine. I'm using the shopify\_app gem.

When I navigate to my app in the merchant dashboard, The home controller in Rails renders a React app that displays some products (these were passed from rails to react as JSON).

---

# What I would like to do now

I want to have a button in React 'List customers', which should then update the react components and show all the customers as a list.

I have created a new controller at `my-app.com/customers`

```
class CustomersController < ShopifyApp::AuthenticatedController
    def index
        customers = ShopifyAPI::Customer.find(:all, params: { limit: 10 })
        render json: customers
    end
end
```

If I go to `my-app.com/customers` in the browser I get the correct json response.

---

I then tried fetching this data from React.

```
fetch('https://my-app.com/customers', {
      headers : { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }
})
.then(response => response.json())
.then(parsedJSON => {
  console.log(parsedJSON);

  // Update state
  // this.setState(...);
})
.catch(error => console.error(error));
```

The Rails backend doesn't allow the request to get this data, because it is not authorized, so it get's redirected to `/login`

In React, I have access to the `session.token`, however I'm not sure how to use it to authenticate my request?

# Questions

1. How do I make such calls to the Shopify API? Am I trying the right approach, i.e use my backend between React and the actual Shopify Api call?
2. How do I authenticate my call so that they pass just as if I'm calling `/customers` in the browser?
3. I guess making Shopify Api calls directly from React would be a really bad idea, because I would expose my secrets to the world, right?
4. What am I doing wrong? What is the correct approach?

---

## 81. Failed to find a valid digest in the &#39;integrity&#39; attribute for resource with computed SHA-256 integrity
**Score:** 5 | **Tags:** heroku, shopify, shopify-app | **Answered:** False
**Link:** https://stackoverflow.com/questions/59403785/failed-to-find-a-valid-digest-in-the-integrity-attribute-for-resource-with-com

I am developing Shopify App, with help of Heroku server.
After hitting the URL `https://warm-tundra-19548.herokuapp.com`.
It is redirecting to login page i.e "<https://prnt.sc/qcvkdc>"
After adding domain i.e `https://daisylilly.myshopify.com`.

Then blank screen come with message in

> Failed to find a valid digest in the 'integrity' attribute for
> resource
> '<https://warm-tundra-19548.herokuapp.com/assets/shopify_app/request_storage_access-5a556c57b51c57f00d9d6a2ba007f3172739bab34cc2f647a93e792348e8798d.js>'
> with computed SHA-256 integrity
> '0lJjndtl8qUdAHc8U0DNkSIqNg4Nx2/QjfsZIycjNoU

Can you please help me with resolving this issue.

---

## 82. Oauth error invalid_request: Could not find Shopify API application with api_key Shopify error
**Score:** 5 | **Tags:** shopify, shopify-app | **Answered:** False
**Link:** https://stackoverflow.com/questions/50227826/oauth-error-invalid-request-could-not-find-shopify-api-application-with-api-key

I am receiving this error immediately after installing my app in my dev store when attempting to exchange the temporary access code for a permanent token.

Oauth error invalid\_request: Could not find Shopify API application with api\_key

I'm using below code

```
$client = new Client();
$response = $client->request(
'POST', 
"https://{$store}/admin/oauth/access_token",
[
'form_params' => [
    'client_id' => $api_key,
    'client_secret' => $secret_key,
    'code' => $query['code']
]
]
);
$data = json_decode($response->getBody()->getContents(), true);
$access_token = $data['access_token'];
```

Any help is much appreciated. Thanks!

---

## 83. Cart toast notification - Shopify Hydrogen
**Score:** 5 | **Tags:** javascript, reactjs, shopify, shopify-hydrogen | **Answered:** True
**Link:** https://stackoverflow.com/questions/74828402/cart-toast-notification-shopify-hydrogen

I managed to create onLineAdd toast notification whenever a person adds something to their cart, however, I can't seem to grasp how to show product information and show it in the toast.

What I'm looking for is onLineAdd to trigger a notification that says: "XXX (with picture) have been added to the cart." Is this possible?

My code:

```
const open = useCallback(() => {
    console.log("Opening product added popup, with image and title.")
}, []);

<ShopifyCartProvider
    onLineAdd={open}
    onCreate={open}>
    {children}
</ShopifyCartProvider>
```

It's even implemented on the official shopify hydrogen store: (Try adding something to the cart here)
<https://shopify.supply/products/entrepreneur-tee>

---

## 84. How to get/generate access token of storefront API
**Score:** 4 | **Tags:** shopify, laravel-8, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/66744989/how-to-get-generate-access-token-of-storefront-api

I am using <https://github.com/osiset/laravel-shopify> package to manage Shopify API with laravel 8 and facing the following error:

HTTP/1.1 403 Forbidden
{
"errors": "App must be extendable to create a storefront access token."
}

Trying the following:

```
$shop = Auth::user();
$orders = $shop->api()->rest('POST', '/admin/api/2021-01/storefront_access_tokens.json', ['storefront_access_token' => ['title' => 'mobile']]);
dd($orders);
```

---

## 85. How to get basic Shopify GraphQL Admin API working with nodeJS?
**Score:** 4 | **Tags:** node.js, graphql, shopify, node-fetch, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/66514765/how-to-get-basic-shopify-graphql-admin-api-working-with-nodejs

I had a very frustrating evening yesterday, trying to get the basic Shopify GraphQL Admin API example working with nodeJS. The original Shopify example code is [here](https://shopify.dev/tutorials/graphql-with-node-and-express).

The problem is that my code returns a status 400 - Bad Request.

I have enabled a "private App" on my store and enabled all the APIs with read access. I carefully copied the apiKey, accessToken and store name from Shopify.

Can anyone point out if there is something wrong with my code? Many thanks.

Code:

```
import fetch from 'node-fetch';

const apiKey = 'xxxx';
const accessToken = 'yyyy';
const store = 'zzzz';
const hostName = store + '.myshopify.com';
const apiVersion = '2021-01';
const apiLocation = '/admin/api/';

const rootUrl = 'https://' + apiKey + ':' + accessToken + '@' + hostName + apiLocation + apiVersion + '/';

const shopGraphQl = 'https://' + hostName + apiLocation + apiVersion + '/graphql.json';
//const shopGraphQl2 = rootUrl + 'graphql.json';
//const urlTest = rootUrl + 'orders.json';

const url = shopGraphQl;

const body = {
    query: `{
        shop {
            name
          }
      }`
};

fetch   (
    url,
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token" : accessToken
        },
        body: JSON.stringify({
            body
        })
    }
)
.then(res => {
    console.log('status = ' + res.status + ' , ' + res.statusText);
})
.then(json => {
    console.log("data returned:\n", json);
})
.catch(err => console.error(err));;
```

---

## 86. PUT request to google cloud storage signed URL generated by Shopify throws error MalformedSecurityHeader
**Score:** 4 | **Tags:** file-upload, google-cloud-storage, shopify, pre-signed-url, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/62995003/put-request-to-google-cloud-storage-signed-url-generated-by-shopify-throws-error

I'm trying to upload a .glb file to a product in a Shopify store through Shopify GraphQL Admin API. For that, it first returns a google cloud storage signed URL, to where I should upload my file through an HTTP PUT request. After uploading, I should attach the same URL to the product with another API call.

This question is about that file uploading to the cloud storage signed URL. I include all these details to make this question easy to be getting answered. **So, please read till the end**.

1. What data Shopify provides me with is mentioned below.

```
{
  "data": {
    "stagedUploadsCreate": {
      "stagedTargets": [
        {
          "parameters": [
            {
              "name": "GoogleAccessId",
              "value": "threed-model-service--6bgx7cbe@shopify-applications.iam.gserviceaccount.com"
            },
            {
              "name": "key",
              "value": "models/a6436c066064bac3/windmill.glb"
            },
            {
              "name": "policy",
              "value": "eyJleHBpcmF0aW9uIjoiMjAyMC0wNy0yMVQwOToxNjoxMFoiLCJjb25kaXRpb25zIjpbWyJlcSIsIiRidWNrZXQiLCJ0aHJlZWQtbW9kZWxzLXByb2R1Y3Rpb24iXSxbImVxIiwiJGtleSIsIm1vZGVscy9hNjQzNmMwNjYwNjRiYWMzL3dpbmRtaWxsLmdsYiJdLFsiY29udGVudC1sZW5ndGgtcmFuZ2UiLDE5NzE3MiwxOTcxNzJdXX0="
            },
            {
              "name": "signature",
              "value": "vz+OdcEmD9Kbv2FbXdxWNUk59XO2GmXzhvtDswXbDQNcyZpUufI85z5x2PFGv/XZ+tSBsl/S393pmy0Bu9xG7oVgOZcMIWEbOIm9kXgQunbjKQY3Ff3BBpMocB0xazzlYmckZozdJ8ZZkyox/c/gEe1QaxqW4+419iufuFHy4Bp3LL/aUr+ATNChwn9Dn8+XnHMOckZxDlbiggcF3dx+yBuTFia8FneaVSiU0M5DIWmHqHb2YDCV0KtEP6jfTj/PQVUjS8pn8EGhrRaMx7Q2A5G8Pycgc9H35hqJnnUKCTa3AYeyI45RbhddYnIWw9YrAADXuQYlVCo6LYBHjxsCWA=="
            }
          ],
          "resourceUrl": "https://storage.googleapis.com/threed-models-production/models/a6436c066064bac3/windmill.glb?external_model3d_id=bW9kZWwzZC00MDg5Ng==",
          "url": "https://storage.googleapis.com/threed-models-production/models/a6436c066064bac3/windmill.glb?external_model3d_id=bW9kZWwzZC00MDg5Ng=="
        }
      ],
      "userErrors": []
    }
  }
}
```

2. Using these parameters, I construct a signed URL as follows.

```
resourceUrl+"&signature="+signature+"&key="+key+"&policy="+policy+"&GoogleAccessId="+GoogleAccessId
```

Eg:

<https://storage.googleapis.com/threed-models-production/models/a6436c066064bac3/windmill.glb?external_model3d_id=bW9kZWwzZC00MDg5Ng==&signature=vz+OdcEmD9Kbv2FbXdxWNUk59XO2GmXzhvtDswXbDQNcyZpUufI85z5x2PFGv/XZ+tSBsl/S393pmy0Bu9xG7oVgOZcMIWEbOIm9kXgQunbjKQY3Ff3BBpMocB0xazzlYmckZozdJ8ZZkyox/c/gEe1QaxqW4+419iufuFHy4Bp3LL/aUr+ATNChwn9Dn8+XnHMOckZxDlbiggcF3dx+yBuTFia8FneaVSiU0M5DIWmHqHb2YDCV0KtEP6jfTj/PQVUjS8pn8EGhrRaMx7Q2A5G8Pycgc9H35hqJnnUKCTa3AYeyI45RbhddYnIWw9YrAADXuQYlVCo6LYBHjxsCWA==&key=models/a6436c066064bac3/windmill.glb&policy=eyJleHBpcmF0aW9uIjoiMjAyMC0wNy0yMVQwOToxNjoxMFoiLCJjb25kaXRpb25zIjpbWyJlcSIsIiRidWNrZXQiLCJ0aHJlZWQtbW9kZWxzLXByb2R1Y3Rpb24iXSxbImVxIiwiJGtleSIsIm1vZGVscy9hNjQzNmMwNjYwNjRiYWMzL3dpbmRtaWxsLmdsYiJdLFsiY29udGVudC1sZW5ndGgtcmFuZ2UiLDE5NzE3MiwxOTcxNzJdXX0=&GoogleAccessId=threed-model-service--6bgx7cbe@shopify-applications.iam.gserviceaccount.com>

3. Then I try to make a PUT request to this URL with the .glb file in POSTman as shown in this image -->
   [![enter image description here](https://i.sstatic.net/pRZW9.png)](https://i.sstatic.net/pRZW9.png)

with the following headers.

[![enter image description here](https://i.sstatic.net/mMP1u.png)](https://i.sstatic.net/mMP1u.png)

4. But I don't get a success response. In fact, I get a 400 error with the following message.

```
<?xml version='1.0' encoding='UTF-8'?>
<Error>
    <Code>MalformedSecurityHeader</Code>
    <Message>Your request has a malformed header.</Message>
    <ParameterName>signature</ParameterName>
    <Details>Signature was not base64 encoded</Details>
</Error>
```

Can someone point me out what I'm doing wrong here? I have been dealing with this error for days and read a lot of questions and articles, but couldn't get this to work. Therefore, any helpful suggestion is highly appreciated.

---

## 87. Shopify Cannot complete OAuth process. Could not find an OAuth cookie for shop url
**Score:** 4 | **Tags:** node.js, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/73702190/shopify-cannot-complete-oauth-process-could-not-find-an-oauth-cookie-for-shop-u

I am trying to Complete OAuth process for Shopify and getting above mentioned error.

What it does?
A log in page appears, after my credentials it redirects to my URL which I also registered in App URLs in Shopify Partners.

I am following documentation from Official Shopify Api <https://github.com/Shopify/shopify-api-node>

```
const session = yield shopify_api_1.default.Auth.validateAuthCallback(request, response, query);
```

this is where the problem is, if I get session, I can move on

looking forward for answers.

---

## 88. Checkout Headless Approach with Shopify?
**Score:** 4 | **Tags:** shopify, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/73097777/checkout-headless-approach-with-shopify

Looking for a way to have a full checkout process with the Shopify Graphql API.
But the concept don't allow it? The final step is then always a redirect to the web checkout page from Shopify.

There are two ways so far I understood.

* via cart graphql api
* via checkout graphql API

**via Cart**

1. create Cart

```
mutation cartCreate {
  cartCreate {
    cart {
      # Cart fields
    }
    userErrors {
      field
      message
    }
  }
}
```

2. get checkout url and redirect user

```
query checkoutURL($cartId: ID!) {
  cart(id: $cartId) {
    checkoutUrl
  }
}
```

checkoutUrl -> webcheckout page

**via Checkout API**

1. create full checkout

```
mutation {
  checkoutCreate(input: {
    lineItems: [{ variantId: "Z2lkOi8vc2hvcGlmeS9Qcm9kdWN0VmFyaWFudC8xMzg3MDQ4MzI3NTc5OA==", quantity: 1 }]
  }) {
    checkout {
       id
       webUrl
       lineItems(first: 5) {
         edges {
           node {
             title
             quantity
           }
         }
       }
    }
  }
}
```

2. redirect user again...
   <https://shopify.dev/api/examples/checkout#complete-the-checkout>

Extract documentation from shopify.dev.

```
    Use the webUrl field to redirect the customer to Shopify's web checkout form.

    Complete the checkout using one of the following methods:
        Shopify card vault
        Stripe
        Spreedly
```

webUrl -> webcheckout page

These are no real headless approaches.

1. Exists there any way to do real full cart -> checkout process without redirect to the shopify page?
2. Is there a way to transform cart to checkout? Don't understand for what it is then finally the checkout api needed, if I can't do a checkout via the api for the user.

---

## 89. How to make API request in a Shopify private APP
**Score:** 4 | **Tags:** javascript, node.js, shopify-app, shopify-api, shopify-api-node | **Answered:** True
**Link:** https://stackoverflow.com/questions/68236633/how-to-make-api-request-in-a-shopify-private-app

So I'm developing a private app in Shopify using node.js and react, so far it's just a form that submits new products to the store, pretty simple, the thing that I have realized is that the Admin API from Shopify won't let me make request as a private app, or so thats what I understand from it, apparently the solution has to do with setting up a back-end server, which I'm at a loss because I quickstarted the app with the Shopify CLI and sets up a ngrok tunnel server for you, I'm unsure if I would need to set up another one or what to do next.
its scaffolded with this process: <https://shopify.dev/apps/getting-started/create>

This article describes the perfect solution but they don't go into details about it so that's why I'm comming here:<https://metafieldsmanager.thebestagency.com/articles/how-to-build-a-private-app>

Code:

```
AddProductForm.js

let headers = {'X-Shopify-Access-Token': 'access token',
'host': 'store-example.myshopify.com', 
'Content-Type': 'application/json',
'Access-Control-Allow-Origin': '*'
}

let baseUrl = 'https://store-example.myshopify.com/admin/api/2021-07/'
```

Right now I'm just attempting a simple fetch request.

```
let handleSubmit = () => {  
        let toAdd = {
            product:{
                title: title,
                body_html: bodyHtml,
                vendor: vendor,
            }

        }
        console.log(baseUrl + 'products.json')
        fetch(baseUrl + 'products.json', {  
            headers:  headers
        }).then(res=>console.log(res))
```

I've omitted the rest of the code to keep it simple but its pretty much basic JSX and form handling.

---

## 90. Embed a whole shopify store inside a iframe
**Score:** 4 | **Tags:** shopify, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/66415089/embed-a-whole-shopify-store-inside-a-iframe

I would ideally like to embed a whole shopify store inside an iframe to allow the full browsing/purchasing/checkout process inside another website (and mobile app, using a webview).

I know there are various JavaScript integration options but they all seem to require basically building the store yourself.

"Buy" buttons won't cut it because the user needs to be able to create a cart and easily add multiple products then checkout.

I note that shopify website disables embedding in iframe using `content-security-policy: frame-ancestors 'none';`

Is there some way to just embed the whole store inside my WebApp, using iframe or some other approach?

---

## 91. Shopify App Billing API: How to offer multiple billing plans?
**Score:** 4 | **Tags:** shopify, billing, shopify-app, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/62836137/shopify-app-billing-api-how-to-offer-multiple-billing-plans

Shopify's recent July 2020 API update allows billing annually for apps, so I've been trying to add the option to choose between monthly and annual billing to my app.

I've been trying to do this by modifying the GraphQL call that creates the billing plan.

I've been trying several different options, but the most logical one seems to be to add an additional line item. This works in rendering both plans to the billing approval screen, but it is still not possible to actually choose between plans (details for both plans are displayed, but only the latter option is actually effective.

Here's the code I've been working with:

```
  const query = JSON.stringify({
    query: `mutation {
      appSubscriptionCreate(
          name: "Basic Plan"
          trialDays: 7
          returnUrl: "${process.env.HOST}"
          lineItems: [
          {
            plan: {
              appRecurringPricingDetails: {
                  price: { amount: 4.99, currencyCode: USD }
              }
            }
            plan: {
              appRecurringPricingDetails: {
                  price: { amount: 49.99, currencyCode: USD }
                  interval: ANNUAL
              }
            }
          }
          ]
        ) {
            userErrors {
              field
              message
            }
            confirmationUrl
            appSubscription {
              id
            }
        }
    }`
  });
```

I'd be happy about any suggestions.

Thanks a lot!

---

## 92. How to parsing string of shopify pagination link according new pagination update?
**Score:** 4 | **Tags:** php, shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/57972234/how-to-parsing-string-of-shopify-pagination-link-according-new-pagination-update

I Have one string which contains the link of prev and next page link:

```
Link: "<https://{shop}.myshopify.com/admin/api/{version}/products.json?page_info={next_page_info}&limit={limit}>; rel={next}, <https://{shop}.myshopify.com/admin/api/{version}/products.json?page_info={prev_page_info}&limit={limit}>; rel={previous}"
```

expecting output

```
array(
    'next' => {next_page_info},
    'prev' => {prev_page_info}
);
```

link string has also some condition as below:

1. string has both next and prev link
2. string has only next link Output should be array('next' => '{next\_page\_info}' );
3. string has only prev link Output should be array('prev' => '{prev\_page\_info}');

---

## 93. Error In API cURL Call: {&quot;errors&quot;:{&quot;price_rule&quot;:&quot;Required parameter missing or invalid&quot;}}
**Score:** 4 | **Tags:** php, laravel, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/54822774/error-in-api-curl-call-errorsprice-rulerequired-parameter-missing-or-i

I am getting an error in cURL call for Price rule based on selected products.
Following is my error:

```
{
   "errors":{
      "price_rule":"Required parameter missing or invalid"
   }
}
```

Following is my body parameters which I am sending in cURL call:

```
{
   "price_rule":{
      "title":"sss",
      "target_type":"line_item",
      "target_selection":"entitled",
      "allocation_method":"across",
      "value_type":"fixed_amount",
      "value":"-434",
      "customer_selection":"all",
      "prerequisite_quantity_range":{
         "greater_than_or_equal_to":"2"
      },
      "entitled_product_ids":{
         "0":"2397130326093",
         "1":"2397129965645",
         "2":"2397131898957",
         "3":"2397132324941"
      },
      "starts_at":"2019-02-22T08:08:53.000Z"
   }
}
```

Following is my cURL call:

```
$ch = curl_init();    
// curl_setopt($ch, CURLOPT_POST, count($newrule));
curl_setopt($ch, CURLOPT_URL, $access_token_url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($pro_ids11));
curl_setopt($ch, CURLOPT_HTTPHEADER, array('X-Shopify-Access-Token: '.$shops_token));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$result = curl_exec($ch);
if (curl_error($ch)) {
    $error_msg = curl_error($ch);
}
curl_close($ch);
if (isset($error_msg)) {
    echo $error_msg;
}
```

Please note that I am working in PHP.
Thanks in Advance!

---

## 94. Is there any way to programmatically authenticate customers in Shopify?
**Score:** 4 | **Tags:** firebase, firebase-authentication, shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/46182944/is-there-any-way-to-programmatically-authenticate-customers-in-shopify

We have a custom app hosted in Firebase (Google's Backend as a service). We would like to use Shopify's authentication so the user doesn't have to create an account in the app as well as the Shopify store (where we require accounts).

**The key:** I need to have some mechanism (like an API) that I can use to have Shopify authenticate a user. (Assume the customer has already created an account in the Shopify store. Account creation will be handled by the normal Shopify process.)

I can create a page in my app to ask for email / pass. Is there some way to send this info (perhaps along with some sort of token generated from a private app) to authenticate the customer? I just need Shopify to confirm whether the email / pass is correct, so I can then 'login' the user into my Firebase app.

Any direction / thoughts / suggestions are greatly appreciated.

PS. Firebase offers a 'custom authentication' option, along with email, Google+, Facebook. The custom auth option requires sending user / pass to the authentication server, which in this case, would be Shopify.

**EDIT:** Based on the responses, edited to clarify that *I need some way to authenticate the user in Shopify*. Handling the custom auth into Firebase seems like a fairly straightforward task, once I receive some sort of signal from Shopify telling me the users email / pass is valid.

---

## 95. Expected a valid shop query parameter
**Score:** 4 | **Tags:** shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/56869517/expected-a-valid-shop-query-parameter

I'm trying to create new Shopify app using shopify-app-cli, I set up all redirect links and .env file, but when I run Shopify serve and when it says Ready on <http://localhost:8081>, I go to localhost page and it shows this error: Expected a valid shop query parameter.
What does it mean?

I checked my .env file for maybe typos, but everything is copied fine.

---

## 96. Shopify Customized Search using external services
**Score:** 4 | **Tags:** javascript, ruby-on-rails, shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/45927777/shopify-customized-search-using-external-services

My situation: we have a Shopify store, we also have a search engine implemented and hosted on AWS. We need to use that search engine instead of the default /search on our Shopify store.

Ideally, when users try to search something, their query (and potentially some other stuff like attribute selectors/checkboxes on the front end) will be passed to our search engine. Then after the result is back, they will be rendered at the front end.

My Question: how should I do this?

Option 1: modify the theme code, inject some javascript to call the search engine
(Possible, but messy)

Option 2: write an app, wrap my search engine within the app, and somehow plug it in the store
(I don't know how to do this)

Option 3: similar to Option 1, but write an app, use the app to inject some code to the theme, and somehow handle the work.
(I don't know how to do this either)

I found a similar post here: [Write custom search app in shopify](https://stackoverflow.com/questions/44751259/write-custom-search-app-in-shopify)
but the answers below were more about filtering/modifying search result returned by the default shopify engine, I want to instead use my own search engine.

---

## 97. How to bundle product in shopify?
**Score:** 4 | **Tags:** shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/52578444/how-to-bundle-product-in-shopify

I tried to develop a Shopify application and I needed to bundle some products and sell those together with the special discount values.

There are some apps like product-bundle but I need bundling product in my app.

I tried to create one product similar to them and after the purchase completed I delete it but I think it's not a good solution because this product will be shown to shop and other customers can purchase that while I want to offer this product to a certain customer only.

In another way, I tried to use Shopify discount but can't satisfy my need or maybe I can't find true ways.

How can I do that?

---

## 98. Request origin cannot be verified - Shopify
**Score:** 4 | **Tags:** shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/47553382/request-origin-cannot-be-verified-shopify

[![enter image description here](https://i.sstatic.net/ozfLT.jpg)](https://i.sstatic.net/ozfLT.jpg)I'm developing an app for Shopify. Currently under development stage. Until now, I have successfully managed to authorise the app and then redirect it back to admin page using the Embedded App SDK. However, when I return to the admin page, it gives me an error saying `Request origin cannot be verified`.

The console shows `Failed to load resource: the server responded with a status of 403 (Forbidden)`
The URL in the console is something like this `https://myshop.myshopify.com/admin/apps/dfdjf4343343434343434bfdf/shopify/shopify/callback?code=ffdfdffd&hmac=fdfdfdfdfdfdfdfdfddfdfdfdfdf&shop=myshop.myshopify.com&state=151193864548800&timestamp=1511938648`

The `fdfdfdfdfdfdfdfdfddfdfdfdfdf` are just random characters that I've replaced instead of a hash. FYI - I've removed the app name and user profile name and avatar from the image.

---

## 99. How to add JavaScript in Shopify public app
**Score:** 4 | **Tags:** ruby-on-rails, shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/55415281/how-to-add-javascript-in-shopify-public-app

Im developing a **Shopify public app using Ruby on Rails**. I want disaply some information in all the store front pages. The official documents only explains about the admin panel modifications. How can I access the store front? And where I should add the scripts, I mean in which controller?

Actually Im a PHP Developer. Im new to Shopify and also Ruby on Rails. Im trying to develop a shopify public app which will show product related information in all pages (front-end). I followed [shopify's tutorial](https://help.shopify.com/en/api/tutorials/build-a-shopify-app-with-ruby-and-sinatra) first, and created a hello world like app which displays products list in admin side. But I really cant find anything that make changes in the store frontend.

So please help me that how to make changes in frontend. Also I want to get the current user information and product details (if it is a product view page).

---

## 100. Error: GraphQL error: Field &#39;metafieldsSet&#39; doesn&#39;t exist on type &#39;Mutation&#39; - Shopify GraphQL error
**Score:** 4 | **Tags:** graphql, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/70216232/error-graphql-error-field-metafieldsset-doesnt-exist-on-type-mutation-s

I have been recently playing with Shopify App Development and i'm struggling with a graphql call to amend some text. The image below displays the call being made correctly in the shopify GraphQL app which is where I test it.

[![enter image description here](https://i.sstatic.net/1jtrn.png)](https://i.sstatic.net/1jtrn.png)

However when I attempt to make this same call from the react component I get the following error

```
Unhandled Runtime Error
Error: GraphQL error: Field 'metafieldsSet' doesn't exist on type 'Mutation'
GraphQL error: Variable $metafields is declared by metafieldsSet but not used
```

Here is the react component in which I try and update the metafield

```
import React, { useState } from 'react';
import gql from 'graphql-tag';
import { Mutation } from 'react-apollo';
import { Layout, Button, Banner, Toast, Stack, Frame } from '@shopify/polaris';
import { Context } from '@shopify/app-bridge-react';
// GraphQL mutation that updates the prices of products
const UPDATE_TEXT = gql`mutation metafieldsSet($metafields: [MetafieldsSetInput!]!) {
    metafieldsSet(metafields: $metafields) {
      metafields {
        value
        id
        key
        ownerType
     
      }
      userErrors {
        field
        message
      }
    }
  }
`;
class UpdateTheText extends React.Component{
    static contextType = Context;
    render(){
        return(
            <Mutation mutation={UPDATE_TEXT}>
            {(handleSubmit, {error, data}) => {
              const [hasResults, setHasResults] = useState(false);
    
              const showError = error && (
                <Banner status="critical">{error.message}</Banner>
              );
    
              const showToast = hasResults && (
                <Toast
                  content="Successfully updated"
                  onDismiss={() => setHasResults(false)}
                />
              );
    
              return (
                <Frame>
                  {showToast}
                  <Layout.Section>
                    {showError}
                  </Layout.Section>
    
                  <Layout.Section>
                    <Stack distribution={"center"}>
                      <Button
                        primary
                        textAlign={"center"}
                        onClick={() => {
                          let promise = new Promise((resolve) => resolve());
                            const newmetafields = {
                                  key: "ExtraShopDesc",
                                  namespace: "ExtraShopDescription",
                                  ownerId: "gid://shopify/Shop/55595073672",
                                  type: "single_line_text_field",
                                  value: "This is an extra shop description twice"
                              }
    
                            promise = promise.then(() => handleSubmit({ variables: { metafields: newmetafields }}));
                          
    
                          if (promise) {
                            promise.then(() => this.props.onUpdate().then(() => setHasResults(true)));
                        }}
                      }
                      >
                        Update Text
                      </Button>
                    </Stack>
                  </Layout.Section>
                </Frame>
              );
            }}
          </Mutation>
        );
    }

}

export default UpdateTheText;
```

I believe i'm passing the variables into the gql but it doesn't seem to be picking them up?

---

## 101. Customise bulk products on same collection in shopify theme
**Score:** 4 | **Tags:** shopify, liquid, liquid-layout, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/46828373/customise-bulk-products-on-same-collection-in-shopify-theme

Is there an option to get customisation of one product in collection and apply the customisation to all the products that comes under the same collection?

For Example:

If we customised the product such as added a link, sorted sections or blocks, inserted a text section, etc... for the product "XXXX" that comes under category "Police", can we apply the customisation to all the products that falls under same "Police" category?

---

## 102. How to wrap text in Polaris Index Table cell?
**Score:** 4 | **Tags:** shopify-app, polaris | **Answered:** False
**Link:** https://stackoverflow.com/questions/74982517/how-to-wrap-text-in-polaris-index-table-cell

am using Polaris Index Table to display some data in my Shopify app. One of the cells in my table has a long string of text and I want to make it wrap so that it fits the size of the screen. Is there a way to do this in Polaris?

Here is my code:

```
import {IndexTable, Card, useIndexResourceState, Text} from '@shopify/polaris';
import React from 'react';

function SimpleIndexTableExample() {
  const customers = [
    {
      id: '3411',
      url: 'customers/341',
      name: 'Mae Jemison long text here, very very long......',
      location: 'Decatur, USA',
      orders: 20,
      amountSpent: '$2,400',
    },
    {
      id: '2561',
      url: 'customers/256',
      name: 'Ellen Ochoa',
      location: 'Los Angeles, USA',
      orders: 30,
      amountSpent: '$140',
    },
  ];
  const resourceName = {
    singular: 'customer',
    plural: 'customers',
  };

  const {selectedResources, allResourcesSelected, handleSelectionChange} =
    useIndexResourceState(customers);

  const rowMarkup = customers.map(
    ({id, name, location, orders, amountSpent}, index) => (
      <IndexTable.Row
        id={id}
        key={id}
        selected={selectedResources.includes(id)}
        position={index}
      >
        <IndexTable.Cell>
          <Text variant="bodyMd" fontWeight="bold" as="span">
            {name}
          </Text>
        </IndexTable.Cell>
        <IndexTable.Cell>{location}</IndexTable.Cell>
        <IndexTable.Cell>{orders}</IndexTable.Cell>
        <IndexTable.Cell>{amountSpent}</IndexTable.Cell>
      </IndexTable.Row>
    ),
  );

  return (
    <Card>
      <IndexTable
        resourceName={resourceName}
        itemCount={customers.length}
        selectedItemsCount={
          allResourcesSelected ? 'All' : selectedResources.length
        }
        onSelectionChange={handleSelectionChange}
        headings={[
          {title: 'Name'},
          {title: 'Location'},
          {title: 'Order count'},
          {title: 'Amount spent'},
        ]}
      >
        {rowMarkup}
      </IndexTable>
    </Card>
  );
}
```

I've tried modifying the cells, styles, etc.

---

## 103. Pass Shopify AppBridge instance to various Nuxt / Vue components
**Score:** 4 | **Tags:** vue.js, shopify, nuxt.js, shopify-app | **Answered:** False
**Link:** https://stackoverflow.com/questions/63197662/pass-shopify-appbridge-instance-to-various-nuxt-vue-components

I'm trying to initialize a Shopify AppBridge instance (<https://shopify.dev/tools/app-bridge>) one time per store (user), and then use that same instance throughout my app to use the various AppBridge features.

My original idea was to add the AppBridge instance into a Vuex store; but I am unable to call any functions within the AppBridge object when retrieving it from the store (something to do with it being a serialized object?). There are various functions I need to use within the instance/object; so this won't work.

So, what is the best way for me to do the following:

1. App loads
2. Middleware or function runs, initializing AppBridge with the user's / store's details
3. Other pages are loaded, use the same AppBridge instance for various features

My current setup is that I re-create a new AppBridge instance on every page / component, but that causes complications.

Any ideas? Much appreciated!

---

## 104. Dynamic Variant Price while adding variant into the Shopify cart
**Score:** 4 | **Tags:** shopify, shopify-app | **Answered:** False
**Link:** https://stackoverflow.com/questions/58405891/dynamic-variant-price-while-adding-variant-into-the-shopify-cart

I have Shopify Store, where customer can design/customise their product before buying it. and based on the design / customisation price of the selected variant may get varied. but I think Shopify does not facilitate to change variant price dynamically while adding into cart.

Is any solution there I might be missing ? Any help will be appreciated.

---

## 105. How would one go about building true React SPA theme in Shopify
**Score:** 4 | **Tags:** javascript, reactjs, shopify, liquid, shopify-app | **Answered:** False
**Link:** https://stackoverflow.com/questions/57404581/how-would-one-go-about-building-true-react-spa-theme-in-shopify

How would one go about building React SPA theme, which will handle routing client-side and will use all the benefits of Shopify Plus plan, (e.g. managed hosting, bandwidth, etc...).

All examples I could find are using Shopify Storefront API as a headless seems, but we all looking for a more “hybrid” solution relying on Shopify Plus servers, but at the same time using as less liquid as possible.

---

## 106. OAuth request redirects to admin dashboard after login shopify
**Score:** 4 | **Tags:** oauth, shopify, shopify-app | **Answered:** False
**Link:** https://stackoverflow.com/questions/51187176/oauth-request-redirects-to-admin-dashboard-after-login-shopify

I have created a shopify application to read store data like category name, product name etc. Following this guideline <https://help.shopify.com/api/getting-started/authentication/oauth>

I have written script in python to make OAUTH request to install my application in shopify store. I am using the api key, secret key during OAuth request and also set the app url, whitelisted redirection url in my application in partner dashboard.
Here 2 cases happen:

1. the first case is when store owner is logged into the store OAuth request is granted and redirects to application installation page, and after installation redirects to redirect\_url passed with OAuth request URL.
2. the 2nd case is when store owner is not logged into store OAuth request redirects to store login page and after login page redirects to admin dashboard of the store. does not redirect to application installation page.

No problem with the first case. I have been trying to solve the 2nd case. I want to redirect to application installation page after logged into the store.

Besides me other shopify developers are facing this problem. here are 2 other links of unanswered same question in shopify discussion forum.

<https://ecommerce.shopify.com/c/shopify-apis-and-technology/t/oauth-flow-for-non-logged-in-users-526732>

<https://ecommerce.shopify.com/c/shopify-apps/t/oauth-error-whitelisted-url-if-user-is-not-logged-in-516603>

what I have tried:

I am trying to do it in django. here is the code in which I am trying to redirect user to shopify store for authorization.

```
def redirect_to_shopify_store(request):
    redirect_url = "https://" + store_name + ".myshopify.com/admin/oauth/authorize?client_id=" + api_key

    redirect_url += "&scope=read_orders, write_checkouts, read_themes, write_themes, read_products, write_products, unauthenticated_read_product_listings, read_product_listings, read_collection_listings"

    redirect_url += "&redirect_uri=" + python_app_base_url + "/get_shopify_access_token/"

    redirect(redirect_url)
```

and here is the code I am trying to receive the shopify access token:

```
def get_shopify_access_token(request):
    code = request.GET.get('code')
    client_id = shopify_config['client_id']

    request_url = "https://{store_name}.myshopify.com/admin/oauth/access_token?client_id={client_id}".format(
    store_name=store_name, client_id=client_id
    )

    request_url += "&client_secret=" + shopify_config['client_secret']
    request_url += "&code=" + code

    response = requests.post(request_url)

    shopify_access_token = response.json()['access_token']

    print("shopify_access_token")
    print(shopify_access_token)

    redirect('success_page_url')
```

If I redirect like the following URL

```
https://{store_name}.myshopify.com/admin/auth/login?redirect=oauth/authorize?client_id, access_scope
```

I get access\_scope missing error and get redirected to following URL:

```
https://{store_name}.myshopify.com/admin/oauth/authorize?client_id
```

could not identify the reason for missing accsess\_scope param.

Any help from shopify experts will be appreciated.

---

## 107. GraphQL implimentation with Shopify using Java
**Score:** 4 | **Tags:** java, shopify, graphql, shopify-app, graphql-java | **Answered:** False
**Link:** https://stackoverflow.com/questions/51060705/graphql-implimentation-with-shopify-using-java

I am building a Shopify app which needs to adjust inventory of products in Shopify. Shopify is about to deprecate its inventory adjustment POST call using `admin/product.json` and will updated to `/admin/inventory_levels/adjust.json`, but the new inventory adjustment POST call allows to update only single inventory level at a time.
But my app needs to update multiple inventory levels at some particular point of time, so doing POST call for every individual inventory level will be resource taking and time consuming. When I contacted a Shopify Expert, he recommended me to use GraphQL for the above purpose. I researched for GraphQL + Shoipfy implementation in Java but did not find satisfactory results, so I need help in implementing Client POST call of GraphQL in Java .
Below is my structure of GraphQL, I want to implement in Java

```
mutation {
  item1: inventoryAdjustQuantity(input: {inventoryLevelId: "gid://shopify/InventoryLevel/9229566067?inventory_item_id=10588945219699", availableDelta: 3}) {
    inventoryLevel {
      available
    }
    userErrors {
      field
      message
    }
  }
  item2: inventoryAdjustQuantity(input: {inventoryLevelId: "gid://shopify/InventoryLevel/9229762675?inventory_item_id=10588945219699", availableDelta: 3}) {
    inventoryLevel {
      available
    }
    userErrors {
      field
      message
    }
  }
  item3: inventoryAdjustQuantity(input: {inventoryLevelId: "gid://shopify/InventoryLevel/9229926515?inventory_item_id=10588945219699", availableDelta: 3}) {
    inventoryLevel {
      available
    }
    userErrors {
      field
      message
    }
  }
  item4: inventoryAdjustQuantity(input: {inventoryLevelId: "gid://shopify/InventoryLevel/9645391987?inventory_item_id=10588945219699", availableDelta: 3}) {
    inventoryLevel {
      available
    }
    userErrors {
      field
      message
    }
  }
  item5: inventoryAdjustQuantity(input: {inventoryLevelId: "gid://shopify/InventoryLevel/9645457523?inventory_item_id=10588945219699", availableDelta: 3}) {
    inventoryLevel {
      available
    }
    userErrors {
      field
      message
    }
  }
  item6: inventoryAdjustQuantity(input: {inventoryLevelId: "gid://shopify/InventoryLevel/9645490291?inventory_item_id=10588945219699", availableDelta: 3}) {
    inventoryLevel {
      available
    }
    userErrors {
      field
      message
    }
  }
  item7: inventoryAdjustQuantity(input: {inventoryLevelId: "gid://shopify/InventoryLevel/9229566067?inventory_item_id=10588945252467", availableDelta: 3}) {
    inventoryLevel {
      available
    }
    userErrors {
      field
      message
    }
  }
  item8: inventoryAdjustQuantity(input: {inventoryLevelId: "gid://shopify/InventoryLevel/9229762675?inventory_item_id=10588945252467", availableDelta: 3}) {
    inventoryLevel {
      available
    }
    userErrors {
      field
      message
    }
  }
  item9: inventoryAdjustQuantity(input: {inventoryLevelId: "gid://shopify/InventoryLevel/9229926515?inventory_item_id=10588945252467", availableDelta: 3}) {
    inventoryLevel {
      available
    }
    userErrors {
      field
      message
    }
  }
  item10: inventoryAdjustQuantity(input: {inventoryLevelId: "gid://shopify/InventoryLevel/9645391987?inventory_item_id=10588945252467", availableDelta: 3}) {
    inventoryLevel {
      available
    }
    userErrors {
      field
      message
    }
  }
}
```

It would be great if you will help me with this issue or will guide me to some resourceful link.

---

## 108. Shopify Billing API after OAuth
**Score:** 4 | **Tags:** ruby-on-rails, shopify, shopify-app | **Answered:** False
**Link:** https://stackoverflow.com/questions/48202853/shopify-billing-api-after-oauth

After I complete OAuth how do I immediately redirect to my recurring charges controller, so I can initiate a charge request with the user? It would be a POST request to my charges controller. The documentation was not any help! I'm guessing it has something to do with redirecting after authentication, but since this is a post request to a controller is that even possible? My app is built on the Shopify Gem using code from Link 2.

[Sample Code from Github Using Sinatra on Charge Controllers](https://github.com/Shopify/example-ruby-app/blob/master/02%20Charging%20For%20Your%20App/app.rb)

[Session Controller from Shopify Gem App Skeleton](https://github.com/Shopify/shopify_app/blob/master/app/controllers/shopify_app/sessions_controller.rb)

---

## 109. How to fetch shopify products based on multiple varying tags which are given dynamically in python?
**Score:** 3 | **Tags:** graphql, shopify, shopify-api, shopify-api-node | **Answered:** True
**Link:** https://stackoverflow.com/questions/62779854/how-to-fetch-shopify-products-based-on-multiple-varying-tags-which-are-given-dyn

I am trying to fetch products from shopify by filtering based on tags. Tags will be dynamic, more than one, and will change.

```
import json
import time
import requests

API_KEY = 'xxxx'
PASSWORD = 'xxxx'
SHOP_NAME = 'xxxx'
API_VERSION = '2020-04' #change to the API version
shop_url = "https://%s:%s@%s.myshopify.com/admin/api/%s" % (API_KEY, PASSWORD, SHOP_NAME, API_VERSION)

def callShopifyGraphQL(GraphQLString, data):
    headers = {
        "X-Shopify-Storefront-Access-Token": 'xxxxxx',
        "accept":"application/json"      
    }
    response = requests.post(shop_url+'/graphql', json={'query': GraphQLString, 'variables': data}, headers=headers)
    answer = json.loads(response.text)
    return answer['data']

str1 = '0-12'
str2 = 'physical'

graphQLquery7 = """ {
  products(first:100, query:"tag:$tags") {
    edges {
      node {
        id
        tags
        title
        onlineStoreUrl
      }
    }
  }
}"""

tag = dict({
  "tags":[str1,str2]
})

resp = callShopifyGraphQL(graphQLquery7, tag)
print json.dumps(resp)


# This query works fine and gives multiple products
# graphQLquery2 = """{
#   products(first:100, query:"tag:[0-12, physical]") {
#     edges {
#       cursor
#       node {
#         id
#         tags
        
#         title
#         onlineStoreUrl
#       }
#     }
#   }
# }"""
```

The Output that I am getting is basically a JSON with products empty

```
{u'extensions': {u'cost': {u'requestedQueryCost': 102, u'throttleStatus': {u'restoreRate': 50.0, u'currentlyAvailable': 998, u'maximumAvailable': 1000.0}, u'actualQueryCost': 2}}, u'data': {u'products': {u'edges': []}}}
{"products": {"edges": []}}
```

I am unable to pass my tags as a variable in the query. I am currently using GraphQl because I couldn't find REST APIs fetch product based on multiple tags which would vary.

EDIT: Removed Python tag as this was not a python issue and I have added the answer as well lisitng two methods on how to do this

---

## 110. CORS error when using shopify admin api in front end
**Score:** 3 | **Tags:** javascript, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/69250522/cors-error-when-using-shopify-admin-api-in-front-end

I have shopify admin api and I want to call it in the front end but when i try to fetch the data it gives me the following error "Access to XMLHttpRequest at 'https://API\_KEY:PASSORD@NAME.myshopify.com/admin/api/2021-07/orders.json' from origin 'null' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource.", I use axios and fetch and both did not work.
any help well be appreciated.

---

## 111. Modify Shopify Shipping Rates at Checkout
**Score:** 3 | **Tags:** shopify, shopify-app, shopify-api, shopify-api-node | **Answered:** True
**Link:** https://stackoverflow.com/questions/66276573/modify-shopify-shipping-rates-at-checkout

Is there a possibility that we could add a custom shipping price at checkout through an API call or script?
[![enter image description here](https://i.sstatic.net/d4Fdf.png)](https://i.sstatic.net/d4Fdf.png)

I want to modify the price based on some rules and I can't figure out how to do it in Shopify. Any help will be highly appreciated.

---

## 112. How to create a REST request using the Shopify Node JS API for a Private App?
**Score:** 3 | **Tags:** node.js, shopify, shopify-api, shopify-api-node | **Answered:** True
**Link:** https://stackoverflow.com/questions/74863219/how-to-create-a-rest-request-using-the-shopify-node-js-api-for-a-private-app

I'm trying to use the Shopify API to query all the orders of a selected Shopify store, using the private app instead of the OAUTH method. Below I have added the code, can't seem to figure out how to get it to work cause there isn't much documentation for the use of the private apps. Does anyone know how I can achieve this or has done this before? I think I maybe wrong but there maybe an error in creating the session.

Upon running the below code I get the below error:
`Error: Missing adapter implementation for 'abstractRuntimeString' - make sure to import the appropriate adapter for your platform`

```
const { shopifyApi, ApiVersion, Session, LATEST_API_VERSION } = require('@shopify/shopify-api');
const { randomUUID } = require('crypto');
const { restResources } = require('@shopify/shopify-api/rest/admin/2022-10');


const selectedStore = {
shop: "store.myshopify.com",
api_secret: "",
api_key: "",
private_admin_key: ""
};

const shopify = shopifyApi({
    apiKey: selectedStore.api_key,
    apiSecretKey: selectedStore.api_secret,
    scopes: ['read_orders', 'read_analytics', 'read_customers'],
    hostName: '<ngrok_url>',
    apiVersion: LATEST_API_VERSION,
    isEmbeddedApp: false,
    isPrivateApp: true,
    restResources
});

const session = new Session({
    id: randomUUID(),
    state: 'state',
    shop: selectedStore.shop,
    accessToken: selectedStore.private_admin_key,
    isOnline: true,
})

console.log(session)

const getOrders = async () => {
    const orders = await shopify.rest.Order.all({
        session,
        status: "all"
    })
    return orders
}

getOrders()
```

---

## 113. Silent authenticate customer via Shopify API
**Score:** 3 | **Tags:** shopify, shopify-app, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/62693622/silent-authenticate-customer-via-shopify-api

We have set up a Shopify store for our brand.
We have users already logged into our web app and our mobile app. Our goal is to manage the whole user journey under a single authentication (that being our web app and mobile app login). When the user then visits the store section in the web app and the mobile app, the app should silently login to the Shopify store with the same credentials of their existing accounts.

For this, I found that we can create a new customer [here](https://shopify.dev/docs/admin-api/rest/reference/customers/customer?api%5Bversion%5D=2020-04).
My questions are:

1. Is this the correct way of managing the users?
2. Is it a good practice to manage users this way?
3. What are the scopes needed to use this endpoint?

---

## 114. Shopify Storefron API - Search query containing term not working
**Score:** 3 | **Tags:** search, graphql, shopify, shopify-api, shopify-storefront-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/73062878/shopify-storefron-api-search-query-containing-term-not-working

so what i want to do is querying the products title with a search term and i expect to get all products containing the term somewhere in the title to be returned.

For example in the graphql explorer we have this product title: "3/4 SLEEVE CREWNECK PULLOVER"

I want this to be returned with the following query:

```
{
  products(first: 250, query:"title:neck") {
    edges {
      node {
        title
      }
    }
  }
}
```

From the docs i can't figure out a way. If you want to try it out you can do it here: <https://shopify.dev/custom-storefronts/tools/graphiql-storefront-api>

Any help is appreciated!

Cheers

---

## 115. NameError: uninitialized constant ShopifyAPI::Session shopify_app gem -v 19, rails 7
**Score:** 3 | **Tags:** ruby-on-rails, shopify-app, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/72545987/nameerror-uninitialized-constant-shopifyapisession-shopify-app-gem-v-19-rai

I am using background jobs to get orders via webhook and perform some other processing. I get the webhook it on my background jobs but when When I try to initiate a session it gives me the following error.

**[NameError: uninitialized constant ShopifyAPI::Session](https://i.sstatic.net/dtjL0.png)**
I am using the following versions:
**rails:- 7.0.3, ruby:- 3.1.2, shopify\_app:- 19.0.2**

can anyone explain it to me that what I am doing wrong here? Did the gem update/latest version has a different approach to activate or create a session in background job.

I really appreciate your suggestions.

---

## 116. Accessing Brand object inside Shop resource in Shopify GraphQL API
**Score:** 3 | **Tags:** graphql, shopify, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/79533470/accessing-brand-object-inside-shop-resource-in-shopify-graphql-api

I'm trying to access the `shop.brand.logo` field in the `Shop` resource, I'm using API version 2025-01.

<https://shopify.dev/docs/api/storefront/2025-01/objects/Brand>

```
query ShopData {
  shop {
    brand {
      logo {
        image {
          url
        }
      }
    }
  }
}
```

I get this error:

```
{
    "errors": [
        {
            "message": "Field 'brand' doesn't exist on type 'Shop'",
            "locations": [
                {
                    "line": 9,
                    "column": 9
                }
            ],
            "path": [
                "query ShopData",
                "shop",
                "brand"
            ],
            "extensions": {
                "code": "undefinedField",
                "typeName": "Shop",
                "fieldName": "brand"
            }
        }
    ]
}{
    "errors": [
        {
            "message": "Field 'brand' doesn't exist on type 'Shop'",
            "locations": [
                {
                    "line": 9,
                    "column": 9
                }
            ],
            "path": [
                "query ShopData",
                "shop",
                "brand"
            ],
            "extensions": {
                "code": "undefinedField",
                "typeName": "Shop",
                "fieldName": "brand"
            }
        }
    ]
}
```

Which is weird because it's explicitly mentioned in their API docs.
Does anyone know any workaround to get the brand logo through the GraphQL API? I would discard any REST API solution since it's sunsetting soon.

---

## 117. How to get the currently logged in customer id using Liquid / JS
**Score:** 3 | **Tags:** shopify, shopify-api, shopify-template, shopify-storefront-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/79349295/how-to-get-the-currently-logged-in-customer-id-using-liquid-js

Since switching to new Customer Accounts sytem, I can't figure out how to access the currently logged in customer in my theme.

With the old system, the customer id was accessible via {{ customer.id }} in liquid, and \_\_st.cid in JavaScript. This no longer works when using the new Customer Accounts.

What's the best way to access the customer id in a theme with the new system?

See also here: <https://community.shopify.com/c/shopify-functions/issue-with-new-customer-accounts-login/m-p/2785423>

Expected: {{ customer.id }} and \_\_st.cid return the id of the currently logged in customer, or null of not logged in.

Actual: Both values are undefined when using the new Customer Accounts system

---

## 118. Shopify cartDiscountCodesUpdate storefront API cartid
**Score:** 3 | **Tags:** shopify, shopify-app, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/73430546/shopify-cartdiscountcodesupdate-storefront-api-cartid

I want to apply discount coupon code to the cart page, I am trying to use the storefront API `cartDiscountCodesUpdate` which expect the cart id. How can I get this cart id. Here is what I tried. I have created the webhook `cart/create` which has payload `id` in the form of string something like '1eef2aa2c2b2e889ec325db72f0877ec'.

Then I tried calling this `id` which I got from `cart/create` response in storefront API `cartDiscountCodesUpdate` like:

```
 mutation cartDiscountCodesUpdate($cartId: ID!, $discountCodes: [String!]) {
  cartDiscountCodesUpdate(cartId: $cartId, discountCodes: $discountCodes) {
   cart {
     id
   }
   userErrors {
     field
     message
   }
  }
 }
```

Query Varialbe:
{
"cartId": "gid://shopify/Cart/1eef2aa2c2b2e889ec325db72f0877ec",
"discountCodes": [
"64J1ZQMBN9W5"
]
}

But its response with below error. I think its the issue with incorrect cart id. Can anyone help me how to get cart id after the cart is created?

Response from `cartDiscountCodesUpdate` storefront API.

```
 {
  "data": {
  "cartDiscountCodesUpdate": {
  "cart": null,
  "userErrors": [
    {
      "field": [
        "cartId"
      ],
      "message": "The specified cart does not exist."
    }
    ]
   }
  }
 }
```

---

## 119. How to display data in Shopify Store from external API using app proxy
**Score:** 3 | **Tags:** shopify, shopify-app, shopify-api, shopify-api-node | **Answered:** False
**Link:** https://stackoverflow.com/questions/69939144/how-to-display-data-in-shopify-store-from-external-api-using-app-proxy

My goal is to display data retrieved from a 3rd party (external) API that requires authentication in my Liquid Shopify theme.

I'm looking to access product options data from the Hulk Product Options API, which requires authentication, as documented here: <https://productoption.hulkapps.com/api-docs/index.html>

My goal would be to send a get request and retrieve data from the Hulk Product Options endpoint.

I've read that an App Proxy is what I need to set up, however I am new to the Shopify app world and am totally lost at how to set this up.

What I've done:

1. Followed [the steps here](https://shopify.dev/apps/getting-started/create) to create an app and install it on a development store that I created through my partners dashboard.
2. Went to the partners dashboard, clicked "Apps" and found the app proxy section.

Questions:

1. What do I put in those fields? I can't find examples for filling out that section with info from an external API.
2. What code in which file do I need to add to the node app that was generated using `shopify node create`. Or is this app just necessary to be able to fill out the app proxy info?
3. What url can I send a GET request to using AJAX / JS in my liquid theme code?

I'm a theme developer new to app development and have never created an app, so if you can provide basic and specific instructions (code would be wonderful!) for someone who knows front-end and is competent but is lost in the app world it's much appreciated. I've asked other theme developers who also have also tried and not been able to figure this out, so there seems to be a gap in the tutorials and resources provided.

Thanks in advance!

---

## 120. Use variables in Shopify Bulk Operations graphql mutation
**Score:** 3 | **Tags:** graphql, shopify, graphql-js, shopify-app, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/69354063/use-variables-in-shopify-bulk-operations-graphql-mutation

I am trying to use graphql to query a store's orders in a bulk operation. I am using a tags variable in the graphql request to query orders with specific tags. I have been following Shopify's [documentation](https://shopify.dev/api/usage/bulk-operations/queries#write-a-bulk-operation) in order to do this.

Here is what I've been trying:

```
const variables = {
  "tags": "tag:foo AND tag:bar"
};

const query = gql`
  mutation getOrders($tags: String!) {  
    bulkOperationRunQuery(
      query:"""
        query {
          orders(query: $tags) {
            edges {
              node {
                id
                email
              }
            }
          }
        }
      """
    ) {
      bulkOperation {
        id
        url
        status
      }
      userErrors {
        field
        message
      }
    }
  }
`;

const bulkOperation = await graphQLClient.request(query, variables);
```

However, I always get this error back from the api:

```
Variable $tags is declared by getOrders but not used
```

Does anyone know if there is a way to use a graphql variable in that bulk operation? Thanks!

---

## 121. In Shopify, how do i get the logged in user information of admin section?
**Score:** 3 | **Tags:** javascript, reactjs, ruby-on-rails, shopify-app, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/69201944/in-shopify-how-do-i-get-the-logged-in-user-information-of-admin-section

I want to track the actions taken by the logged-in user in Shopify admin.

If a shop has multiple staff with admin access, how can I get the information of which staff/user is currently logged in?

It can be either via API or from JS.

---

## 122. Add discount to Shopify ajax cart
**Score:** 3 | **Tags:** shopify, shopify-template, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/66813411/add-discount-to-shopify-ajax-cart

I'm using the Shopify [Ajax Cart Api](https://shopify.dev/docs/themes/ajax-api/reference/cart) and trying to add an item with a discount. Does anyone know if this is possible? I know I can just add an item at the discounted price, but that's not the experience I want.

Current request looks like this:

```
const order = []

addToCart() {
        if(this.unlimitedAdded === true){
          console.log("pushing order w/ unlimited")
          this.order.push({
            quantity: this.quantity,
            id: this.productID,
      },
      {
        quantity: 1,
        id: 31095169613901
      })
      this.$store.commit('cart/add', this.unlimited)
        } else {
          this.order.push({
            quantity: this.quantity,
            id: this.productID,
            })
        }
      this.$store.commit('cart/add', this.planName)
      if (window.ShopifyAnalytics) {
        console.log('Firing Shopify track data from Nuxt')
        window.ShopifyAnalytics.lib.track(
            'monorail://trekkie_storefront_added_product/1.0',
            {
              'currency': 'USD',
              'productId': this.productID,
              'name': this.planName,
              'price': this.salePrice,
              'brand': 'Shine Bathroom',
              'variant': this.planName,
              'category': 'Bathroom Assistant',
              'nonInteraction': true,
            },
        )
      }

      console.log(`Adding ${this.productID} to cart. Quantity: ${this.quantity}`)
      this.$axios.post('/cart/add.js', {items: this.order},)
      .then((response) => {
        console.log(response)
        window.location.href = '/pages/direct-checkout'
      }, (error) => {
        console.log(error)
      })
    }
```

Ideally I would like to send a discount code with the quantity and id, but I don't see that anywhere in their documentation for this specific resource.

Thanks!

---

## 123. Shopify API GraphQL: How to call GraphQL API programmatically?
**Score:** 3 | **Tags:** graphql, shopify-app, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/66679788/shopify-api-graphql-how-to-call-graphql-api-programmatically

I want to add a scripttag to an Onlinestore, and I managed to do it with the GraphQL explorer/app.

But I am completely lost in how to do it programmatically in my app, and the Shopify documentation doesn't really help me.

My goal: When a merchant presses a button in his admin page, I want my app to post a scripttag to this store.

I have created the an app with the Shopify App CLI.

In the server folder the CLI creates (these are the parts I suspect are important)

```
//this is in file "server.js"

router.post("/graphql", verifyRequest(), async (ctx, next) => {
    await Shopify.Utils.graphqlProxy(ctx.req, ctx.res);
  });
```

In server/handlers/mutations/

The CLI creates two files "get-subscription-url.js" and "get-one-time-url.js" where Graph Ql calls are done.

However, I dont understand how the frontend (the pages folder) can make these API calls.

If the merchant presses a button, how can I let apollo make a mutation api call? How is it authenticated?

Or do I (somehow) have to pass the API Call request to my backend, the server folder (maybe the route /graphql ?), so that the backend executes the mutation/query?

---

## 124. how to add redirect page in shopify plus?
**Score:** 3 | **Tags:** javascript, shopify, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/66541525/how-to-add-redirect-page-in-shopify-plus

How to add a simple page which says "Wait while we redirect you" and then redirect to custom payment/loyalty page in shopify. We have shopify+ account & our own loyalty point (manual payment method setup).

So for example below:

1. customer on checkout page:
   [![enter image description here](https://i.sstatic.net/bgORa.png)](https://i.sstatic.net/bgORa.png)
2. now customer on redirect page like below:
   [![enter image description here](https://i.sstatic.net/Y87z6.png)](https://i.sstatic.net/Y87z6.png)
3. the customer on the custom payment page.

Now, I wanted to create redirect page and if my customer select certain payment/loyalty option then they will redirect to the point 2) screenshot and then go to point 3) but if they decided to go from point 3) to point 1) then the order should not be created in shopify.

so we are skipping processing step where order has been created.

I've done lots of research on this by looking different options. Please do not suggest additional script as we got the shopify plus store where I want to create redirect page and skipping order creation at that point.
I know `window.location` but this is not I am looking for.

My reserach:
[checkout liquid shopify](https://shopify.dev/docs/themes/theme-templates/checkout-liquid)

[Editing checkout page best practices](https://shopify.dev/tutorials/develop-theme-layouts-checkout-best-practices)

I know we can achieve this by using below but not sure how:
[![enter image description here](https://i.sstatic.net/oaXkU.png)](https://i.sstatic.net/oaXkU.png)

---

## 125. Generate both online and offline access token for a Shopify public app
**Score:** 3 | **Tags:** shopify, koa, shopify-app, shopify-api, shopify-api-node | **Answered:** False
**Link:** https://stackoverflow.com/questions/66091828/generate-both-online-and-offline-access-token-for-a-shopify-public-app

Shopify's boilerplate app does this to generate an access token (online accessMode by default)

```
server.use(
    createShopifyAuth({
      apiKey: SHOPIFY_API_KEY,
      secret: SHOPIFY_API_SECRET,
      scopes: [SCOPES],

      async afterAuth(ctx) {
        // Access token and shop available in ctx.state.shopify
        const { shop } = ctx.state.shopify;

        // Redirect to app with shop parameter upon auth
        ctx.redirect(`/?shop=${shop}`);
      },
    })
  );
```

In my case, I want both online and offline token

* Offline token will be generated once (if the store is not added to my database) with accessMode set to offline and pushed to the DB.
* Online token for the current logged in user.

Is there a way to generate both tokens in a single flow?

This below doesn't work. Koa responds a 404 not found

```
server.use(function (ctx, next) {

    console.log(JSON.stringify(ctx.request.query.shop))
    if (ctx.request && ctx.request.query && ctx.request.query.shop) {
        if (isStoreAlreadyAdded(ctx.request.query.shop) === 0) {
            createShopifyAuth({
      apiKey: SHOPIFY_API_KEY,
      secret: SHOPIFY_API_SECRET,
      scopes: [SCOPES],
      accessMode: 'offline',

      async afterAuth(ctx) {
        // Access token and shop available in ctx.state.shopify
        const { shop } = ctx.state.shopify;

        // Redirect to app with shop parameter upon auth
        ctx.redirect(`/?shop=${shop}`);
      },
    })
        }
    } else {
        shopifyAuth({
            afterAuth(ctx) {
                const {shop, accessToken} = ctx.state.shopify;
                console.log('We did it!', accessToken);
                ctx.redirect(`/?shop=${shop}`);
            },
        })
    }
});
```

---

## 126. Shopify Custom payment gateway without using Hosted Payment SDK
**Score:** 3 | **Tags:** shopify, shopify-app, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/62625900/shopify-custom-payment-gateway-without-using-hosted-payment-sdk

Shopify mentions using their [Hosted Payment SDK](https://shopify.dev/docs/hosted-payment-sdk) as their only way for implementing payment gateways for shopify. My requirement is a bit different. Here is my scenario

The customer checks out an order, then i have custom app (built by us) within shopify that customizes the checkout page and shows them a button that says "Make payment", when the user clicks on this button, they are sent out of shopify and brought to an external page that captures the order details passed during redirect, here the customer would pay for their order, after the payment is successful, the external app will call the shopify admin api and update payment status for this order, setting it to paid status, then the customer gets redirected back to shopify and the order is complete.

Using this flow, I won't have to use shopify's hosted payment SDK which requires approval and takes close to 30 for their team to get back to me.

I am new to shopify , would this be possible ? Is it possible to change order payment status using the shopify admin api ?

---

## 127. Laravel 5 get response header
**Score:** 3 | **Tags:** laravel-5, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/62177454/laravel-5-get-response-header

I need to get the Http response Link Header from a Shopify orders http request. Unfortunately, the application is still using Laravel 5.1 and not the latest version.

(I believe) The call is being made using Custom HTTP Requests with some docs on this page:
<https://laravel.com/docs/5.1/testing>

This is the call being made that returns order data but no other info.

```
$this->shopifyApiCreds->call($params)
```

This returns a response variable, but I do not know how to return any headers from this response.

Thanks!

---

## 128. Rails ShopifyAPI::Product does not return total_count, pagination does not worked using shopify-kaminari
**Score:** 3 | **Tags:** ruby-on-rails, ruby, shopify-app, shopify-api | **Answered:** False
**Link:** https://stackoverflow.com/questions/60181110/rails-shopifyapiproduct-does-not-return-total-count-pagination-does-not-worke

Gem info:

* omniauth-shopify-oauth2 (1.2.0)
* shopify-kaminari (1.1.0)
* shopify\_api (4.3.2 494b37a)
* shopify\_app (7.4.0)

**Request**:

```
parameters = {fields: 'id,title,url,handle', page: params[:page] || 1, limit: 5}
parameters = parameters.merge(title: params[:title]) if params[:title].present?

@products = ShopifyAPI::Product.find(:all, params: parameters)
```

**Issue**:

When requesting **WITH** filter for `title` result doesn't include `total_count`.

Thus `pagination` doesn't worked, doesn't show in view.

```
<%= paginate @items, :pagination_class => 'pagination-centered', params: {title: params[:title], page: params[:page] || 1} %>
```

---

## 129. Using custom variables in .ENV using Shopify CLI
**Score:** 3 | **Tags:** reactjs, shopify-app, shopify-api, shopify-api-node | **Answered:** True
**Link:** https://stackoverflow.com/questions/66681346/using-custom-variables-in-env-using-shopify-cli

I'm using the Shopify CLI to create an app which allows me to use Shopify Serve.

Whenever you run Shopify Serve it automatically rewrites the .ENV file and removes any custom variables added. I'm trying to add a variable for MongoDB.

Can someone suggest a solution to either allow me to use the .ENV file to store the MongoDB details or an alternative solution?

Thanks!

---

## 130. Oauth error missing_shopify_permission: read_all_orders
**Score:** 3 | **Tags:** shopify, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/53186710/oauth-error-missing-shopify-permission-read-all-orders

When i mentioned scope read\_all\_orders . I faced the following error while installation

Oauth error missing\_shopify\_permission: read\_all\_orders

Without read\_all\_orders scope App install perfectly.

I dont know what happens exactly i am trying both new created store and 2 month old store

My scopes :- 'read\_products', 'read\_orders', 'read\_customers', 'write\_orders', 'read\_price\_rules', 'write\_price\_rules', 'read\_all\_orders'

---

## 131. Shopify app access token - how to make it more secure?
**Score:** 3 | **Tags:** shopify, access-token, shopify-app | **Answered:** True
**Link:** https://stackoverflow.com/questions/58347894/shopify-app-access-token-how-to-make-it-more-secure

When store owner installs my app I save access tokens into database for later use. Having access tokens from store is huge security responsibility because anybody with these tokens can modify stores from any domain/address, there is no ip or domain lock.

What method could I use to make this more secure? I was thinking to save tokens offline and then upload it only when needed (in case I need to make some global updates for all stores), then delete it again. In case when merchant access app configuration within admin, I would just save it into session. Is there any better method?

---

## 132. Shopify npx shopify hydrogen link Access Denied
**Score:** 3 | **Tags:** shopify, hydrogen, shopify-hydrogen | **Answered:** True
**Link:** https://stackoverflow.com/questions/78333885/shopify-npx-shopify-hydrogen-link-access-denied

I am trying to create a Shopify website using shopify hydrogen, in the documentation it says to do npx shopify hydrogen.
When i do this i get this error:

```
    The Admin GraphQL API responded unsuccessfully with errors:

    [
      {
        "message": "Access denied for hydrogenStorefronts field. Required access: Request must be initiated from  
     the Shopify CLI and user must have full access to apps or access to the Hydrogen channel.",
        "locations": [
          {
            "line": 3,
            "column": 5
          }
        ],
        "path": [
          "hydrogenStorefronts"
        ],
        "extensions": {
          "code": "ACCESS_DENIED",
          "documentation": "https://shopify.dev/api/usage/access-scopes",
          "requiredAccess": "Request must be initiated from the Shopify CLI and user must have full access to     
    apps or access to the Hydrogen channel."
        }
      }
    ]

    Request ID: 90efe6d3-afcc-4dc3-8766-d612ceeecf62-1713263066
```

I have also watched some tutorials no how to set it up, and they say to go to your .env file and edit/add: PUBLIC\_STORE\_DOMAIN, PRIVATE\_STOREFRONT\_API\_TOKEN, PUBLIC\_STOREFRONT\_API\_TOKEN
However my env file only has
SESSION\_SECRET="foobar"
PUBLIC\_STORE\_DOMAIN="food-yes.myshopify.com"

it doesnt have a PRIVATE\_STOREFRONT\_API\_TOKEN, PUBLIC\_STOREFRONT\_API\_TOKEN variable declared.

Any advice would be helpful.

---

## 133. How can you use Sass Modules with Shopify Hydrogen V2?
**Score:** 3 | **Tags:** sass, css-modules, remix, shopify-hydrogen, sass-modules | **Answered:** False
**Link:** https://stackoverflow.com/questions/75690555/how-can-you-use-sass-modules-with-shopify-hydrogen-v2

I'm exploring using Hydrogen instead of Next.js Commerce for building out an ecommerce platform that I'm working on, but the only styling option for Hydrogen V2 seems to be tailwind or vanilla CSS. I can't find any documentation anywhere for using Sass Modules or even just CSS Modules like with Next.js.

---

## 134. Is there a Shopify Hydrogen component or hook to display the shop pay installments banner?
**Score:** 3 | **Tags:** reactjs, shopify, e-commerce, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/75470100/is-there-a-shopify-hydrogen-component-or-hook-to-display-the-shop-pay-installmen

I can see that it is possible to add this into a theme (reference: <https://shopify.dev/docs/themes/pricing-payments/installments>). But I cannot find any documentation regarding showing this in a custom store using Shopify hydrogen.

---

## 135. Error: Could not find client component Shopify hydrogen custom storefront
**Score:** 3 | **Tags:** reactjs, shopify, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/74217550/error-could-not-find-client-component-shopify-hydrogen-custom-storefront

So I came up with this weird issue I've got no idea why it happened. This is e-com site I was using shopify hydrogen to build and deploy. I was ok under dev enviroment, but the following errors shows up when I tried to deploy. Then I found 'yarn preview' also gave the same error. Any help on this?

[![enter image description here](https://i.sstatic.net/SPFyy.jpg)](https://i.sstatic.net/SPFyy.jpg)

```
react-dom.production.min.js:189 Error: Could not find client component HomeProductBanner-NzY1NjE3NDQ3
    at Ep (react-server-dom-vite.js:49:1)
    at wp (react-server-dom-vite.js:83:1)
    at Qp (react-server-dom-vite.js:404:1)
    at Kp (react-server-dom-vite.js:462:1)
    at Gp (react-server-dom-vite.js:512:1)
    at r (react-server-dom-vite.js:565:1)
Vo @ react-dom.production.min.js:189
o.componentDidCatch.n.callback @ react-dom.production.min.js:190
Hu @ react-dom.production.min.js:144
us @ react-dom.production.min.js:261
yc @ react-dom.production.min.js:260
Kd @ react-dom.production.min.js:259
qd @ react-dom.production.min.js:283
Et @ react-dom.production.min.js:281
gc @ react-dom.production.min.js:270
S @ scheduler.production.min.js:13
dn @ scheduler.production.min.js:14
react-dom.production.min.js:189 Error: Could not find client component HomeSocksBanner-MTYyNTk5NzAzMQ
    at Ep (react-server-dom-vite.js:49:1)
    at wp (react-server-dom-vite.js:83:1)
    at Qp (react-server-dom-vite.js:404:1)
    at Kp (react-server-dom-vite.js:462:1)
    at Gp (react-server-dom-vite.js:512:1)
    at r (react-server-dom-vite.js:565:1)
Vo @ react-dom.production.min.js:189
o.componentDidCatch.n.callback @ react-dom.production.min.js:190
Hu @ react-dom.production.min.js:144
us @ react-dom.production.min.js:261
yc @ react-dom.production.min.js:260
Kd @ react-dom.production.min.js:259
qd @ react-dom.production.min.js:283
Et @ react-dom.production.min.js:281
gc @ react-dom.production.min.js:270
S @ scheduler.production.min.js:13
dn @ scheduler.production.min.js:14
react-dom.production.min.js:189 Error: Could not find client component HomeLottery-LTE1NzcyNjUxMjc
    at Ep (react-server-dom-vite.js:49:1)
    at wp (react-server-dom-vite.js:83:1)
    at Qp (react-server-dom-vite.js:404:1)
    at Kp (react-server-dom-vite.js:462:1)
    at Gp (react-server-dom-vite.js:512:1)
    at r (react-server-dom-vite.js:565:1)
Vo @ react-dom.production.min.js:189
o.componentDidCatch.n.callback @ react-dom.production.min.js:190
Hu @ react-dom.production.min.js:144
us @ react-dom.production.min.js:261
yc @ react-dom.production.min.js:260
Kd @ react-dom.production.min.js:259
qd @ react-dom.production.min.js:283
Et @ react-dom.production.min.js:281
gc @ react-dom.production.min.js:270
S @ scheduler.production.min.js:13
dn @ scheduler.production.min.js:14
react-dom.production.min.js:189 Error: Could not find client component HomeHands-ODQwMjg5NDM4
    at Ep (react-server-dom-vite.js:49:1)
    at wp (react-server-dom-vite.js:83:1)
    at Qp (react-server-dom-vite.js:404:1)
    at Kp (react-server-dom-vite.js:462:1)
    at Gp (react-server-dom-vite.js:512:1)
    at r (react-server-dom-vite.js:565:1)
Vo @ react-dom.production.min.js:189
o.componentDidCatch.n.callback @ react-dom.production.min.js:190
Hu @ react-dom.production.min.js:144
us @ react-dom.production.min.js:261
yc @ react-dom.production.min.js:260
Kd @ react-dom.production.min.js:259
qd @ react-dom.production.min.js:283
Et @ react-dom.production.min.js:281
gc @ react-dom.production.min.js:270
S @ scheduler.production.min.js:13
dn @ scheduler.production.min.js:14
localhost/:1 Unchecked runtime.lastError: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received
localhost/:1 Unchecked runtime.lastError: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received
```

---

## 136. EDGE_FUNCTION_INVOCATION_FAILED when deploying an hydrogen application in Vercel
**Score:** 3 | **Tags:** reactjs, vercel, hydrogen, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/75776829/edge-function-invocation-failed-when-deploying-an-hydrogen-application-in-vercel

When I am deploying my Hydrogen based Shopify application into Vercel. I am getting this error
EDGE\_FUNCTION\_INVOCATION\_FAILED

when seeing on logs it tells this.

![1](https://i.sstatic.net/BUPy5.png)

---

## 137. Can Tailwind CSS work with dynamic Shopify liquid variables?
**Score:** 2 | **Tags:** tailwind-css, shopify, liquid, tailwind-css-4, shopify-liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/79603522/can-tailwind-css-work-with-dynamic-shopify-liquid-variables

I'm relatively new to Tailwind and using it with a custom Shopify theme. I installed Tailwind using the Tailwind CLI, and all static classes work fine.

However, I'm having trouble when trying to use **Liquid variables inside Tailwind utility classes**. I understand that Tailwind compiles before Liquid runs, but I want to clarify whether there's a better way to handle this.

**The code that doesn't work, but what I am trying to achieve:**

```
<!-- I tried dynamically setting max-width with a liquid variable -->
<div class="max-w-[{{ settings.page_width }}px]">
  Content here
</div>
```

In the browser, this correctly renders as:

```
<div class="max-w-[1400px]">Content here</div>
```

…but Tailwind doesn’t apply the style because `max-w-[1400px]` wasn’t in the source when Tailwind compiled the CSS.

**What works instead:**

```
<style>
    :root {
        --page-width: {{ settings.page_width }} /* 1400px */
    }
    .page-width {
        max-width: var(--page-width);
    }
</style>


<div class="page-width">
  Content here
</div>
```

**My Question:**

Is there any way to get Tailwind to apply styles for class names that use dynamic Liquid values like `{{ settings.page_width }}` — **without** manually safelisting every possible value in `tailwind.config.js`?

Or would I need to use a mix of tailwind and a 'vanilla' css file to handle those variables?

Thanks in advance.

---

## 138. Product price calculations in Shopify Liquid
**Score:** 2 | **Tags:** shopify, shopify-liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/72362502/product-price-calculations-in-shopify-liquid

very new to Shopify Liquid and trying to navigate through the code.

I'm trying to replicate the discount that is appearing here: <https://theoodie.com/products/avocado-oodie>

I've setup a discount code and assigned it to a collection, I'm then retrieving it in my product template so I know how much to discount. I would like to strike-through the price and then display what the discounted amount will be once the coupon is applied. Trying to work out how I can write the discounted price out though...

Noticed that if I echo product.price, it shows in cents. I've figured out I can divide it and then minus my discount, like below...

```
 {{ product.price | divided_by: 100 | minus: 20 }}
```

but the formatting is lacking, no decimal places, and no currency. Is there a particular function/class? that I can run to output the price minus my discount in the same format as the standard product price?

Further to this, how would I strike-through the standard price if I have a discount? I plan to put a little notation like the example website to say this is the price once coupon added.

Cheers!

---

## 139. Shopify Products API skipping items in pagination
**Score:** 2 | **Tags:** shopify, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/65947095/shopify-products-api-skipping-items-in-pagination

I am trying to create a paginated shopify products page. I'm using the `since_id` strategy laid out in their docs: <https://shopify.dev/docs/admin-api/rest/reference/products/product#index-2020-10>

Using this endpoint, as explained in the docs:

`/products.json?limit=5&since_id=${sinceId}`

sinceId being the id of the last product on the previous page

**The pagination seems to skip items.** And it doesn't seem to be a set number of products that it skips. Sometimes it is just one. Others it can be up to 10.

Obviously, that makes the "pagination" not work.

I am aware of the link in the header solution. But wanted to know if anyone has experienced this issue with `since_id`?

---

## 140. How to update Shop Metafields using GraphQL in Shopify
**Score:** 2 | **Tags:** graphql, shopify, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/68379403/how-to-update-shop-metafields-using-graphql-in-shopify

How can I create/update a shop metafield using GraphQL in shopify?
I could easily create a collection metafield using the following:

```
mutation {
  collectionUpdate(
    input: {
      id: "gid"
      metafields: [
        {
          namespace: "testNamespace"
          key: "testKey"
          value: "someValue2"
          valueType: STRING
        }
        {
          id: "gid"
          value: "value"
        }
      ]
    }
  ) {
    collection {
      id
      metafields(first: 10) {
        edges {
          node {
            id
            value
          }
        }
      }
    }
    userErrors {
        field
        message
      }
  }
}
```

But there seems to be no equivalent for the shop.
Also, a shop metafield can be retrieved using:

```
{
  shop {
    metafield(namespace:"namespace",key:"key") {
          id
          value
        }
  }
}
```

---

## 141. Can&#39;t Get Product Metafields using StoreFront GraphQL API
**Score:** 2 | **Tags:** graphql, shopify, e-commerce, shopify-api, shopify-storefront-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/64794400/cant-get-product-metafields-using-storefront-graphql-api

I am using storefront API for my Shopify store and need to retrieve product metafields for my product.

I already added metafields using 3rd party app ([Metafields Guru](https://apps.shopify.com/metafields-editor-2)).

I need to get all those metafields for product, and had been following this article.
<https://shopify.dev/tutorials/retrieve-metafields-with-storefront-api>

```
{
  productByHandle(handle: "xxx-handle") {
    id
    title
    handle
    productType
    metafields(first: 5) {
      edges {
        node {
          key
          value
        }
      }
    }
  }
}
```

But I get an empty array for metafields. Not sure what I am missing here.

Any help would be appreciated!

---

## 142. Shopify API Node: AdminAPI vs StoreFrontAPI Queries
**Score:** 2 | **Tags:** shopify, shopify-api, shopify-api-node | **Answered:** True
**Link:** https://stackoverflow.com/questions/65460310/shopify-api-node-adminapi-vs-storefrontapi-queries

I am trying to make a graphql request to shopify's admin api. I am using the official shopify-api-node library.

My query is as follows

```
      const response = await shopify.graphql({
      `order(id:"gid://shopify/Order/3138432598213") {
        currentCartDiscountAmountSet {
          shopMoney {
            amount
            currencyCode
          }
        }
      }`
    });
```

And the response is

[![enter image description here](https://i.sstatic.net/NaYGy.png)](https://i.sstatic.net/NaYGy.png)

From my understanding, this should return an object with a data field and an extensions field (I'm interested in query cost).

The response I get is simply contains order.

Is this because I'm querying storefront API? I'm confused because I want to query admin api. According to shopify docs, order under storefront API does not have the field currentCartDiscountAmountSet, whereas order under admin API does have this field. I am getting the correct order with the field currentCartDiscountAmountSet, and so I presume that I'm querying admin api. But then again, I'm not getting data and extensions?

My questions are:

1. When using shopify-api-node, how to I specify if I want to query admin or storefront API?
2. Why am I not getting data and extensions in my response? Is it actually because I'm querying storefront api? If so, then why am I successfully able to get currentCartDiscountAmountSet?

---

## 143. Get multiple transformedSrc from a variant image
**Score:** 2 | **Tags:** graphql, shopify, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/62686702/get-multiple-transformedsrc-from-a-variant-image

I have a query:

```
query {
 productByHandle(handle: "${productHandle}") {
   variants(first: 3) {
     edges {
       node {
         title
         id
         priceV2 {
           amount
         }
         image {
           transformedSrc(maxWidth: 400)
          }
        }
      }
    }
  }
}
```

Which works great. However, I'm struggling to find the syntax to get **multiple transformedSrcs** from the variant image. I want to use this for an image srcset, so I'll need to have multiple sizes returned.

I'm new to GraphQL in general. I tried an array on the image, using an `AND` with multiple maxWidth and scale, duplicating the image piece, etc. I've also searched the Shopify API docs many times.

Is this just not possible for some reason, or am I missing something?

---

## 144. Need to shorten the width of an embedded shopify buy button variant drop down that has long text
**Score:** 2 | **Tags:** html, css, shopify, shopify-api, buybutton.js | **Answered:** True
**Link:** https://stackoverflow.com/questions/77483866/need-to-shorten-the-width-of-an-embedded-shopify-buy-button-variant-drop-down-th

Essentially I have embedded buy buttons on a store page. Typically when products have variants the titles of these variants are just clothing size (S, M, L, XL, 2XL, etc) so the names of the variants are very short. I now have a product that has LONG variant names, and these longer names are stretching the width of the variant drop down. I instead need the width of the drop down with the LONG NAME variants, to be the exact same width as the drop down with the SHORT NAME variants. I can't figure this out... it seems as if no matter what new width styles I add to the embedded code, the long names are forcing the dropdown to still stay long... Maybe I'm just not adding the new width styles to the correct area within the embedded code?

Here is a JS fiddle showing what's happening - <https://jsfiddle.net/t7bdv601/4/>

And here is all of the code -

```
 <body>

   <div id="horizontalstorecontainer">
     <div class="store-scrolling-wrapper">

       <div class="clothingcard2">
         <div class="productwrapperclothing">
           <div class="animationwrapperclothing">
             <a href="/test">
               <img src="https://www.missingnewyork.com/images/glow-joker-hoodie-by-missing-store.jpg" alt="." class="clothing" />
             </a>
           </div>
           <div class="itemandpricewrapperclothing">
             <a href="/test">
               <h1>LONG NAME VARIANTS</h1>
             </a>
             <h2>$ 20.00</h2>
           </div>
         </div>
         <div id="bf3">
           <script type="text/javascript">
             /*<![CDATA[*/
             (function() {
               var scriptURL = 'https://sdks.shopifycdn.com/buy-button/latest/buy-button-storefront.min.js';
               if (window.ShopifyBuy) {
                 if (window.ShopifyBuy.UI) {
                   ShopifyBuyInit();
                 } else {
                   loadScript();
                 }
               } else {
                 loadScript();
               }

               function loadScript() {
                 var script = document.createElement('script');
                 script.async = true;
                 script.src = scriptURL;
                 (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(script);
                 script.onload = ShopifyBuyInit;
               }

               function ShopifyBuyInit() {
                 var client = ShopifyBuy.buildClient({
                   domain: 'missingnewyork.myshopify.com',
                   storefrontAccessToken: '8ad1e9d2d113621e1e9785f5a84b7330',
                 });
                 ShopifyBuy.UI.onReady(client).then(function(ui) {
                   ui.createComponent('product', {
                     id: '7011046490178',
                     node: document.getElementById('bf3'),
                     moneyFormat: '%24%7B%7Bamount%7D%7D',
                     options: {
                       "product": {
                         "styles": {
                           "product": {
                             "@media (min-width: 601px)": {
                               "max-width": "20px",
                               "margin-left": "20px",
                               "margin-bottom": "50px"
                             }
                           },
                           "button": {
                             "padding-left": "0px",
                             "padding-right": "0px",
                             "width": "60%",
                             "font-weight": "bold",
                             "color": "#000000",
                             ":hover": {
                               "color": "#000000",
                               "background-color": "#e6e6e6"
                             },
                             "background-color": "#ffffff",
                             ":focus": {
                               "background-color": "#e6e6e6"
                             },
                             "border-radius": "5px"
                           }
                         },
                         "contents": {
                           "img": false,
                           "title": false,
                           "price": false
                         },
                         "text": {
                           "outOfStock": "SOLD OUT"
                         },
                       },
                       "productSet": {
                         "styles": {
                           "products": {
                             "@media (min-width: 601px)": {
                               "margin-left": "-20px"
                             }
                           }
                         }
                       },
                       "modalProduct": {
                         "contents": {
                           "img": false,
                           "imgWithCarousel": true,
                           "button": false,
                           "buttonWithQuantity": true
                         },
                         "styles": {
                           "product": {
                             "@media (min-width: 601px)": {
                               "max-width": "20px",
                               "margin-left": "0px",
                               "margin-bottom": "0px"
                             }
                           },
                           "button": {
                             "font-weight": "bold",
                             "color": "#000000",
                             ":hover": {
                               "color": "#000000",
                               "background-color": "#e6e6e6"
                             },
                             "background-color": "#ffffff",
                             ":focus": {
                               "background-color": "#e6e6e6"
                             },
                             "border-radius": "5px"
                           }
                         },
                         "text": {
                           "button": "ADD TO CART"
                         }
                       },
                       "cart": {
                         "styles": {
                           "button": {
                             "font-weight": "bold",
                             "color": "#000000",
                             ":hover": {
                               "color": "#000000",
                               "background-color": "#e6e6e6"
                             },
                             "background-color": "#ffffff",
                             ":focus": {
                               "background-color": "#e6e6e6"
                             },
                             "border-radius": "5px"
                           },
                           "title": {
                             "color": "#ffffff"
                           },
                           "header": {
                             "color": "#ffffff"
                           },
                           "lineItems": {
                             "color": "#ffffff"
                           },
                           "subtotalText": {
                             "color": "#ffffff"
                           },
                           "subtotal": {
                             "color": "#ffffff"
                           },
                           "notice": {
                             "color": "#ffffff"
                           },
                           "currency": {
                             "color": "#ffffff"
                           },
                           "close": {
                             "color": "#ffffff",
                             ":hover": {
                               "color": "#ffffff"
                             }
                           },
                           "empty": {
                             "color": "#ffffff"
                           },
                           "noteDescription": {
                             "color": "#ffffff"
                           },
                           "discountText": {
                             "color": "#ffffff"
                           },
                           "discountIcon": {
                             "fill": "#ffffff"
                           },
                           "discountAmount": {
                             "color": "#ffffff"
                           },
                           "cart": {
                             "background-color": "#000000"
                           },
                           "footer": {
                             "background-color": "#000000"
                           }
                         },
                         "text": {
                           "title": "CART",
                           "empty": "YOUR CART IS EMPTY.",
                           "notice": "Shipping and taxes are added at checkout.",
                         }
                       },
                       "toggle": {
                         "styles": {
                           "toggle": {
                             "font-weight": "bold",
                             "background-color": "#ffffff",
                             ":hover": {
                               "background-color": "#e6e6e6"
                             },
                             ":focus": {
                               "background-color": "#e6e6e6"
                             }
                           },
                           "count": {
                             "color": "#000000",
                             ":hover": {
                               "color": "#000000"
                             }
                           },
                           "iconPath": {
                             "fill": "#000000"
                           }
                         }
                       },
                       "lineItem": {
                         "styles": {
                           "variantTitle": {
                             "color": "#ffffff"
                           },
                           "title": {
                             "color": "#ffffff"
                           },
                           "price": {
                             "color": "#ffffff"
                           },
                           "fullPrice": {
                             "color": "#ffffff"
                           },
                           "discount": {
                             "color": "#ffffff"
                           },
                           "discountIcon": {
                             "fill": "#ffffff"
                           },
                           "quantity": {
                             "color": "#ffffff"
                           },
                           "quantityIncrement": {
                             "color": "#ffffff",
                             "border-color": "#ffffff"
                           },
                           "quantityDecrement": {
                             "color": "#ffffff",
                             "border-color": "#ffffff"
                           },
                           "quantityInput": {
                             "color": "#ffffff",
                             "border-color": "#ffffff"
                           }
                         }
                       }
                     },
                   });
                 });
               }
             })();
             /*]]>*/

           </script>
         </div>
       </div>

       <div class="clothingcard2">
         <div class="productwrapperclothing">
           <div class="animationwrapperclothing">
             <a href="/test">
               <img src="https://www.missingnewyork.com/images/glow-joker-hoodie-by-missing-store.jpg" alt="." class="clothing" />
             </a>
           </div>
           <div class="itemandpricewrapperclothing">
             <a href="/test">
               <h1>SHORT NAME VARIANTS</h1>
             </a>
             <h2>$ 20.00</h2>
           </div>
         </div>
         <div id="gjh">
           <script type="text/javascript">
             /*<![CDATA[*/
             (function() {
               var scriptURL = 'https://sdks.shopifycdn.com/buy-button/latest/buy-button-storefront.min.js';
               if (window.ShopifyBuy) {
                 if (window.ShopifyBuy.UI) {
                   ShopifyBuyInit();
                 } else {
                   loadScript();
                 }
               } else {
                 loadScript();
               }

               function loadScript() {
                 var script = document.createElement('script');
                 script.async = true;
                 script.src = scriptURL;
                 (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(script);
                 script.onload = ShopifyBuyInit;
               }

               function ShopifyBuyInit() {
                 var client = ShopifyBuy.buildClient({
                   domain: 'missingnewyork.myshopify.com',
                   storefrontAccessToken: '8ad1e9d2d113621e1e9785f5a84b7330',
                 });
                 ShopifyBuy.UI.onReady(client).then(function(ui) {
                   ui.createComponent('product', {
                     id: '6969282134082',
                     node: document.getElementById('gjh'),
                     moneyFormat: '%24%7B%7Bamount%7D%7D',
                     options: {

                       "option": {
                         "styles": {
                           "wrapper": {
                             "border": "0px",
                             "border-radius": "5px",
                             "position": "absolute",
                             "height": "42px",
                             "bottom": "0px",
                             "width": "100px",
                             "padding": "3px"

                           }
                         }
                       },

                       "product": {
                         "styles": {
                           "buttonWrapper": {
                             "margin-left": "40%"
                           },
                           "product": {
                             "@media (min-width: 601px)": {
                               "max-width": "calc(25% - 20px)",
                               "margin-left": "20px",
                               "margin-bottom": "0px"
                             }
                           },
                           "button": {
                             "padding-left": "0px",
                             "padding-right": "0px",
                             "width": "100%",
                             "right": "0",
                             "font-weight": "bold",
                             "color": "#000000",
                             ":hover": {
                               "color": "#000000",
                               "background-color": "#e6e6e6"
                             },
                             "background-color": "#ffffff",
                             ":focus": {
                               "background-color": "#e6e6e6"
                             },
                             "border-radius": "5px"
                           },
                         },
                         "option": {
                           "display": "inline-block",
                           "width": "20px",
                         },
                         "contents": {
                           "img": false,
                           "title": false,
                           "price": false
                         },
                         "text": {
                           "outOfStock": "SOLD OUT"
                         },
                       },
                       "productSet": {
                         "styles": {
                           "products": {
                             "@media (min-width: 601px)": {
                               "margin-left": "-20px"
                             }
                           }
                         }
                       },
                       "modalProduct": {
                         "contents": {
                           "img": false,
                           "imgWithCarousel": true,
                           "button": false,
                           "buttonWithQuantity": true
                         },
                         "styles": {
                           "product": {
                             "@media (min-width: 601px)": {
                               "max-width": "100%",
                               "margin-left": "0px",
                               "margin-bottom": "0px"
                             }
                           },
                           "button": {
                             "font-weight": "bold",
                             "color": "#000000",
                             ":hover": {
                               "color": "#000000",
                               "background-color": "#e6e6e6"
                             },
                             "background-color": "#ffffff",
                             ":focus": {
                               "background-color": "#e6e6e6"
                             },
                             "border-radius": "5px"
                           }
                         },
                         "text": {
                           "button": "ADD TO CART"
                         }
                       },
                       "cart": {
                         "styles": {
                           "button": {
                             "font-weight": "bold",
                             "color": "#000000",
                             ":hover": {
                               "color": "#000000",
                               "background-color": "#e6e6e6"
                             },
                             "background-color": "#ffffff",
                             ":focus": {
                               "background-color": "#e6e6e6"
                             },
                             "border-radius": "5px"
                           },
                           "title": {
                             "color": "#ffffff"
                           },
                           "header": {
                             "color": "#ffffff"
                           },
                           "lineItems": {
                             "color": "#ffffff"
                           },
                           "subtotalText": {
                             "color": "#ffffff"
                           },
                           "subtotal": {
                             "color": "#ffffff"
                           },
                           "notice": {
                             "color": "#ffffff"
                           },
                           "currency": {
                             "color": "#ffffff"
                           },
                           "close": {
                             "color": "#ffffff",
                             ":hover": {
                               "color": "#ffffff"
                             }
                           },
                           "empty": {
                             "color": "#ffffff"
                           },
                           "noteDescription": {
                             "color": "#ffffff"
                           },
                           "discountText": {
                             "color": "#ffffff"
                           },
                           "discountIcon": {
                             "fill": "#ffffff"
                           },
                           "discountAmount": {
                             "color": "#ffffff"
                           },
                           "cart": {
                             "background-color": "#000000"
                           },
                           "footer": {
                             "background-color": "#000000"
                           }
                         },
                         "text": {
                           "title": "CART",
                           "empty": "YOUR CART IS EMPTY.",
                           "notice": "Shipping and taxes are added at checkout.",
                         }
                       },
                       "toggle": {
                         "styles": {
                           "toggle": {
                             "font-weight": "bold",
                             "background-color": "#ffffff",
                             ":hover": {
                               "background-color": "#e6e6e6"
                             },
                             ":focus": {
                               "background-color": "#e6e6e6"
                             }
                           },
                           "count": {
                             "color": "#000000",
                             ":hover": {
                               "color": "#000000"
                             }
                           },
                           "iconPath": {
                             "fill": "#000000"
                           }
                         }
                       },
                       "lineItem": {
                         "styles": {
                           "variantTitle": {
                             "color": "#ffffff"
                           },
                           "title": {
                             "color": "#ffffff"
                           },
                           "price": {
                             "color": "#ffffff"
                           },
                           "fullPrice": {
                             "color": "#ffffff"
                           },
                           "discount": {
                             "color": "#ffffff"
                           },
                           "discountIcon": {
                             "fill": "#ffffff"
                           },
                           "quantity": {
                             "color": "#ffffff"
                           },
                           "quantityIncrement": {
                             "color": "#ffffff",
                             "border-color": "#ffffff"
                           },
                           "quantityDecrement": {
                             "color": "#ffffff",
                             "border-color": "#ffffff"
                           },
                           "quantityInput": {
                             "color": "#ffffff",
                             "border-color": "#ffffff"
                           }
                         }
                       }
                     },
                   });
                 });
               }
             })();
             /*]]>*/

           </script>
         </div>
       </div>

     </div>
   </div>

 </body>
```

And the CSS -

```
body {
  background: black !important;
}

::-webkit-scrollbar {
  height: .88vh;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: white;
}

::-webkit-scrollbar-thumb:hover {
  background: #ffffff;
}

#horizontalstorecontainer {
  z-index: 0;
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
}

.store-scrolling-wrapper {
  overflow-x: auto;
  overflow-y: hidden;
  white-space: nowrap;
  text-align: center;
  margin: 0 auto;
  height: 100%;
  width: 100%;
  -webkit-overflow-scrolling: touch;
  -ms-overflow-style: none;
}

.clothingcard2 {
  display: inline-block;
  position: relative;
  height: 60%;
  width: 35%;
  top: 50.6%;
  transform: translateY(-50%);
}

.clothingcard2 img {
  height: 100%;
}

.productwrapperclothing {
  top: 0;
  width: 100%;
  display: inline-block;
  height: calc(100% - 42px);
}

#bf3,
#gjh {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  margin: 0 auto;
}

.animationwrapperclothing {
  height: calc(100% - 66.4px);
  -webkit-perspective: 2000px;
  -moz-perspective: 2000px;
  -ms-perspective: 2000px;
  -o-perspective: 2000px;
  perspective: 2000px;
  display: flex;
  justify-content: flex-end;
  flex-direction: column;
}

.clothing {
  margin: 0 auto;
  position: relative;
  height: 100%;
  width: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  bottom: 0;
  -moz-user-select: -moz-none;
  -khtml-user-select: none;
  -webkit-user-select: none;
  -ms-user-select: none;
  user-select: none;
  outline: 1px solid transparent;
}

.animationwrapperclothing>a {
  height: 100%;
  display: flex;
  justify-content: flex-end;
  flex-direction: column;
}

.itemandpricewrapperclothing {
  position: fixed;
  width: 100%;
  bottom: 42px;
  margin: 0 auto;
  right: 0;
  left: 0;
}

.itemandpricewrapperclothing>a {
  display: inline-block;
  list-style: none;
  text-decoration: none;
}

h1 {
  font-family: neue-haas-grotesk-text, sans-serif;
  color: white;
  font-weight: 500;
  font-style: normal;
  list-style: none;
  text-align: center;
  text-decoration: none;
  font-size: 13px;
}

h2 {
  font-family: neue-haas-grotesk-text, sans-serif;
  color: #7e7e7e;
  font-weight: 500;
  font-style: normal;
  list-style: none;
  text-align: center;
  text-decoration: none;
  font-size: 12px;
  margin-top: -4px;
}



@media screen and (orientation: portrait) {

  .clothingcard2 {
    width: 100%;
    margin-left: 0;
    margin-right: 0;
    padding-right: 0;
  }

  .clothingcard2 img {
    max-width: 95%;
    max-height: 100%;
    height: auto;
    width: auto;
  }

  .productwrapperclothing {
    padding: 0;
  }
}
```

Please note that I have changed the 'max-width' inside of the embedded code for the LONG NAME VARIANT product to something extremely small (just 20px) instead of what the SHORT NAME VARIANT width is set at (which is 'calc(25% - 20px)')...yet it is still not changing the width of the LONG NAME VARIANT dropdown at all... I don't want it to be 20px anyway, I need it to be the exact same width as the SHORT NAME variant product, but I have just changed it to 20px to test trying to find where I can actually alter the width of the dropdown but I can't seem to get it to be shorter at all...

And to clarify, I understand that the text would be getting cut off when the width of the LONG NAME VARIANT drop down is as short as the SHORT NAME VARIANT drop down... this is okay. I still need the LONG NAME VARIANT dropdown to be the same width as the SHORT NAME VARIANT dropdown but only *before* it is clicked on ... and then *after* the dropdown is clicked on I need it to resize so that the text is NOT cut off.

EDIT - I really need these changes to be implemented directly in the embedded buy button, *not* in the CSS... Unless there is a way where the styles can be changed in the CSS without affecting all the other buy buttons on the webstore too. These new styles should *only* affect the product that has the LONG variant names. The styling for all of the other buy buttons on the page need to stay exactly the same as the SHORT variant name product on the JSFiddle (in the JSFiddle I only have 1 other product shown for simplicity, but on the actual store page there are 20+ other products).

---

## 145. How Do I Get MetaObject Values On Single MetaObject Page In Shopify
**Score:** 2 | **Tags:** shopify, liquid, shopify-api, shopify-template, metaobject | **Answered:** True
**Link:** https://stackoverflow.com/questions/75492491/how-do-i-get-metaobject-values-on-single-metaobject-page-in-shopify

I am using metaObjects in shopify. I have created a metaObject name "Projects" . I created a page "Projects" to display those saved projects through liquid code. It is working as per the requirement on Projects page but now i want to display each project detail on single page. How do i approach this ? Like should i create a page and set a template on it and in that template , fetch the metaobject handle to display its details . I am facing issue like how do i call the same single page for all projects details and display its details. Can someone please guide what is the possible way to get each metaObject values on single project page .

Thanks

---

## 146. Fetch shopify products based on product tags
**Score:** 2 | **Tags:** graphql, shopify, product, shopify-app, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/73063005/fetch-shopify-products-based-on-product-tags

I am working on fetching Shopify products based on the product tag. I did the below code for it and it's working fine when I put the `AND` condition, But it douses not work with the `OR` condition. It shows products where a tag appears in text content.

[![enter image description here](https://i.sstatic.net/RHQot.png)](https://i.sstatic.net/RHQot.png)

---

## 147. Calculate Gross Sales using Shopify API
**Score:** 2 | **Tags:** shopify, shopify-app, shopify-api, shopify-api-node | **Answered:** True
**Link:** https://stackoverflow.com/questions/63031868/calculate-gross-sales-using-shopify-api

I want to calculate Gross Sales using Shopify API. I have already readed the shopify API documentation and tried the formula they used to calculate gross sales and failed to get the same result they have at the shopify reports website.

I used this shopify endpoint to retrieve all orders

```
/admin/api/2020-07/orders.json?status=any&created_at_min=2020-07-03T00:00:00-04:00&created_at_max=2020-07-04T00:00:00-04:00&limit=250
```

PS: The number of orders from shopify API and shopify Dashboard is equal. ( I am getting all the orders correctly)

I tried to use the sum of total\_line\_items\_price, but I got a different result from Shopify Reports.   
Shopify API results after summing the total\_line\_items\_price: **X**   
Also, I tried to use the formula they provided at Shopify API documentation where they mentioned that **Gross Sales = product selling price x ordered quantity** and I got the same result as sum of the total\_line\_items\_price: **X**   
Shopify Gross Sales at the financial report dashboard: **Y**   
Shopify API sum of total\_tax: Z Which is equal to the financial report taxes.   
Please I need your help to calculate Gross Sales Correctly

Thank you

---

## 148. After creating a product how can I publish it to the online store in shopify?
**Score:** 2 | **Tags:** shopify, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/77492777/after-creating-a-product-how-can-i-publish-it-to-the-online-store-in-shopify

I'm creating new product using the **productCreate** mutation. Now I want to publish it to my online store.

To do that I'm querying the list of publications using the **[publications](https://shopify.dev/docs/api/admin-graphql/unstable/queries/publications)** query but the challenge I'm facing is to determine which publication id belongs to the online store? Previously they had a "name" property which is now deprecated.

Once I become certain that this id belongs to the online store then I can publish it using the **[publishablePublish](https://shopify.dev/docs/api/admin-graphql/2023-10/mutations/publishablePublish)** mutation.

Also how can I set the inventory quantity of a newly created product?

Thanks!

---

## 149. Shopify API (using Python): File upload failed due to &quot;Processing Error.&quot; Why?
**Score:** 2 | **Tags:** python, python-requests, graphql, shopify, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/76392943/shopify-api-using-python-file-upload-failed-due-to-processing-error-why

I am struggling to figure out why I'm not able to successfully upload images to the Files section of my Shopify store. I followed this code here, except mine is a Python version of this: <https://gist.github.com/celsowhite/2e890966620bc781829b5be442bea159>

```
import requests
import os

# Set up Shopify API credentials
shopify_store = 'url-goes-here.myshopify.com' // the actual URL is here
access_token = 'token-goes-here' // the actual token is here

# Read the image file
image_path = r'C:\the-actual-filepath-is-here\API-TEST-1.jpg'  # Replace with the actual path to your image file
with open(image_path, 'rb') as file:
    image_data = file.read()

# Create staged upload
staged_upload_url = f"https://{shopify_store}/admin/api/2023-04/graphql.json"
staged_upload_query = '''
mutation stagedUploadsCreate($input: [StagedUploadInput!]!) {
  stagedUploadsCreate(input: $input) {
    stagedTargets {
      resourceUrl
      url
      parameters {
        name
        value
      }
    }
    userErrors {
      field
      message
    }
  }
}
'''
staged_upload_variables = {
    "input": [
        {
            "filename": "API-TEST-1.jpg",
            "httpMethod": "POST",
            "mimeType": "image/jpeg",
            "resource": "FILE"
        }
    ]
}

response = requests.post(
    staged_upload_url,
    json={"query": staged_upload_query, "variables": staged_upload_variables},
    headers={"X-Shopify-Access-Token": access_token}
)

data = response.json()
staged_targets = data['data']['stagedUploadsCreate']['stagedTargets']
target = staged_targets[0]
params = target['parameters']
url = target['url']
resource_url = target['resourceUrl']

# Post image data to the staged target
form_data = {
    "file": image_data
}
headers = {
    param['name']: param['value'] for param in params  # Fix the headers assignment
}
headers["Content-Length"] = str(len(image_data))

response = requests.post(url, files=form_data, headers=headers)  # Use 'files' parameter instead of 'data'

# Create the file in Shopify using the resource URL
create_file_url = f"https://{shopify_store}/admin/api/2023-04/graphql.json"
create_file_query = '''
mutation fileCreate($files: [FileCreateInput!]!) {
  fileCreate(files: $files) {
    files {
      alt
    }
    userErrors {
      field
      message
    }
  }
}
'''
create_file_variables = {
    "files": [
        {
            "alt": "alt-tag",
            "contentType": "IMAGE",
            "originalSource": resource_url
        }
    ]
}

response = requests.post(
    create_file_url,
    json={"query": create_file_query, "variables": create_file_variables},
    headers={"X-Shopify-Access-Token": access_token}
)

data = response.json()
files = data['data']['fileCreate']['files']
alt = files[0]['alt']
```

It runs the code, it doesn't output any errors. However when I navigate to the Files section of the Shopify store, it says "1 upload failed -- processing error."

Any clues in the code as to what might be causing that?

Also when I print(data) at the very end, this is what it says:

{'data': {'fileCreate': {'files': [{'alt': 'alt-tag'}], 'userErrors': []}}, 'extensions': {'cost': {'requestedQueryCost': 20, 'actualQueryCost': 20, 'throttleStatus': {'maximumAvailable': 1000.0, 'currentlyAvailable': 980, 'restoreRate': 50.0}}}}

Seeming to indicate it created it successfully. But there's some misc processing error.

Thanks

---

## 150. How to avoid Shopify app opening in a new tab?
**Score:** 2 | **Tags:** shopify, shopify-app, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/75385725/how-to-avoid-shopify-app-opening-in-a-new-tab

### THE SITUATION:

I am testing my Shopify app.   
Until few days ago it was working fine.   
The intended behavior was it to be opened embedded in Shopify dashboard.

Recently when I click on the app it opens in a new tab at the following url:

```
https://[STORE-ID].myshopify.com/admin/apps/[APP-NAME]?force_legacy_domain=1
```

Note the `force_legacy_domain` param added to the url.

### SHOPIFY DOMAIN CHANGE

It seems there have been some changes in the Shopify admin url.   
With the new change it should be opened at the following url:

```
https://admin.shopify.com/store/[STORE-NAME]/apps/[APP-NAME]
```

### QUESTION:

How can I avoid opening the app in a new tab?

---

## 151. Shopify Admin API: How To Get Correct Prices For Discounted Order?
**Score:** 2 | **Tags:** graphql, shopify, shopify-api | **Answered:** True
**Link:** https://stackoverflow.com/questions/73699390/shopify-admin-api-how-to-get-correct-prices-for-discounted-order

I am building an integration between Shopify and our ERP via the admin API using GraphQL. All is working well except when I try and get the exact prices for an order.

In the documentation **discountedTotalSet** should be '*The total line price after discounts are applied*' but I am finding it returns the full price - see examples below.

Can anyone give me guidance on how to get the API to show the same prices that are on the order? I need this to match exactly line by line. This is the query I am using for the order:

```
{
  node(id: "gid://shopify/Order/4866288156908") {
    id
    ...on Order {
      name
      lineItems (first: 50) {
        edges {
          node {
            id
            quantity
            sku
            discountedTotalSet {
              shopMoney {
                currencyCode
                amount
              }
            }
          }
        }
      }
    }
  }
}
```

And this is the result, note amount says 599.00 but that is not correct, see screenshot for the same order from the UI.

```
{
  "data": {
    "node": {
      "id": "gid://shopify/Order/4866288156908",
      "name": "AK-1003",
      "lineItems": {
        "edges": [
          {
            "node": {
              "id": "gid://shopify/LineItem/12356850286828",
              "quantity": 1,
              "sku": "AK-A1081",
              "discountedTotalSet": {
                "shopMoney": {
                  "currencyCode": "AUD",
                  "amount": "599.0"
                }
              }
            }
          }
        ]
      }
    }
  },
```

[Shopify UI screenshot*emphasized text*](https://i.sstatic.net/3Hhu7.png)

---

## 152. Upload file (image) from local machine using shopify-api-node
**Score:** 2 | **Tags:** node.js, shopify, shopify-app, shopify-api, shopify-api-node | **Answered:** True
**Link:** https://stackoverflow.com/questions/70944562/upload-file-image-from-local-machine-using-shopify-api-node

I am trying to upload local images to a Shopify product via [node.js](https://nodejs.org/) and [shopify-api-node](https://github.com/MONEI/Shopify-api-node).

This is the part of the code, where I am uploading the images.

```
product.images.forEach(async image => {
  Logger.toFile("product.image", image);
  try {
    await this._api.productImage.create(shopifyProduct.id, {
      src: image.src
    });
  } catch (error) {
    Logger.error("Error uploading images.");
    this._handleErrors(error);
  }
})
```

If I use an external URL for `image.src`, everything works just fine.

Here is the logger with working external URL:

```
[2022-02-01 16:44:38 UTC][Products] product.image {
  src: 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/220px-Image_created_with_a_mobile_phone.png',
  position: 1
}
```

And the not working local src:

```
product.image {
  src: '/Users/radoslav/Server/projects/tmp/pics/264-426.png',
  position: 1
}
```

The path is correct and the image `264-426.png` exists.

Any suggestions, what I am doing wrong, or is it possible to upload an image to Shopify from a local link?

---

## 153. &#39;Cannot redefine property: __internal__deprecationWarning&#39; in a Shopify Hydrogen project
**Score:** 2 | **Tags:** reactjs, typescript, shopify-hydrogen | **Answered:** True
**Link:** https://stackoverflow.com/questions/77048923/cannot-redefine-property-internal-deprecationwarning-in-a-shopify-hydrogen

I'm buildling a Shopify Hydrogen project with Remix and Typescript and all of a sudden I keep encountering the following error when I run `npm run dev`. It was working fine 5 hours prior, come back from dinner and now app does not launch.

```
╭─ error ───────────────────────────────────────────────────────────────────────╮
│                                                                               │
│  Cannot redefine property: __internal__deprecationWarning                     │
│                                                                               │
│  To investigate the issue, examine this stack trace:                          │
│    at defineProperty                                                          │
│    at <anonymous> (@babel/types/lib/index.js:66)                              │
│      Object.defineProperty(exports, "__internal__deprecationWarning", {       │
│    at _compile (node:internal/modules/cjs/loader:1241)                        │
│    at js (node:internal/modules/cjs/loader:1295)                              │
│    at load (node:internal/modules/cjs/loader:1091)                            │
│    at _load (node:internal/modules/cjs/loader:938)                            │
│    at require (node:internal/modules/cjs/loader:1115)                         │
│    at require (node:internal/modules/helpers:130)                             │
│    at <anonymous> (@babel/types/src/builders/validateNode.ts:3)               │
│      import { BUILDER_KEYS } from "../index.ts";                              │
│    at _compile (node:internal/modules/cjs/loader:1241)                        │
│                                                                               │
╰───────────────────────────────────────────────────────────────────────────────╯

TypeError: Cannot redefine property: __internal__deprecationWarning
    at Function.defineProperty (<anonymous>)
    at Object.<anonymous> (/projectFolder projectFolder/node_modules/@babel/types/lib/index.js:66:8)
    at Module._compile (node:internal/modules/cjs/loader:1241:14)
    at Module._extensions..js (node:internal/modules/cjs/loader:1295:10)
    at Module.load (node:internal/modules/cjs/loader:1091:32)
    at Module._load (node:internal/modules/cjs/loader:938:12)
    at Module.require (node:internal/modules/cjs/loader:1115:19)
    at require (node:internal/modules/helpers:130:18)
    at Object.<anonymous> (/projectFolder folder/jmlshopifystore/node_modules/@babel/types/lib/builders/validateNode.js:8:14)
    at Module._compile (node:internal/modules/cjs/loader:1241:14)
```

* Reverted to an several earlier commits — no luck. Doesn't seem to matter which branch or commit.
* Added babel/core and babel/types as dev dependencies in order to get latest versions of possible packages.
* Deleted node\_modules and package-lock.json and reinstalled every step of the way; even cleared cache.
* Tried updating all dependencies one by one with node\_modules and package-lock.json reinstalls; no luck.

Any help would be greatly appreciated.

UPDATE: I went from Node v20.6.0 down to v20.5.1 and it worked again!

---

## 154. Not able to generate public api token in judge.me shopify
**Score:** 2 | **Tags:** shopify, remix.run, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/77415027/not-able-to-generate-public-api-token-in-judge-me-shopify

I have built website using [hydrogen shopify framework](https://hydrogen.shopify.dev/) and I want to integrate reviews using [judge.me](https://judge.me/) app. I am using this [npm package](https://www.npmjs.com/package/@judgeme/shopify-hydrogen/v/2.0.0) to integrate.

It require public api token, which I am trying to generate by clicking on `show` but it is throwing an error "Something went wront, please try again"

I am currently using free version, is it because of this?

[![enter image description here](https://i.sstatic.net/6Jrjo.jpg)](https://i.sstatic.net/6Jrjo.jpg)

---

## 155. How to polyfill Shopify Hydrogen (Remix) with node modules?
**Score:** 2 | **Tags:** node.js, reactjs, remix.run, esbuild, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/75996934/how-to-polyfill-shopify-hydrogen-remix-with-node-modules

I am trying to use ReSVG-JS with Shopify Hydrogen but am encountering several issues.
At first I was building my project with `remix dev` and all was fine, however, after further integrating Shopify Hydrogen into my project I switched my `run dev` script to `npm run build:css && concurrently -g -r npm:dev:css \"shopify hydrogen dev\"`, basically building with Shopify Hydrogen now.

This is when things went sideways. I received the first error that `process` was not defined. After some research I was able to fix this by patching into the ESBuild config of Remix with [remix-esbuild-override](https://www.npmjs.com/package/remix-esbuild-override) and by [polyfilling (with this package)](https://www.npmjs.com/package/esbuild-plugin-polyfill-node) `process`. Except that this was not enough and I needed to also manually patch the polyfilling package to add `process.arch` and `process.platform` in order for ReSVG to be happy.

```
withEsbuildOverride((option, {isServer, isDev}) => {
  if (!isServer) return option;

  option.plugins = [
    ...(option.plugins ?? []),
    polyfillNode({
      globals: {
        process: true,
        buffer: true,
      },
    }),
  ];

  return option;
});
```

After that I encountered another error to do with `fs` and that there was no `existsSync`. I was able to fix this by importing into the file that imports ReSVG `installGlobals` from `@remix-run/node` and calling `installGlobals()`.

```
import {installGlobals} from '@remix-run/node';
installGlobals();
import {Resvg} from '@resvg/resvg-js';
```

Now I was thrown into another error:

```
TypeError: globalThis.XMLHttpRequest is not a constructor
    at checkTypeSupport (path\to\project\node_modules\rollup-plugin-node-polyfills\polyfills\http-lib\capability.js:20:11)
    at node_modules/rollup-plugin-node-polyfills/polyfills/http-lib/capability.js (path\to\project\node_modules\rollup-plugin-node-polyfills\polyfills\http-lib\capability.js:39:45)
    at path\to\project\dist\worker\index.js:14:59
    at node_modules/rollup-plugin-node-polyfills/polyfills/http-lib/request.js (path\to\project\node_modules\rollup-plugin-node-polyfills\polyfills\http-lib\request.js:1:1)
```

I tried using the polyfill package I was using and multiple others that integrate with ESBuild but sadly failed to do so.

I am completely at loss and was hoping to find someone who could help out maybe even with a completely different solution, since mine is basically beating it until it works...

Thanks!

---

## 156. Sorting Meta Objects By Date in liquid - Shopify
**Score:** 1 | **Tags:** liquid, liquid-template, shopify-liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/77817222/sorting-meta-objects-by-date-in-liquid-shopify

I'm trying to sort a meta object by date.

```
{% assign sorted_shows = shop.metaobjects.shows.values | sort: 'show.date' | reverse %}

{% for shows in sorted_shows %}
{{ shows.date }} <br>
{% endfor %}
```

These are the results I get:

2024-02-09

2025-01-10

2024-02-01

2024-01-26

2024-02-16

any ideas? I'm stumped

---

## 157. Liquid&#39;s concat filter not working on arrays from shopify metafields?
**Score:** 1 | **Tags:** shopify, liquid, shopify-template, shopify-liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/76617681/liquids-concat-filter-not-working-on-arrays-from-shopify-metafields

Liquid's `concat` filter works like a charm using it on self-created arrays or arrays from section settings. However, I cannot get it to work when using it on arrays from metafields of a shopify product.

I have two metafields on my products: One holding a list of products and one holding a list of product variants. The types of the metafields are `list.product_reference`
and `list.variant_reference`. I want to merge both lists:

```
{%- assign products = product.metafields.custom.fcv_products.value -%}
{%- assign variants = product.metafields.custom.fcv_variants.value -%}
{%- assign items = products | concat: variants -%}
```

However, `items` will be `null`. When outputting this expression in the console like this:

```
<script>console.log({{ products | concat: variants | json }})</script>
```

I get the following error: `Liquid error (sections/...): concat filter requires an array argument`

Both arrays contain elements. The following logs all work as expected:

```
{%- for variant in variants -%}
  <script>console.log({{ variant | json }}); // Prints variants from the list </script>
{%- endfor -%}
<script>console.log({{ products | json }}); // Prints an array with products </script>
<script>console.log({{ variants | json }}); // Prints an array with variants </script>
<script>console.log({{ items | json }}); // Prints null </script>
```

Prior to this solution using the metafields, I used something similar to the following, which worked perfectly fine:

```
{%- assign products = section.settings.products -%}
{%- assign variants_nested = products | map: "variants" -%}
{%- assign variants = "" | split: "" -%}
{%- for variants_list in variants_nested -%}
  {%- assign variants = variants | concat: variants_list %}
{%- endfor -%}
{%- assign items = products | concat: variants -%}
```

Because of changed requirements we have to switch to the metafields solution.

Any ideas?

---

## 158. How can I fill the gaps on the Shopify collection page when I hide or exclude products?
**Score:** 1 | **Tags:** javascript, shopify, liquid, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/78776934/how-can-i-fill-the-gaps-on-the-shopify-collection-page-when-i-hide-or-exclude-pr

The first page is not filled entirely, but it already created other pages after excluding/hidding particular taged products.

```
{% for product in collection.products %}
  {% if product.tags contains 'hideProd' %}{% continue %}{% endif %}
  <!-- your product grid item -->
{% endfor %}
```

Gaps should fill.

For example, if there are 100 products in a collection and the pagination is set to 5 pages (with 20 products per page), but 20 products are excluded or hidden, the pagination should adjust to display only 4 pages.

---

## 159. Section not hidden before css/javascript transition
**Score:** 1 | **Tags:** javascript, html, jquery, css, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/78587063/section-not-hidden-before-css-javascript-transition

I'm quite new to css/javascript/shopify liquid but I'm trying to bug fix a section of text that animates in when you scroll. At the moment as you scroll slowly the section can be seen before scrolling further when it will disappear and then the transition will happen correctly.

Below is my js code:

```
$(document).ready(function() {
  var reapplyAnimation = function(element, animationClass) {
    // Remove the class to reset the animation
    $(element).removeClass(animationClass);
    setTimeout(function() {
      // Re-add the class to trigger the animation
      $(element).addClass(animationClass);
    }, 50); // A slight delay ensures the class change is recognized
  };

  $('.blob').each(function() {
    var blobElement = this;
    new Waypoint({
      element: blobElement,
      handler: function(direction) {
        if (direction === 'down') {
          // Apply animations to the blob and image as before
          reapplyAnimation(blobElement, 'animated-fade-rotate');
          var relatedImage = $(blobElement).closest('.custom-image-text-section').find('.image-container img')[0];
          reapplyAnimation(relatedImage, 'animated-slide-rotate');

          // Now also target the text container for its animation
          var textContainer = $(blobElement).closest('.custom-image-text-section').find('#text-container')[0];
          reapplyAnimation(textContainer, 'animated-fade-in-slide-in-right');
        }
      },
      offset: '75%' // Trigger point
    });
  });
});
```

I'm able to set the opacity of the section to 0 in the css but I need a way for this script to then override that opacity and transition it to 1 over the course of the animation. Below is the keyframes animation that as far as I can see should be able to change the opacity but it doesn't.

```
@keyframes fadeInSlideInRight {
    from {
        opacity: 0;
        transform: translateX(50%); /* Start from the right */
    }
    to {
        opacity: 1;
        transform: translateX(0); /* Slide to its original position */
    }
}

.animated-fade-in-slide-in-right {
  animation: fadeInSlideInRight 800ms ease-out forwards;
}
```

Please forgive me if I haven't answered the question very well ,I'm only just getting used to the languages!

---

## 160. Shopify - Product With Multiple Variants, If One Of Them Is Sold Out Everything Else Is Sold Out Too
**Score:** 1 | **Tags:** shopify, liquid, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/78311112/shopify-product-with-multiple-variants-if-one-of-them-is-sold-out-everything

In my store I have a product that has the following variants: color, size and length.

For example I have the following quantities (grouped by size) for this product:

* color: blue, size: 40/54, length: 32, quantity: 5
* color: blue, size: 40/54, length: 34, quantity: 5
* color: blue, size: 40/54, length: 36, quantity: 5

---

* color: blue, size: 42/56, length: 32, quantity: 5
* color: blue, size: 42/56, length: 34, quantity: 5
* color: blue, size: 42/56, length: 36, quantity: 5

---

* color: blue, size: 44/58, length: 32, quantity: 0
* color: blue, size: 44/58, length: 34, quantity: 5
* color: blue, size: 44/58, length: 36, quantity: 5

As you can see only the product with size 44/58 and length 32 is sold out, but in my store it displays that everything is available and if the user selects the size 44/58 with the length 32 a random length is chosen for him. How can I fix this? I have a third part theme that doesn't have support and I can't change it with another theme.

Here's the code of the file swatch.liquid that manages the display of the variants:

```
{% comment %}
  Set the extension of your color files below. Use 'png', 'jpeg', 'jpg' or 'gif'.
{% endcomment %}
{% assign file_extension = 'png' %}
{% capture variantsswatch %} {% endcapture %}
{% if swatch == "Color" %}
    {% capture variantsswatch %}{{ 'products.variants.color' | t }}{% endcapture %}
{% elsif swatch == "Size" %}
    {% capture variantsswatch %}{{ 'products.variants.size' | t }}{% endcapture %}
{% else %}
    {% capture variantsswatch %}{{ swatch }}{% endcapture %}
{% endif %}

{% if swatch == blank %}
    <div class="swatch error">
        <p>You must include the snippet swatch.liquid with the name of a product option.</p>
        <p>Use: <code>{% raw %}{% include 'swatch' with 'name of your product option here' %}{% endraw %}</code></p>
        <p>Example: <code>{% raw %}{% include 'swatch' with 'Colore' %}{% endraw %}</code></p>
    </div>
{% else %}
{% assign found_option = false %}
{% assign is_color = false %}
{% assign is_lunghezza = false %}
{% assign option_index = 0 %}
{% assign indexChild = 0 %}
{% for option in product.options %}
    {% if option == swatch %}
        {% assign found_option = true %}
        {% assign option_index = forloop.index0 %}
        {% assign indexChild = forloop.index %}
        <style rel="stylesheet" type="text/css">
            .proVariants .selector-wrapper:nth-child({{ indexChild }}){display: none;}
            .maxus-productdetail__options:not(:last-child) {
                margin-right: 20px;
            }
        </style>
        {% assign downcased_option = swatch | downcase %}
        {% if downcased_option contains 'colore' or downcased_option contains 'colour' or downcased_option contains 'color' %}
            {% assign is_color = true %}
        {% endif %}
        {% if downcased_option contains 'lunghezza' or downcased_option contains 'length' %}
            {% assign is_lunghezza = true %}
        {% endif %}
    {% endif %}
{% endfor %}
{% unless found_option %}

{% else %}
<div class="maxus-productdetail__options{% unless section.settings.spd_style == "pd_style2" %} {% endunless %} {% if is_color %}var-colore{% endif %}">
    <div class="{% if settings.swatch_style == "sw_radio1" or settings.swatch_style == "sw_radio2" %} swatch_radio1 {% elsif settings.swatch_style == "sw_radio3" or settings.swatch_style == "sw_radio4" %} swatch_radio3 {% elsif settings.swatch_style == "sw_rectangle1" or settings.swatch_style == "sw_rectangle2" or settings.swatch_style == "sw_gallery" %} swatch_rectangle1 {% endif %}swatch clearfix {% if settings.po_style == "po_swatchs" %} align-center flex engoc-flex-wrap{% endif %}" data-option-index="{{ option_index }}">
        <!-- <p class="text-uppercase title_variant" style="border-bottom:none;padding-bottom:none;">{{ variantsswatch }} </p> -->
        {% if variantsswatch == 'Colore' %}
        <p class="text-uppercase title_variant" style="border-bottom:none;padding-bottom:none;">Colore </p>
        {% elsif variantsswatch == 'Taglia' %}
        <p class="text-uppercase title_variant" style="border-bottom:none;padding-bottom:none;">Taglia </p>
        {% elsif variantsswatch == 'Lunghezza' %}
        <p class="text-uppercase title_variant" style="margin-left:6px;border-bottom:none;padding-bottom:none;">Lunghezza </p>
        {% endif %}
        {% assign values = '' %}
        {% for variant in product.variants %}
            {% assign value = variant.options[option_index] %}
            {% unless values contains value %}
                {% assign values = values | join: ',' %}
                {% assign values = values | append: ',' | append: value %}
                {% assign values = values | split: ',' %}

                {% assign unique_variant_id = variant.id | append: '-' | append: value | append: '-' | append: option_index %}

                {% assign available = false %}
                {% if variant.available %}
                    {% assign available = true %}  
                {% else %}
                    {% comment %}
                        Check if any other variant with the same size is available
                    {% endcomment %}
                    {% for other_variant in product.variants %}
                        {% if other_variant != variant and other_variant.options[option_index] == value and other_variant.available %}
                            {% assign available = true %}
                            {% break %}
                        {% endif %}
                    {% endfor %}
                {% endif %}
                    {% if is_color %}
                      <div data-value="{{ value | escape }}" data-style="square" class="maxus-color none color {{ value | handle }} {% if available %} available {% else %}soldout{% endif %}" {% if available %}{% else %}data-toggle="tooltip" data-placement="top"  data-html="true" data-original-title="Coming Soon <br> NOTIFY ME"{% endif %}>
                        <input id="swatch-{{ option_index }}-{{ value | handle }}" type="radio" name="option-{{ option_index }}" value="{{ value | escape }}"{% if forloop.first %} checked{% endif %} {% unless available %}disabled{% endunless %} />
                        {% if settings.swatch_style == "sw_radio1" or settings.swatch_style == "sw_radio3"  %}
                            <label class="radio_style1" for="swatch-{{ option_index }}-{{ value | handle }}">
                                <label class="color_style1" for="swatch-{{ option_index }}-{{ value | handle }}">
                                </label>
                                <span class="text_color">{{ value }}</span>
                            </label>  
                        {% elsif settings.swatch_style == "sw_radio2"  %}
                            <div class="radio_style2" data-toggle="tooltip" data-placement="top" data-original-title="{{value}}">
                                <label class="color_style2" for="swatch-{{ option_index }}-{{ value | handle }}" style="background-image: url({{ variant.image.src | product_img_url: 'grande' }}); background-size: cover;">
                                </label>
                            </div>  
                        {% elsif settings.swatch_style == "sw_rectangle1"  %}
                            <label class="rectangle_style1" for="swatch-{{ option_index }}-{{ value | handle }}">
                                <span class="text_rec">{{ value }}</span>
                            </label>
                        {% elsif settings.swatch_style == "sw_gallery"  %}
                            <div class="swatch_gallery">
                                <label class="bg_image" for="swatch-{{ option_index }}-{{ value | handle }}" style="background-color: {{ value | split: ' ' | last | handle }}; background-image: url({{ value | handle | append: '.' | append: file_extension | file_url }}); background-size: cover;">
                                </label>
                            </div> 
                        {% elsif settings.swatch_style == "default" or settings.swatch_style == "sw_radio4" or settings.swatch_style == "sw_rectangle2"   %}
                            <div class="  border-color ">
                                <label class="link_color" for="swatch-{{ option_index }}-{{ value | handle }}" style="background-color: {{ value | split: ' ' | last | handle }}; background-image: url({{ value | handle | append: '.' | append: file_extension | file_url }}); background-size: cover;">
                                </label>
                            </div> 
                        {% endif %}
                        </div>

                    {% elsif is_lunghezza %}
                        <div data-value="{{ value | escape }}" data-style="square" class="maxus-color none length colora-nero {{ value | handle }} {% if available %} available {% else %}soldout{% endif %}" {% if available %}{% else %}data-toggle="tooltip" data-placement="top"  data-html="true" data-original-title="Coming Soon <br> NOTIFY ME"{% endif %}>
                          <input id="swatch-{{ option_index }}-{{ value | handle }}" type="radio" name="option-{{ option_index }}" value="{{ value | escape }}"{% unless available %} disabled{% endunless %} />
                          {% if settings.swatch_style == "sw_radio1" or settings.swatch_style == "sw_radio2" or settings.swatch_style == "sw_radio3" or settings.swatch_style == "sw_radio4" %}
                              <label class="radio_style1" for="swatch-{{ option_index }}-{{ value | handle }}">
                                  <label class="color_style1" for="swatch-{{ option_index }}-{{ value | handle }}" >
                                  </label>
                                  <span class="text_color">{{ value }}</span>
                              </label> 
                          {% elsif settings.swatch_style == "sw_rectangle1" or settings.swatch_style == "sw_rectangle2" or settings.swatch_style == "sw_gallery" %}
                              <label class="rectangle_style1" for="swatch-{{ option_index }}-{{ value | handle }}">
                                  <span class="text_rec">{{ value }}</span>
                              </label>
                          {% elsif settings.swatch_style == "default" %}
                              <label class="variant_other" for="swatch-{{ option_index }}-{{ value | handle }}" >
                                  {{ value }}
                              </label>
                          {% endif %}
                      </div>
                    {% else %}
                      <div data-value="{{ value | escape }}" data-style="square" class="maxus-color none taglia {{ value | handle }} {% if available %} available {% else %}soldout{% endif %}" {% if available %}{% else %}data-toggle="tooltip" data-placement="top"  data-html="true" data-original-title="Coming Soon <br> NOTIFY ME"{% endif %}>
                        <input id="swatch-{{ option_index }}-{{ value | handle }}" type="radio" name="option-{{ option_index }}" value="{{ value | escape }}" {% unless available %} disabled{% endunless %} />
                        {% if settings.swatch_style == "sw_radio1" or settings.swatch_style == "sw_radio2" or settings.swatch_style == "sw_radio3" or settings.swatch_style == "sw_radio4" %}
                              <label class="radio_style1" for="swatch-{{ option_index }}-{{ value | handle }}">
                                  <label class="color_style1" for="swatch-{{ option_index }}-{{ value | handle }}" >
  
                                  </label>
                                  <span class="text_color">{{ value }}</span>
                              </label> 
                          {% elsif settings.swatch_style == "sw_rectangle1" or settings.swatch_style == "sw_rectangle2" or settings.swatch_style == "sw_gallery" %}
                              <label class="rectangle_style1" for="swatch-{{ option_index }}-{{ value | handle }}">
                                  <span class="text_rec">{{ value }}</span>
                              </label>
                          {% elsif settings.swatch_style == "default" %}
                              <label class="variant_other" for="swatch-{{ option_index }}-{{ value | handle }}" >
                                  {{ value }}
                              </label>
                          {% endif %}
                        </div>
                    {% endif %}
                
            {% endunless %}
        {% endfor %}
    </div>
</div>
{% endunless %}
{% endif %}
```

---

## 161. How to load values from shop.metafields as options in a Shopify schema tag in liquid file?
**Score:** 1 | **Tags:** shopify, liquid, shopify-app, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/76098188/how-to-load-values-from-shop-metafields-as-options-in-a-shopify-schema-tag-in-li

I am working on a Shopify theme app that requires me to load configuration options from shop.metafields and use them as selectable options in a schema tag. I have tried to generate the options array inside the schema tag using a for loop, but it doesn't seem to be correct approach. Here's a simplified version of my code:

```
{% assign optionsArray = shop.metafields.global.convertcart_blockIds %};

{% schema %}
  {
    "name": "Recommended Products",
    "tag": "section",
    "target": "section",
    "settings": [
      {
        "type": "richtext",
        "id": "heading",
        "label": "Heading"
      }, {
        "type": "select",
        "id": "blockId",
        "label": "Block ID",
        "info": "Select an option",
        "options": [{% for option in optionsArray %}
            {
            "value": "{{ option }}",
            "label": "{{ option }}"
          }{% unless forloop.last %},
          {% endunless %}{% endfor %}]
      }
    ]
  }
{% endschema %}
```

I have tried constructing the options array in the script tag but still using that options array in schema was not possible. Can someone please help me figure out how to properly load the configuration options from shop.metafields and use them as selectable options in a schema tag? Any help or directions on this would be greatly appreciated. Thanks!

---

## 162. How do I make a database request from a liquid app proxy page?
**Score:** 1 | **Tags:** shopify, liquid, shopify-app, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/75980967/how-do-i-make-a-database-request-from-a-liquid-app-proxy-page

I'm new to Shopify development so please forgive me if I'm misunderstanding how this should work, but I'm working on an app that has a user-facing frontend and have run into a roadblock. To start off with some backstory, I'm trying to make a classifieds page that can be accessed from the frontend, and will still integrate with the existing theme (so header, footer, etc are imported from the shop's theme), and the data gets populated from a database I have set up. Then from the admin page, the listings can be removed/whatever else needs to be done by an admin.

I'm developing this for a theme that doesn't have theme extension functionality (so no app blocks), so after doing some research it seems like an app proxy that returns a liquid file is my best bet. I've modified the Shopify QR code app example to have an app proxy running on the same server, and currently have it returning a .liquid file after everything has been verified. This is where I'm a bit confused, as I tried using a `{ javascript }` tag so I can make a request to my database end points and populate everything accordingly, but it would give me an error saying that tag doesn't exist (even though it exists [here](https://shopify.dev/docs/api/liquid/tags/javascript)). Am I going about this wrong, or am I just missing something? There's another app that uses the same idea, where it routes to /a/<appname> and displays custom data that can make a request to a server so I know this method is possible, I guess I'm just a little lost on the implementation of it. Any advice would be much appreciated!

---

## 163. Shopify Schema Select Value
**Score:** 1 | **Tags:** shopify, shopify-template, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/75216209/shopify-schema-select-value

I'm trying to access the selected schema value in Shopify and all that gets returned is the label formatted in lowercase with dashes instead of spaces.

`

```
{
        "type": "hmc360_options",
        "name": "3D Configuration Options",
        "settings": [
          {
            "type": "text",
            "id": "options_title",
            "label": "Title",
            "default": "3D Options"
          },
          {
            "type": "select",
            "id": "hmc360-option-type",
            "label": "Option Type",
            "default": "na",
            "options": [
              {
                "label": "Style",
                "value": "pick_a_style"
              },
              {
                "value": "pick_a_wood_finish",
                "label": "Finish"
              },
              {
                "label": "N/A",
                "value": "na"
              }
            ]
          }
}
```

When {{ block.settings.hmc360-option-type }} is used in Liquid, it returns the value as described above. I can't seem to find anything about this so I'm lead to believe it's something silly on my end.

{{ block.settings.hmc360-option-type }} should return "pick\_a\_style" or "pick\_a\_wood\_finish"

---

## 164. How to call a metafield value on the checkout page in shopify
**Score:** 1 | **Tags:** shopify, liquid, shopify-template, shopify-liquid, shopifyscripts | **Answered:** False
**Link:** https://stackoverflow.com/questions/75027779/how-to-call-a-metafield-value-on-the-checkout-page-in-shopify

I'm trying to display the item data from the metafield on the checkout page using this code-

{{ pages.package-urls.metafields.custom.checkout\_message }} on checkout.liquid file.

We are using Shopify Plus and the metafields are displaying on other templates fine.

---

## 165. Shopify Liquid Differentiate Taxable Products
**Score:** 1 | **Tags:** shopify, shopify-template, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/72814377/shopify-liquid-differentiate-taxable-products

**Is there any solution, that can help me to Differentiate taxable products?**

**For Eg:** We need to extract only those products from a single collection, which has a variation with taxable without adding any patches with if a condition or contain operator.

**What I Tried:**

```
{% for products in collections.all.products | where : 'variants.taxable' , false %}
   ......
{% endfor %}
```

But didn't succeed. If anyone has any solution to feature this out. that will be appreciated.

Thanks

---

## 166. Is there any way to add metafields data on the homepage of shopify site?
**Score:** 1 | **Tags:** shopify, liquid, shopify-template, shopifyscripts, shopify-liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/72351377/is-there-any-way-to-add-metafields-data-on-the-homepage-of-shopify-site

I want to show some content on the homepage of my shopify site, the content is added in metafields created for pages. Is there any way to add metafields data on the homepage of shopify site?

---

## 167. Shopify app extension fetch data with my database
**Score:** 1 | **Tags:** shopify, shopify-app, shopify-api, shopify-storefront-api, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/71948738/shopify-app-extension-fetch-data-with-my-database

I was wondering how to get the data from my database(mySQL || mongodb) and then use App Block it displaying it.

Can someone please help.

---

## 168. How to modify product page using Theme and Asset api for a shopify App
**Score:** 1 | **Tags:** shopify, shopify-app, shopify-template, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/70743599/how-to-modify-product-page-using-theme-and-asset-api-for-a-shopify-app

I am creating a Shopify app that will insert a trust seal or badge on the product page. However, there is difficulty in implementing it since there is no clear documentation or tutorials on how to do it. What I want to achieve is to place an image (trust badge) somewhere before or after the Add to cart button. This is a public app, so modifying the theme through Shopify API themes/assets is the only option to do it dynamically.

Shopify is really new to me. I just studied it for 3 weeks, maybe someone who has prior experience in implementing this would help me.

Please refer to the image for reference.
[![enter image description here](https://i.sstatic.net/06U7u.png)](https://i.sstatic.net/06U7u.png)

Thank you in advance! :-)

---

## 169. Why would the Supabase client cause a MiniOxygen error with &quot;dev&quot; script but work with &quot;preview&quot; script?
**Score:** 1 | **Tags:** typescript, remix.run, supabase-js, shopify-hydrogen | **Answered:** True
**Link:** https://stackoverflow.com/questions/79422617/why-would-the-supabase-client-cause-a-minioxygen-error-with-dev-script-but-wor

In my up to date shopify hydrogen/remix app, I am trying to import the supabase-js package into my server.ts or specific route. When I initialize the createClient function, then run the "shopify hydrogen dev --codegen" command, I get this error.

```
MiniOxygen couldn't load your app's entry point.
ReferenceError: exports is not defined
    at /@fs/home/xx/repos/root/node_modules/.pnpm/@supabase+postgrest-js@1.18.1/node_modules/@supabase/postgrest-js/dist/cjs/index.js?v=1f494df2:5:23
    at /@fs/home/xx/repos/root/node_modules/.pnpm/@supabase+postgrest-js@1.18.1/node_modules/@supabase/postgrest-js/dist/esm/wrapper.mjs?v=1f494df2:1:110
    at /@fs/home/xx/repos/root/node_modules/.pnpm/@supabase+supabase-js@2.48.1/node_modules/@supabase/supabase-js/dist/module/SupabaseClient.js?v=1f494df2:2:31
```

When I run the script for "npm run build && shopify hydrogen preview", it starts up and works without problem. The supabase-js client works as intended.

This is a snippet from my `server.ts` file where the client is called

```
import { createClient } from '@supabase/supabase-js'

/**
 * Export a fetch handler in module format.
 */
export default {
  async fetch(
    request: Request,
    env: Env,
    executionContext: ExecutionContext,
  ): Promise<Response> {
    try {
      /**
       * Open a cache instance in the worker and a custom session instance.
       */
      if (!env?.SESSION_SECRET) {
        throw new Error('SESSION_SECRET environment variable is not set');
      }

      const test = createClient(env.SUPABASE_URL, env.SUPABASE_ANON_KEY)
```

```
Versions:
 Node: >=20.0.0
 Vite: 5.4.14
 @shopify/hydrogen: 2024.10.1
 @shopify/mini-oxygen: 3.1.1
 @supabase/supabase-js: 2.48.1
 @supabase/postgrest-js: 1.18.1
 @remix-run/node: 2.15.3
 @remix-run/react: 2.15.3
 @remix-run/server-runtime: 2.15.3
 React: 18.3.1
 React-DOM: 18.3.1

Dependencies:
 @supabase/supabase-js: ^2.48.1
 @shopify/hydrogen: ^2024.10.1
 @shopify/mini-oxygen: ^3.1.1
 React: ^18.3.1
 @remix-run/react: ^2.15.3
 clsx: ^2.1.1
 component-folder: workspace:*
 graphql: ^16.10.0
 graphql-tag: ^2.12.6
 swiper: ^11.2.2
 tiny-invariant: ^1.3.3

Dev Dependencies:
 Vite: ^5.4.14
 @shopify/hydrogen-codegen: ^0.3.2
 @shopify/mini-oxygen: ^3.1.1
 @types/node: ^22.13.0
 eslint: ^8.57.1
 typescript: ^5.7.3
 prettier: ^3.4.2 

Scripts:
 dev: shopify hydrogen dev --codegen
 build: shopify hydrogen build --codegen --no-lockfile-check
 preview: npm run build && shopify hydrogen preview
```

Now I am stuck trying to wrap my head around why one would cause issues but the other does not. My first thought was perhaps it is related to the pnpm workspaces used in this monorepo. The structure is

```
root
|--working_folder
|    |--package.json
|    |--vite.config.ts
|--package.json
```

The error message indicates the package causing the problem is in the root folder's node\_modules. But the supabase-js was installed in the working\_folder dir. So that made me think maybe it's the `vite.config.ts` file causing an issue with bundling?

```
import path from 'path';

import {defineConfig} from 'vite';
import {hydrogen} from '@shopify/hydrogen/vite';
import {oxygen} from '@shopify/mini-oxygen/vite';
import {vitePlugin as remix} from '@remix-run/dev';
import tsconfigPaths from 'vite-tsconfig-paths';
import {flatRoutes} from 'remix-flat-routes';

export default defineConfig({
  plugins: [
    hydrogen(),
    oxygen(),
    remix({
      presets: [hydrogen.preset()],
      future: {
        v3_fetcherPersist: true,
        v3_relativeSplatPath: true,
        v3_throwAbortReason: true,
      },
      ignoredRouteFiles: ['**/*'],
      routes: async (defineRoutes) => {
        return flatRoutes(['routes'], defineRoutes);
      },
    }),
    tsconfigPaths(),
  ],
  ssr: {
    noExternal: [],
    optimizeDeps: {
      include: [
        'websocket',
        'fast-deep-equal/react',
        'typographic-base',
        'marked',
      ],
    },
  },
  optimizeDeps: {
    include: [
      'clsx',
      '@headlessui/react',
      'react-intersection-observer',
      'react-use/esm/useScroll',
      'react-use/esm/useDebounce',
      'react-use/esm/useWindowScroll',
      'remove-markdown',
    ],
    exclude: [],
  },
  build: {
    // Allow a strict Content-Security-Policy
    // withtout inlining assets as base64:
    assetsInlineLimit: 0,
  },
  resolve: {
    alias: {
      '@tailwindcss/vite': '@tailwindcss/vite/index.js',
      '~': path.resolve(__dirname, './app'),
    },
  },
});
```

If so, I'm a little perplexed why the build command would lead to a working page.

The other option could be the mini-oxygen workers not working with the supabase package. My understanding is that the workers are similar to cloudflare workers, which per supabase-js's README, says to include this code for compatibility.

```
import { createClient } from '@supabase/supabase-js'

// Provide a custom `fetch` implementation as an option
const supabase = createClient('https://xyzcompany.supabase.co', 'public-anon-key', {
  global: {
    fetch: (...args) => fetch(...args),
  },
})
```

This approach was also unsuccessful.

My current workaround is to make a fetch request to supabase without any imports. This isn't ideal for 2 reasons. The first is there are a number of conveniences to using their client, the second, and bigger concern is that this is an deeper issue with versioning or bundling.

# Questions:

* Is there an issue with how Vite handles @supabase/supabase-js or @supabase/postgrest-js during development in this worker setup?
* How can I configure the environment (MiniOxygen vs Vite) to resolve the exports is not defined error?
* Has anyone encountered this issue when using supabase-js in a worker environment (like MiniOxygen) and found a solution?
* Is there anything in my Vite or worker configuration that might be causing this discrepancy?

Thank you very much for taking your time and providing any help!

---

## 170. npm run dev not working. Command `hydrogen dev` not found
**Score:** 1 | **Tags:** npm, shopify, shopify-hydrogen | **Answered:** True
**Link:** https://stackoverflow.com/questions/77633400/npm-run-dev-not-working-command-hydrogen-dev-not-found

When 'npm run dev' I get this.

```
?  Command `hydrogen dev` not found. Did you mean `kitchen-sink prompts`?

>  (y) Yes, confirm
   (n) No, cancel

   Press ↑↓ arrows to select, enter or a shortcut to confirm.
```

[enter image description here](https://i.sstatic.net/tUCtK.png)

Node and npm are up-to-date. I also tried opening a new terminal. I also tried deleting and rebuiding the storefront.

---

## 171. In Shopify using GraphQL how should I query a metaobject and a sub-query metaobject in a single query?
**Score:** 1 | **Tags:** graphql, shopify, shopify-hydrogen, metaobject | **Answered:** True
**Link:** https://stackoverflow.com/questions/76683226/in-shopify-using-graphql-how-should-i-query-a-metaobject-and-a-sub-query-metaobj

I am building a website with Shopify Hydrogen.

Using GraphQL I am accessing MetaObjects.

The structure of the MetaObject is one field and one sub-MetaObject (a generic, reusable meta object).

I wish to have a query that gives me the fields from the MetaObject (working) and the Sub-MetaObject (not working).

My query looks like this...

```
query {
    metaobject(
        handle: {
            handle: "template-home",
            type: "header_template",
        }
    ) {
        handle,
        type
        page_url: field(key: "page-url") {
            value
        },
        header_info: field(key: "header_info") {
            value
        },    
    }
}
```

..and that gets half the job done but doesn't let me see the sub-metaobject and the result is...

```
{
    "data": {
        "metaobject": {
            "handle": "template-home",
            "type": "header_template",
            "page_url": {
                "value": "/"
            },
            "header_info": {
                "value": "gid://shopify/Metaobject/1234567890"
            }
        }
    }
}
```

I don't want the key to the Metaobject returned, I want the fields from the meta object as a sub-result (or even flattened in the parent would be fine too).

How do I write another sub-query to expose all the fields within this sub-meta object so I can run one command. The point of GraphQL is to avoid additional server side trips in comparison to REST, so presume this is possible but new to GraphQL.

If not possible, how do I avoid multiple calls to Shopify in Remix?

Thanks.

---

## 172. Dev page showing up all the time on index page
**Score:** 1 | **Tags:** shopify, remix.run, shopify-storefront-api, shopify-hydrogen | **Answered:** True
**Link:** https://stackoverflow.com/questions/76088551/dev-page-showing-up-all-the-time-on-index-page

Even after setting the `.env` file, I keep having the dev home page on my store. I need to go to `http://localhost:3000/index` to be able to see the actual index page I created. How can I remove it?

The shopify hydrogen docs suggest that this shouldn't appear once you set the `.env` correctly.

[![enter image description here](https://i.sstatic.net/OVzXp.png)](https://i.sstatic.net/OVzXp.png)

---

## 173. Open Cart Slider using custom ajax add to cart script Shopify Flow Theme
**Score:** 1 | **Tags:** javascript, jquery, vue.js, shopify, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/79045306/open-cart-slider-using-custom-ajax-add-to-cart-script-shopify-flow-theme

I have created custom ajax add to cart functionality in my store and I want to open the slider cart after successful add to cart event. I have achieved it using the below code but it only works for the first time.

If you remove the products from cart and try to add again then it won't show the updated cart or if you want to add more to it then also it won't work. Cart drawer only opens for the first time only. I am using shopify flow theme.

```
function addProductsToCart(variantIdRegular, variantIdSubscription, selling_plan_id) {
  
  var itemsToAdd = [{ id: variantIdRegular, quantity: 1 }];

  if ($("input[name=payment-option]").is(":checked")) {
      itemsToAdd.push({ id: variantIdSubscription, quantity: 1, selling_plan: selling_plan_id });
  }
  
  $.ajax({
    url: '/cart/add.js',
    type: 'post',
    dataType: 'json',
    contentType: "application/json",
    data: JSON.stringify({ 'items': itemsToAdd }),
    success: function(response) {
      console.log('Both products added', response);
      var cartDrawerButtonSelector = ".js-drawer-open-right-link";
      var cartDrawerButton = document.querySelector(cartDrawerButtonSelector);
      cartDrawerButton.click();
    },
    error: function(xhr, status, error) {
      console.error('Failed to add products', xhr.responseJSON);
    }
  });
}
```

What can I try next to fix this?

---

## 174. Shopify Hydrogen: ERR_CONNECTION_RESET - Cannot reach development server on local machine (localhost:3000) after running npm run dev
**Score:** 1 | **Tags:** shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/78821201/shopify-hydrogen-err-connection-reset-cannot-reach-development-server-on-loca

Note: I'm on Windows 10, running Ubuntu 24.04 LTS, WSL.

Hi, I'm trying to get started with learning Shopify Hydrogen and creating a storefront. I have followed Shopify's guide here: <https://shopify.dev/docs/storefronts/headless/hydrogen/getting-started>

I have created a new storefront project directory with `npm create @shopify/hydrogen@latest -- --quickstart`

I then did `npm run dev` to run the development server, which seemingly is running okay, if my command line is anything to go by: [Image of command line](https://i.sstatic.net/oJpibtMA.png)

```
> hydrogen-quickstart@2024.7.3 dev
> shopify hydrogen dev --codegen


Environment variables injected into MiniOxygen:

SESSION_SECRET   from local .env

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help


╭─ success ────────────────────────────────────────────────────────────────────╮
│                                                                              │
│  View Hydrogen app: http://localhost:3000/ [1]                               │
│                                                                              │
│  View GraphiQL API browser:                                                  │
│  http://localhost:3000/graphiql                                              │
│                                                                              │
│  View server network requests:                                               │
│  http://localhost:3000/subrequest-profiler                                   │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
[1] http://localhost:3000/
```

However, whenever I try to access the development server at localhost:3000 in my browser (any browser, Chrome, Firefox, all return the same issue), nothing loads. In Chrome, I get a "This site can't be reached" - `ERR_CONNECTION_RESET` error: [Chrome browser error: ERR\_CONNECTION\_RESET](https://i.sstatic.net/fc1muq6t.png)

**This issue is exclusively happening to me with Shopify Hydrogen.** I haven't encountered any issues with running local development servers with other applications, e.g. Vite with React, Next.js - those are all working.

If anyone has any ideas about what I can do to resolve this issue, I would appreciate it.

Thanks.

---

## 175. Shopify Hydrogen - project no longer launches after updating to 2024.4
**Score:** 1 | **Tags:** typescript, command-line-interface, shopify, remix.run, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/78329263/shopify-hydrogen-project-no-longer-launches-after-updating-to-2024-4

Since updating my Hydrogen project it now no longer launches when using the npm run dev command.

* My project was working fine.
* Decided to update package.json (and relevant files) to latest found in Templates > [Skeleton](https://github.com/Shopify/hydrogen/tree/main/templates/skeleton).
* Attempt to execute "npm run dev".
* Failed to run / start local web server with absolutely no error.

See below for the command (and the lack of result)

```
PS C:\GitHub\XXXX\hydrogen\hydrogen> npm run dev

hydrogen@1.0.7 dev
shopify hydrogen dev --codegen

PS C:\GitHub\XXXX\hydrogen\hydrogen>
```

Package.json

```
{
  "name": "hydrogen",
  "private": true,
  "sideEffects": false,
  "version": "1.0.7",
  "type": "module",
  "scripts": {
    "build": "shopify hydrogen build --codegen",
    "dev": "shopify hydrogen dev --codegen",
    "preview": "npm run build && shopify hydrogen preview",
    "lint": "eslint --no-error-on-unmatched-pattern --ext .js,.ts,.jsx,.tsx .",
    "typecheck": "tsc --noEmit",
    "codegen": "shopify hydrogen codegen"
  },
  "browserslist": [
    "defaults"
  ],
  "prettier": "@shopify/prettier-config",
  "dependencies": {
    "@headlessui/react": "^1.7.2",
    "@headlessui/tailwindcss": "0.2.0",
    "@remix-run/react": "^2.8.0",
    "@remix-run/server-runtime": "^2.8.0",
    "@shopify/cli": "3.52.0",
    "@shopify/cli-hydrogen": "^8.0.0",
    "@shopify/hydrogen": "2024.4.0",
    "@shopify/remix-oxygen": "^2.0.4",
    "clsx": "^1.2.1",
    "cross-env": "^7.0.3",
    "graphql": "^16.6.0",
    "graphql-tag": "^2.12.6",
    "isbot": "^3.8.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-intersection-observer": "^9.4.1",
    "react-use": "^17.4.0",
    "schema-dts": "^1.1.0",
    "tiny-invariant": "^1.2.0",
    "typographic-base": "^1.0.4",
    "js-cookie": "3.0.5",
    "pdfmake": "0.2.10"
  },
  "devDependencies": {
    "@graphql-codegen/cli": "5.0.2",
    "@playwright/test": "^1.40.1",
    "@remix-run/dev": "^2.8.0",
    "@remix-run/eslint-config": "^2.8.0",
    "@shopify/hydrogen-codegen": "^0.3.0",
    "@shopify/mini-oxygen": "^3.0.0",
    "@shopify/eslint-plugin": "^44.0.0",
    "@shopify/oxygen-workers-types": "^4.0.0",
    "@shopify/prettier-config": "^1.1.2",
    "@tailwindcss/forms": "^0.5.3",
    "@tailwindcss/typography": "^0.5.9",
    "@total-typescript/ts-reset": "^0.4.2",
    "@types/eslint": "^8.4.10",
    "@types/react": "^18.2.22",
    "@types/react-dom": "^18.2.7",
    "cross-env": "^7.0.3",
    "eslint": "^8.20.0",
    "eslint-plugin-hydrogen": "0.12.2",
    "postcss": "^8.4.21",
    "postcss-import": "^15.1.0",
    "postcss-preset-env": "^8.2.0",
    "prettier": "3.2.4",
    "rimraf": "^3.0.2",
    "tailwindcss": "^3.3.0",
    "typescript": "^5.2.2",
    "postcss-nesting": "11.2.2",
    "prettier-plugin-tailwindcss": "0.5.11",
    "react-icons": "5.0.1",
    "@types/pdfmake": "0.2.9",
    "vite": "^5.1.0",
    "vite-tsconfig-paths": "^4.3.1"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

Any ideas most appreciated - even if how to find out more diagnostic information. Thanks.

**Update #1**

Good feedback on the below issue page
<https://github.com/Shopify/hydrogen/issues/2000>

I'm upgrading manually because I'm half way through changes on my main branch - you can use the upgrade command apparently but you need to do this before you make changes and only if your project is fully checked in.

But for some reason I am receiving the below error messages...

```
Warning: Could not find ts-node at 
 »   C:\GitHub\XXXX\hydrogen\hydrogen\node_modules\@shopify\cli\dist\index-e6f8190d.js. Please ensure that ts-node   
 »   is a devDependency. Falling back to compiled source.


Unhandled Rejection:  OTLPExporterError: Request Timeout
    at ClientRequest.<anonymous> (file:///C:/GitHub/XXXX/hydrogen/hydrogen/node_modules/@shopify/cli/dist/chunk-LKVSWZE2.js:46699:25)
    at ClientRequest.emit (node:events:517:28)
    at ClientRequest.emit (node:domain:489:12)
    at TLSSocket.socketCloseListener (node:_http_client:474:11)
    at TLSSocket.emit (node:events:529:35)
    at TLSSocket.emit (node:domain:489:12)
    at node:net:350:12
    at TCP.done (node:_tls_wrap:657:7) {
  data: undefined,
  code: 'ECONNRESET'
}
[Error: internal error]
```

---

## 176. Shopify Hydrogen - Issue with Blog-&gt;Article retrieve via GraphQL - UNAUTHORIZED?
**Score:** 1 | **Tags:** graphql, shopify, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/78292571/shopify-hydrogen-issue-with-blog-article-retrieve-via-graphql-unauthorized

This was working fine for days until I noticed it not working today. I was pulling articles from a blog via GraphQL. Today, I saw a:

```
Oops
500 [h2:error:storefront.query] [object Object] - Request ID: 3c8bc60f-d909-4821-89e7-6fd796495c13-1712578684
```

Digging in via GraphiQL I see the object return:

```
{
  "errors": [
    {
      "message": "",
      "extensions": {
        "code": "UNAUTHORIZED"
      }
    }
  ]
}
```

All articles do this. Nothing has changed in the shopify admin area. Articles are 'visible'. My non-headless site shows the article fine. The primary blog 'collection' shows the articles and assets associated with it as well. I get the error when trying to access the article directly. Any ideas?

Here is the GraphQL that is run

```
query Article($articleHandle: String!, $blogHandle: String!, $country: CountryCode, $language: LanguageCode) @inContext(language: $language, country: $country) {
  blog(handle: $blogHandle) {
    articleByHandle(handle: $articleHandle) {
      title
      contentHtml
      publishedAt
      author: authorV2 {
        name
      }
      image {
        id
        altText
        url
        width
        height
      }
      seo {
        description
        title
      }
    }
  }
}
```

Again, this has been working and I haven't been in this code for a bit.

---

## 177. React with Tailwind with HeadlessUI - how to add plugin configuration
**Score:** 1 | **Tags:** reactjs, typescript, tailwind-css, headless-ui, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/78133089/react-with-tailwind-with-headlessui-how-to-add-plugin-configuration

I've a react app using Tailwind with some Headless UI tabs.  
I'm trying to style the tabs when active but in order to do that I had to include a new package. Namely @headlessui/tailwindcss found [here](https://www.npmjs.com/package/@headlessui/tailwindcss).

This is the example they document...

```
// tailwind.config.js
module.exports = {
  content: [],
  theme: {
    extend: {},
  },
  plugins: [
    require('@headlessui/tailwindcss')

    // Or with a custom prefix:
    require('@headlessui/tailwindcss')({ prefix: 'ui' })
  ],
}
```

However, I don't use requires in my project (modules, ES2022)... I use imports. This is what my plugins section looks like at the moment...

```
import formsPlugin from "@tailwindcss/forms";
import typographyPlugin from "@tailwindcss/typography";
```

// ...then inside the config...

```
plugins: [formsPlugin, typographyPlugin]
```

How do I add "@headlessui/tailwindcss" into the plugins using an import approach?

Any ideas?

Thanks,
Dan.

---

## 178. Shopify Hydrogen embedding third party booking widget Bokun
**Score:** 1 | **Tags:** reactjs, shopify, shopify-hydrogen | **Answered:** True
**Link:** https://stackoverflow.com/questions/78067461/shopify-hydrogen-embedding-third-party-booking-widget-bokun

**Hello,**

The website I am working on uses Bokun for online booking / gift card purchases.  
They supply a booking widget that is essentially a script tag that dynamically loads the booking / gift card buying interface. Nothing ground breaking there.
The embedded code is set within page content and rendered as below...

```
<div dangerouslySetInnerHTML={{ __html: page.body }} className="" />
```

However I'm using Shopify Hydrogen (react / remix) (above code) to render the below code (page content).

```
<script type="text/javascript" src="https://widgets.bokun.io/assets/javascripts/apps/build/BokunWidgetsLoader.js?bookingChannelUUID=XXXXX" async></script>
     
<div class="bokunWidget" data-src="https://widgets.bokun.io/online-sales/XXXX/gift-card/XXXX"></div>
```

I believe I have sorted out the Security Policy errors e.g. \*.bokun.io and \*.polyfill.io

But now I'm now presented with (hopefully) one last error I can't seem to fix...

```
Warning: Prop `type` did not match. Server: "text/javascript" Client: "application/ld+json"
```

Any ideas / suggestions?

**Thanks.**

---

## 179. what is right way to pass collection id as argument in Shopify hydrogen storefront graphql query?
**Score:** 1 | **Tags:** graphql, shopify, shopify-api, shopify-storefront-api, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/77653462/what-is-right-way-to-pass-collection-id-as-argument-in-shopify-hydrogen-storefro

I want to get collection details while I have array of collection ids which I got from metaobjects collection list.

I am using this code in loader function

```
const id_= "gid://shopify/Collection/409408995579";
  const collection_id_data = await storefront.query({
    data: {
      "query": COLLECTION_QUERY_ID,
      "variables": {"id": id_,},
    },
  })


const COLLECTION_QUERY_ID = `query GetCollection($id: ID!) {
  collection(id: $id) {
    handle
  }
}`
```

I ALSO TRIED THIS CODE TOO:

```
const id_= "gid://shopify/Collection/409408995579"
  const abcd = await storefront.query({
    query: SINGLE_COLLECTION,
    variables: { id_ },
  });
const SINGLE_COLLECTION = `query ($id_ : ID!) {
  collection(id: $id_) {    
    handle
  }
}`
```

but this cause following error:
***TypeError: string.replace is not a function
at minifyQuery
at Object.query***

libratry versions I am using :

```
    "@remix-run/react": "2.1.0",
    "@shopify/cli": "3.50.0",
    "@shopify/cli-hydrogen": "^6.0.0",
    "@shopify/hydrogen": "^2023.10.0",
    "@shopify/remix-oxygen": "^2.0.0",
    "graphql": "^16.6.0",
    "graphql-tag": "^2.12.6",
```

What I want to achieve is to get collection details by using its ids which I have in an array. I want to pass ids to query in loop to get all data collections.

---

## 180. Not able to access env variables in Remix, even in a server file
**Score:** 1 | **Tags:** typescript, remix, remix.run, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/75485110/not-able-to-access-env-variables-in-remix-even-in-a-server-file

I was using Shopify's version of Remix and ran into an issue where I tried to access an API key to be used in a newsletter signup form. However, I cannot access my env variables due to the error `process is not defined.`

app/env/env.server.ts:

```
import {ZodFormattedError} from 'zod';

const serverSchema = z.object({
  KLAVIYO_API_KEY: z.string(),
  KLAVIYO_GLOBAL_LIST_ID: z.string(),
  KLAVIYO_API_VERSION: z.string(),
})

const _serverEnv = serverSchema.safeParse(process.env);

const formatErrors = (errors: ZodFormattedError<Map<string, string>, string>) =>
  Object.entries(errors)
    .map(([name, value]) => {
      if (value && '_errors' in value)
        return `${name}: ${value._errors.join(', ')}\n`;
    })
    .filter(Boolean);

if (_serverEnv.success === false) {
  // eslint-disable-next-line no-console
  console.error(
    '❌ Invalid environment variables:\n',
    ...formatErrors(_serverEnv.error.format()),
  );

  throw new Error('Invalid environment variables');
}

export const env = {..._serverEnv.data};
```

routes/newsletter/subscribe.tsx:

```
import {ActionArgs, json} from '@shopify/remix-oxygen';
import { env } from '../../env/env.server';

export async function action({request}: ActionArgs) {
  const email = (await request.formData()).get('email')?.toString() ?? '';
  try {
    const res = await subscribeToKlaviyoList(email);

    return res.json();
  } catch (error) {
    return json({error: error.message, ok: false});
  }
}



export async function subscribeToKlaviyoList(
  email: string,
  source = 'Home Page Footer',
) {
  const API_KEY = env.KLAVIYO_API_VERSION;
  const API_VERSION = env.KLAVIYO_API_VERSION;
  const LIST_ID = env.KLAVIYO_GLOBAL_LIST_ID;

  return await fetch(
    'https://a.klaviyo.com/api/profile-subscription-bulk-create-jobs/',
    {
      method: 'POST',
      headers: {
        accept: 'application/json',
        revision: API_VERSION ?? '2023-01-24',
        'content-type': 'application/json',
        Authorization: `Klaviyo-API-Key ${API_KEY}`,
      },
      body: JSON.stringify({
        data: {
          type: 'profile-subscription-bulk-create-job',
          attributes: {
            list_id: LIST_ID,
            custom_source: source,
            subscriptions: [
              {
                channels: {email: ['MARKETING']},
                email,
              },
            ],
          },
        },
      }),
    },
  );
}
```

I've followed along with [this](https://remix.run/docs/en/v1/hooks/use-fetcher) example from Remix and [this](https://github.com/remix-run/remix/blob/9b46b9025f534fc8e7bf4c4839ab46092505706e/examples/newsletter-signup/app/routes/newsletter.tsx) GitHub repo, but in both instances, they either aren't using env variables or the API key is hard coded. Any help is greatly appreciated.

---

## 181. Basic MUI component not working in a Typescript project
**Score:** 1 | **Tags:** material-ui, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/75179397/basic-mui-component-not-working-in-a-typescript-project

I'm starting a new Hydrogen project ( Shopify React ). I wanted to use the Material UI lib for my project.

Here is my "basic" code :

```
import * as React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));

export default function Home() {
  return (
  <Box sx={{ flexGrow: 1 }}>
      <Grid container spacing={2}>
        <Grid item xs={8}>
          <Item>xs=8</Item>
        </Grid>
        <Grid item xs={4}>
          <Item>xs=4</Item>
        </Grid>
        <Grid item xs={4}>
          <Item>xs=4</Item>
        </Grid>
        <Grid item xs={8}>
          <Item>xs=8</Item>
        </Grid>
      </Grid>
    </Box>

  )
}
```

And the error I'm getting :

```
Warning: Only plain objects can be passed to client components from server components. Classes or other objects with methods are not supported. Remove sheet from these props: {key: "css", sheet: {\_insertTag: function, isSpeedy: false, tags: \[...\], ctr: 0, nonce: undefined, key: "css", container: undefined, ...}, nonce: undefined, inserted: {...}, registered: {...}, insert: function}
Error processing route: http://localhost:3000/rx
Error: Functions cannot be passed directly to client components because they're not serializable. Remove \_insertTag (function) from this object, or avoid the entire object: {\_insertTag: function, isSpeedy: false, tags: \[...\], ctr: 0, nonce: undefined, key: "css", container: undefined, ...}
at resolveModelToJSON (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=fa4e9613:1515:13)
at StyleSheet.toJSON (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=fa4e9613:1029:14)
at stringify (\<anonymous\>)
at processModelChunk (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=fa4e9613:164:14)
at retryTask (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=fa4e9613:1625:26)
at performWork (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=fa4e9613:1658:7)
at eval (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=fa4e9613:1755:12)
at scheduleWork (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=fa4e9613:58:3)
at startWork (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=fa4e9613:1754:3)
at Object.start (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=fa4e9613:1866:7)
at setupReadableByteStreamController (node:internal/webstreams/readablestream:3110:23)
at setupReadableByteStreamControllerFromSource (node:internal/webstreams/readablestream:3147:3)
at new ReadableStream (node:internal/webstreams/readablestream:250:7)
at Module.renderToReadableStream (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=fa4e9613:1863:16)
at runRSC (/node_modules/@shopify/hydrogen/dist/esnext/entry-server.js?v=fa4e9613:598:46)
at processRequest (/node_modules/@shopify/hydrogen/dist/esnext/entry-server.js?v=fa4e9613:200:15)
at handleRequest (/node_modules/@shopify/hydrogen/dist/esnext/entry-server.js?v=fa4e9613:163:26)
/.../node_modules/yoga-layout-prebuilt/yoga-layout/build/Release/nbind.js:53
throw ex;
^

TypeError: Cannot read properties of undefined (reading 'null')
at getOrCreateServerContext (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite.js?v=fa4e9613:116:23)
at resolveProvider (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite.js?v=fa4e9613:395:51)
at processFullRow (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite.js?v=fa4e9613:469:9)
at processBinaryChunk (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite.js?v=fa4e9613:513:5)
at progress (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite.js?v=fa4e9613:566:5)
```

The problem seems to be related to the lib, when I use basic balise, I'm not facing any issues.

Thanks !

---

## 182. shopify hydrogen and sass setup
**Score:** 1 | **Tags:** sass, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/74160923/shopify-hydrogen-and-sass-setup

hi can somebody explain me how to setup sass module in hydrogen project.
I looked in the documentation but nothing really helpfull.
I ve tried also to add sass dependency but still doesn't recognize my sass file.

---

## 183. Can&#39;t use StoryblokComponent from storyblok/react in my Shopify Hydrogen project
**Score:** 1 | **Tags:** storyblok, shopify-hydrogen | **Answered:** False
**Link:** https://stackoverflow.com/questions/73829302/cant-use-storyblokcomponent-from-storyblok-react-in-my-shopify-hydrogen-project

I'm trying to integrate storyblok's preview/live editing features in my Shopify Hydrogen app. There's isn't any documentation on how to do this in Hydrogen, so I've been using a combination of the [react-specific documentation](https://www.storyblok.com/tp/headless-cms-react) and [nextjs-specific documentation](https://www.storyblok.com/tp/add-a-headless-cms-to-next-js-in-5-minutes) to try to figure it out.

I have everything configured correctly in Storyblok (I built a simple nextjs app and can get the preview/live editing features working correctly there.) But I can't figure out how to get the StoryblokComponent working in my Hydrogen app.

Here's what I'm doing:

I've put the storyblokInit function in App.server.jsx and that part seems to be working (I think).

```
import { storyblokInit, apiPlugin } from '@storyblok/react';
import { Page } from './components/storyblok/Page.client';
import { Teaser } from './components/storyblok/Teaser.client';

const storyblokComponents = {
  page: Page,
  teaser: Teaser
}

storyblokInit({
  accessToken: 'xxxxxxx',
  use: [apiPlugin],
  storyblokComponents
});
```

I'm fetching my Storyblok data using hydrogen's fetchSync. This is working as expected.

```
export function getStoryblokData(slug) {
    if (isServer()) {
        const storyblokData = fetchSync(
            'https://api.storyblok.com/v2/cdn/stories/' + slug + '?token=' + storyblokToken,
            {
              preload: true,
              cache: CacheLong(),
            }
          ).json();
          log.debug('storyblok data from slug: /' + slug, storyblokData);
          return storyblokData;
    }
}
```

I've built the Page and Teaser components pretty much just copy/pasting from the tutorials.

```
import { storyblokEditable, StoryblokComponent } from "@storyblok/react";
 
function Page({ blok }) {
  return (
    <main {...storyblokEditable(blok)}>
      {blok.body.map((nestedBlok) => (
        <StoryblokComponent blok={nestedBlok} key={nestedBlok._uid} />
      ))}
    </main>
  );
}
 
export default Page;


import { storyblokEditable } from "@storyblok/react";

const Teaser = ({ blok }) => {
  return <h2 style={{textAlign: 'center'}} 
    {...storyblokEditable(blok)} >{blok.headline}</h2>;
};
 
export default Teaser;
```

Then in index.server.jsx I'm trying to use StoryblokComponent from storyblok/react

```
import {
  StoryblokComponent,
} from "@storyblok/react";
 let storyblokData = getStoryblokData('home');
    
  return (
    <>
      <StoryblokComponent blok={storyblokData.story.content} />
    </>
  );
}
```

This, as far as I can tell, is where things go wrong. My app breaks and I get this error message:

```
Error processing route: http://localhost:3000/
TypeError: Cannot read properties of undefined (reading 'page')
    at q (/Users/jbaudreau/Desktop/DEMO/hydrogen-storyblok-demo/node_modules/@storyblok/react/dist/storyblok-react.js:7:1033)
    at ce (/Users/jbaudreau/Desktop/DEMO/hydrogen-storyblok-demo/node_modules/@storyblok/react/dist/storyblok-react.js:7:429)
    at attemptResolveElement (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=32cf2471:1060:12)
    at resolveModelToJSON (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=32cf2471:1377:21)
    at Array.toJSON (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=32cf2471:1029:14)
    at stringify (<anonymous>)
    at processModelChunk (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=32cf2471:164:14)
    at retryTask (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=32cf2471:1625:26)
    at performWork (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=32cf2471:1658:7)
    at eval (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=32cf2471:1139:14)
    at scheduleWork (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=32cf2471:58:3)
    at pingTask (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=32cf2471:1138:5)
    at ping (/node_modules/@shopify/hydrogen/vendor/react-server-dom-vite/esm/react-server-dom-vite-writer.browser.server.js?v=32cf2471:1152:14)
    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
```

If anyone can help me figure this out, I'd really appreciate it!

---

## 184. How Can I Target This &lt;span&gt; in CSS?
**Score:** 0 | **Tags:** html, css, shopify, shopify-liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/76568007/how-can-i-target-this-span-in-css

I'm trying to add a line through style to the 'original' price on a shopify site when the sale/compare at price is used.

I'm a bit stumped at how to target this for styling. I'm guessing it's something simple, would appreciate the help!

I'm trying to select the text and style with:

```
text-decoration: line-through !important;
```

See Below HTML

```
<div class="col-span-1">
        <h1 class="text-md">
          THE BLACK PREMIUM SELVEDGE
          <span data-product-price>
            $375.00
          </span>
          <div data-price-wrapper>
            
            <span class="visually-hidden" data-compare-text="">Regular price</span>
            <div data-compare-price="">
               $625.00 
            </div>
```

I've tried all kinds of variations of selectors/nth child etc. and nothing seems to work.

I've only been able to successfully target the col-span-1 and text-md classes.

The span I'm trying to select has

```
data-price-wrapper
```

in it, but as it's not a class or id I'm unsure how to select it!

---

## 185. {{&#160;product.metafields.myfields.myfield.updated_at }} |&#160;Shopify Liquid | Metafields
**Score:** 0 | **Tags:** shopify, liquid, shopify-template, shopify-liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/73558667/product-metafields-myfields-myfield-updated-at-shopify-liquid-metafiel

I wanted to ask if it is possible to show the time when a metafield was updated using Shopify Liquid. I tried these ways:

```
{{ product.metafields.myfields.myfield.updated_at }}
```

```
{{ product.metafields.myfields.myfield.updatedAt }}
```

But neither of those work.

I would very hope someone can help me.

Bye!

---

## 186. Shopify Metafield List of Collections
**Score:** 0 | **Tags:** shopify, liquid, liquid-template, shopify-liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/78164486/shopify-metafield-list-of-collections

I need to get the list of images from my metafield(content type: collection list) in collection. I'm using this logic but it is not working...

Code snippet

```
{% assign top_collections = collection.metafields.custom.c-top-collections %}
{% if top_collections %}
  <ul>
    {% for collection in top_collections %}
      <li>{{ collection.value }}</li>
    {% endfor %}
  </ul>
{% endif %}
```

Please, what is the correct form of doing this? Thank you.

---

## 187. Hide Prices Based On Product Vendor And Customer Tag - Shopify Dawn Theme
**Score:** 0 | **Tags:** css, if-statement, shopify, liquid, shopify-liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/77507893/hide-prices-based-on-product-vendor-and-customer-tag-shopify-dawn-theme

We have a b2b & b2c store using Dawn Theme where we hide prices of products from a brand ‘Dahua’ until an approved customer is logged in.

For this Customers have to register an account and when we’ve done our checks, we approve the account by adding a tag to the customer “trade5” and then they can see prices of Dahua products and place orders for them.

So here is the conditional logic I’m trying to apply;

If the Product Vendor is “dahua” AND
If the customer tag is “trade5”

Do nothing

Else

Apply CSS style “display: none“ to necessary classes.

For every other brands and products customer must be able to see prices and buy products as normal.

=================

I’ve come up with the following code and it works on product pages but the dual condition doesn’t work on home page and collection pages. If I remove the 2nd condition (Vendor if statement), it works everywhere but then it’s applying the style to all brands and products.

===========

```
{% assign customersTagsDowncased = customer.tags | downcase %}

{% assign ProductsVendorDowncased = product.vendor | downcase %}

 

 {%- if customersTagsDowncased contains 'trade5' -%}

 {%- else -%}

    {%- if ProductsVendorDowncased contains 'dahua' -%}

      <style>

        .product-form__buttons, .price__container, .product__tax, .product-form__input, .card-information, .quick-add {

         display: none !important;

       </style>

    {%- endif -%}

 {%- endif -%}
```

==================

It fails on homepage and collection pages every time I have more than 1 conditional logics.

I’ve tried using product tags instead of vendor and other approaches like using 'unless' and 'for' tags too - like the one below but they also fail.

=================

```
{% unless customer.tags contains "trade5" %}

  {% if product.vendor contains "dahua" %}

    <style>

      .product-form__buttons, .price__container, .product__tax, .product-form__input, .card-information, .quick-add {

       display: none !important;

    </style>

  {% endif %}

{% endunless %}
```

=======================

Someone please tell me where I’m going wrong and how to fix it? or if there is a better approach to achieve this without apps.

Preview Store link: <https://crwisj4ojn26fg0n-66693726439.shopifypreview.com>

---

## 188. Shopify Metaobject document link and url fields not working after connecting new domain
**Score:** 0 | **Tags:** html, shopify, liquid, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/79604217/shopify-metaobject-document-link-and-url-fields-not-working-after-connecting-new

I have a product documents metafield with a metaobject reference. The metaobject definition includes a file field, as well as a URL field. Here is what I have set up:

```
{% assign documents = product.metafields.custom.pdp_documents.value %}
<div id="documents" class=" page-width narrow">
  <h3 class="uppercase text-[rgb(var(--colors-text))] anm-fade-element pt-2 pb-2 p-break-words description--caption_cNfMyR tracking-widest leading-tight is-visible mb-6 lg:mb-9 text-left">Documents</h3>
  {% for document in documents %}
 <div class="doc-row flex justify-between">

   <div class="doc_link"><a href={{document.document_url}}
title="Download {{document.title}}">{{document.title}}</a></div>
<div class="flex justify-start pdf"><a href={{document.file | file_url}} target="_blank">PDF</a><span>({{document.file_size}})</span></div>
 </div>
{%endfor%}
</div>
```

This worked just fine before I connected a custom domain to the store. However, after connecting the domain, the links don't work. Looking at dev tools, the hrefs appear to be populating correctly. Here is what I see for one document of one product:

```
<div class="doc-row flex justify-between">
   <div class="doc_link"><a href="https://cdn.shopify.com/s/files/1/0598/5973/0494/files/Primex_OneVUE-SlimMetalSeriesAnalog.pdf?v=1742598724" title="Download PoE Analog Clocks - Slim Metal Series - Data Sheet ">PoE Analog Clocks - Slim Metal Series - Data Sheet </a></div>
<div class="flex justify-start pdf"><a href="//primexinc.com/cdn/shop/files/Primex_OneVUE-SlimMetalSeriesAnalog.pdf?v=9615792470605801721" target="_blank">PDF</a><span>(301.13 kB)</span></div>
 </div>
```

I would appreciate if someone could help me figure out what's going on here!

I tried changing the field in the metaobject. Originally, I had `{{document.file | file_url}}` for both links in the row. I thought that using a different kind of field (URL instead of File) might solve the issue, so I added the URL field to the first link in the row and substituted `{{document.document_url}}` and tried again, with the same result - the links are not clickable!

---

## 189. Dropdown issue in shopify theme dev
**Score:** 0 | **Tags:** shopify, dropdown, liquid, shopify-template, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/79447378/dropdown-issue-in-shopify-theme-dev

I hope you all are doing well. I am currently learning Shopify theme development, and I was working on a theme, but I encountered a glitch that I can’t figure out how to fix. The issue is with the dropdown menu – on mobile, it opens when clicked, but it doesn’t close when clicked again.

The fun fact is that when I run the code in my local environment using shopify CLI, the mobile dropdown opens and closes perfectly. However, after uploading it to Shopify, the mobile dropdown opens but doesn’t close.

This issue is beyond my understanding now, so if anyone here can help me solve it, I would be extremely grateful. Please help me!

```
<header class="navbar">
  <div class="logo">
    {% if section.settings.logo %}
      <a href="/">
        {{ section.settings.logo | image_url: width: 200 | image_tag }}
      </a>
    {% else %}
      <a href="/">{{ shop.name }}</a>
    {% endif %}
  </div>

  <ul class="nav-links">
    {% for link in linklists.main-menu.links %}
      <li class="{% if link.links != blank %}dropdown{% endif %}">
        <a href="{{ link.url }}">{{ link.title }}</a>
        {% if link.links != blank %}
          <ul class="dropdown-menu">
            {% for child_link in link.links %}
              <div class="dropdown-links-wrapper">
                <div class="dropdown-heading">
                  {{ child_link.title }}
                </div>
                <div class="dropdown-links">
                  {% for grandchild_link in child_link.links %}
                    <li><a href="{{ grandchild_link.url }}">{{ grandchild_link.title }}</a></li>
                  {% endfor %}
                </div>
              </div>
            {% endfor %}
          </ul>
        {% endif %}
      </li>
    {% endfor %}
  </ul>

  <button class="hamburger">
    <span class="line"></span>
    <span class="line"></span>
  </button>
</header>

{% schema %}
{
  "name": "Header",
  "settings": [
    {
      "type": "image_picker",
      "id": "logo",
      "label": "Logo Image"
    },
    {
      "type": "text",
      "id": "dropdown_heading",
      "label": "Dropdown Heading",
      "default": "Explore Collection"
    }
  ]
}
{% endschema %}
```

```
@font-face {
    font-family: 'ITALIC';
src:url('https://cdn.shopify.com/s/files/1/0692/4484/6253/files/4DD591D8-4168-4263-B05B-7183DDAFF1F4.TTF?v=1739773692');}

@font-face {
    font-family: 'INTER';
src:url('https://cdn.shopify.com/s/files/1/0692/4484/6253/files/INTER.TTF?v=1739773693');}

body, html {
    margin: 0;
    padding: 0;

}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #121212;
    padding: 10px 20px;
    width: fit-content;    /* width: 50% ki jagah */
    min-width: 50%;       /* minimum width set ki hai */
    max-width: 90%;  
    height: 2rem;
    white-space: nowrap;
    position: fixed;
    top: 2%;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1000;
    border-radius: 0.2rem;
    transition: transform 0.6s cubic-bezier(0.66, 0, 0.34, 1);  /* smooth 
    transition add ki */
}

.navbar.hidden {
    transform: translate(-50%, -140%);  /* navbar ko uper hide karne ke liye */
}

.logo a {
    color: #E4E3FF;
    font-size: 24px;
    font-family: ITALIC;
    font-weight: 100;
    text-decoration: none;
    display: flex;
    align-items: center;
  }

.logo img {
    width: 100%;
    max-width: 150px;  /* maximum width set ki hai */
    object-fit: contain;
}

.logo {
    overflow:hidden;
}

.nav-links {
    list-style: none;
    display: flex;
    gap: 1rem;
    /* width: 100%; Ensure nav-links take full width */
    justify-content: space-between; /* Space out links evenly */
}

.nav-links a {
    color: #E4E3FF;
    text-decoration: none;
    font-size: clamp(0.8rem, 1.2vw, 1rem);
    font-family: INTER;
    font-weight: 400;
    transition: color 0.3s ease;
}

/* Desktop-only hover effects */
@media (hover: hover) and (min-width: 768px) {
    .nav-links a:hover {
        color: #8f8ef0;
    }
    
    .dropdown:hover .dropdown-content {
        display: block;
    }
    
    .dropdown:hover .dropdown-icon {
        transform: rotate(180deg);
    }
    
    .dropdown:hover > a::after {
        transform: translateY(-50%) rotate(180deg);
    }
}

/* Desktop view */
@media (min-width: 1024px) {
    .nav-links a {
        font-size: 1rem;
    }
}

.menu-toggle {
    display: none;
    flex-direction: column;
    cursor: pointer;
}

.bar {
    height: 3px;
    width: 25px;
    background-color: #E4E3FF;
    margin: 4px 0;
}

.hero {
    background-image: url('your-image.jpg');
    background-size: cover;
    background-position: center;
    height: 200vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.hero-content h1 {
    color: #E4E3FF;
    font-size: 60px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.dropdown-menu {
    border-radius: 0.2rem;
  
    position: absolute;
    top: 100%;
    left: 0;
    background-color: #121212;
    list-style: none;
    padding: 0;
    margin: 0;
    overflow-y: scroll;
    max-height: 0;
    width: 100%;
    transition: max-height 0.8s cubic-bezier(0.66, 0, 0.34, 1), visibility 0.8s;
    z-index: 999;
    visibility: hidden;
    display: grid;
    align-items: start;
    grid-template-columns: repeat(4, 1fr);
}

.dropdown-menu::-webkit-scrollbar {
    width: 5px;
}

/* Track */
.dropdown-menu::-webkit-scrollbar-track {
    background: #333333;
}

/* Handle */
.dropdown-menu::-webkit-scrollbar-thumb {
 background: #8f8ef0;
}

.dropdown-links-wrapper{
    display: flex;
    align-items: start;
    justify-content: center;
    flex-direction: column;
    width: fit-content;
    padding: 1rem 0.5rem ;
    
}

.dropdown:hover .dropdown-menu,
.dropdown-menu.active {
    max-height: 300px;
    visibility: visible;
    z-index: 1000;
}

/* Existing dropdown styles */
.dropdown > a {
    position: relative;  /* Icon positioning ke liye */
    padding-right: 20px; /* Icon ke liye space */
}

/* Dropdown icon ke liye pseudo-element */
.dropdown > a::after {
    content: "▼";
    font-size: 0.7em;
    margin-left: 8px;
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    transition: transform 0.3s cubic-bezier(0.66, 0, 0.34, 1);
}

/* Active state mein rotation */
.dropdown:hover > a::after,
.dropdown.active > a::after {
    transform: translateY(-50%) rotate(180deg);
}


/* WAPIS ADD KARO HEADING STYLES */
.dropdown-heading {
    color: #8f8ef0;
    font-size: 1.3rem;
    margin-bottom: 10px;  /* Heading aur links ke beech space ke liye */
    font-family: ITALIC;
    font-weight: lighter;
}

/* REMOVE KARO SIRF WO STYLES JO ICON SE RELATED THAY */
/* (position aur padding-right nahi add karna) */

.hamburger {
  display: none; /* Desktop par hide */
  background: transparent;
  border: none;
  padding: 10px;
  cursor: pointer;
  z-index: 100;
}

.line {
  display: block;
  width: 20px;
  height: 1px;
  background: #8f8ef0;
  margin: 6px 0;
  transition: 0.4s;
}

/* Mobile view show karein */
@media (max-width: 768px) {
  .hamburger {
    display: block;
  }

  .nav-links {
    display: flex;
    flex-direction: column;
    width: 100%;
    position: absolute;
    top: 100%;
    left: 0;
    background-color: #121212;
    padding: 0;
    margin-top: 0rem;
    max-height: 0;
    overflow: scroll;
    visibility: hidden;
    border-radius: 0.2rem;
    gap: 0rem;

    transition: max-height 1s cubic-bezier(0.66, 0, 0.34, 1), visibility 1s;
  }

  .nav-links.active {
    max-height: 500px;
    visibility: visible;
  }

  .nav-links li {
    padding: 10px 20px;
  }

  .menu-toggle {
    display: flex;
  }

  .dropdown-menu {
    position: static;
    white-space: nowrap;
    display: block;
  }

  .dropdown-menu.active {
    display: block;
    max-height: 500px;
  }
  .navbar {
    padding: 10px 20px;
    min-width: 75%;     
  }
}

/* Active state animations */
.hamburger.active .line:first-child {
  transform: rotate(45deg) translate(4px, 0px);
}

.hamburger.active .line:nth-child(2) {
  transform: rotate(-45deg) translate(5px, -1px);
}

/* Hover effect for desktop */
@media (min-width: 768px) {
  .dropdown:hover .dropdown-content {
    display: block;
  }
  .dropdown:hover .dropdown-icon {
    transform: rotate(180deg);
  }
}

/* Mobile click handling */
@media (max-width: 767px) {
  .dropdown.active .dropdown-menu {
    max-height: 500px;
    visibility: visible;
  }
  
  .dropdown.active .dropdown-icon {
    transform: rotate(180deg);
  }
}

/* Shopify Specific CSS Fixes */
.nav-links.active {
  display: flex !important; /* Shopify's default display properties ko override kare */
  z-index: 9999 !important; /* Announcement bars se upar dikhane ke liye */
}

.dropdown.active {
  opacity: 1 !important;
  transform: translateY(0) scaleY(1) !important; /* Shopify transitions ko force kare */
  pointer-events: all !important;
}

/* Chrome tap highlight remove */
.dropdown {
  -webkit-tap-highlight-color: transparent;
}
```

```
// --------------------------
// DOM Elements Selection
// --------------------------
const navLinks = document.querySelector(".nav-links");
const dropdowns = document.querySelectorAll(".dropdown");
const hamburger = document.querySelector(".hamburger");
const navbar = document.querySelector(".navbar");

// --------------------------
// Dropdown Functionality
// --------------------------
function handleDropdown(e) {
  e.stopPropagation();

  // Mobile devices ke liye
  if (window.innerWidth < 768) {
    const currentDropdown = e.currentTarget;

    // Toggle current dropdown
    currentDropdown.classList.toggle("active");

    // Close other dropdowns
    dropdowns.forEach((drop) => {
      if (drop !== currentDropdown) {
        drop.classList.remove("active");
      }
    });
  }
}

// Click outside to close dropdowns
document.addEventListener("click", (e) => {
  if (window.innerWidth >= 768) return;

  const isClickInside = e.target.closest(".dropdown");

  if (!isClickInside) {
    dropdowns.forEach((dropdown) => {
      dropdown.classList.remove("active");
    });
  }
});

// --------------------------
// Hamburger Menu Toggle
// --------------------------
hamburger.addEventListener("click", () => {
  // Toggle menu visibility
  hamburger.classList.toggle("active");
  navLinks.classList.toggle("active");

  // Close all dropdowns when closing navbar
  if (!navLinks.classList.contains("active")) {
    dropdowns.forEach((dropdown) => {
      dropdown.classList.remove("active");
    });
  }
});

// --------------------------
// Scroll Behavior
// --------------------------
let lastScrollPosition = window.pageYOffset;

window.addEventListener("scroll", () => {
  if (window.innerWidth >= 768) {
    // Desktop check
    const currentScrollPosition = window.pageYOffset;

    // Hide/show navbar on scroll
    if (currentScrollPosition > lastScrollPosition) {
      navbar.classList.add("hidden");
    } else {
      navbar.classList.remove("hidden");
    }

    lastScrollPosition = currentScrollPosition;
  }
});

// --------------------------
// Initialize Event Listeners
// --------------------------
dropdowns.forEach((dropdown) => {
  dropdown.addEventListener("click", handleDropdown);
});
```

I want the mobile dropdown to open and close smoothly when clicked

---

## 190. How to Properly Display list.file_reference Metafield Images in Shopify Theme?
**Score:** 0 | **Tags:** shopify, liquid, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/79416432/how-to-properly-display-list-file-reference-metafield-images-in-shopify-theme

I'm working on a Shopify theme section that needs to display images stored in a list.file\_reference metafield. The metafield stores multiple images as references to Shopify’s Media Library (gid://shopify/MediaImage/...), but I’m struggling to retrieve and display them correctly.

**What I’ve Tried**

Retrieving the metafield value:

```
{% assign feature_images = product.metafields.accentuate.product_features_image %}
Looping through the values:

{% if feature_images and feature_images.size > 0 %}
    {% for feature_image in feature_images %}
        <img src="{{ feature_image | image_url }}" alt="Feature Image">
    {% endfor %}
{% endif %}
Debugging the metafield output: When I print feature_images using:

<pre>{{ feature_images | json }}</pre>
```

I get:

```
["gid://shopify/MediaImage/32558718288180", "gid://shopify/MediaImage/32558717075764"]
```

This confirms the metafield is correctly storing image references.

Matching the images with product.media:

```
{% for feature_image in feature_images %}
    {% assign media_id = feature_image | split: '/' | last | plus: 0 %}

    {% for media in product.media %}
        {% if media.id == media_id %}
            <img src="{{ media.preview_image.src }}" alt="Feature Image">
        {% endif %}
    {% endfor %}
{% endfor %}
```

But the images are still not displaying—the tag remains empty.

**Expected Behavior**

The section should loop through the metafield and display all images correctly.
Shopify's Media Library images should render using preview\_image.src.

**What’s Not Working**

The media.id extracted from gid://shopify/MediaImage/... does not match product.media.
Using image\_url or file\_url doesn’t work for gid://shopify/MediaImage/....

**Questions**

How can I properly retrieve and display images from a list.file\_reference metafield?

Am I correctly extracting the ID from gid://shopify/MediaImage/... and matching it with product.media?

Should I be using a different approach to display these images?

**Additional Information**

Metafield Type: list.file\_reference
Example Metafield Value:

```
["gid://shopify/MediaImage/32558718288180", "gid://shopify/MediaImage/32558717075764"]
```

Example product.media Debug Output:

```
[
    {
        "id": 32558718288180,
        "preview_image": {
            "src": "https://cdn.shopify.com/.../image1.jpg"
        }
    },
    {
        "id": 32558717075764,
        "preview_image": {
            "src": "https://cdn.shopify.com/.../image2.jpg"
        }
    }
]
```

Any help would be greatly appreciated!

---

## 191. Bug in javascript code for website transitions on scroll
**Score:** 0 | **Tags:** javascript, jquery, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/78592742/bug-in-javascript-code-for-website-transitions-on-scroll

Below is the js code which is running various animations on a webpage. As you scroll there is 4 text/picture sections that transition onto the page when a trigger point is hit.

```
$(document).ready(function() {
  var reapplyAnimation = function(element, animationClass) {

    void element.offsetWidth;

    $(element).addClass(animationClass);
  };

  $('.blob').each(function() {
    var blobElement = this;
    var animated = false;
    var section = $(blobElement).closest('.custom-image-text-section');
    $(section).addClass('hidden-on-load');
    
    new Waypoint({
      element: blobElement,
      handler: function(direction) {
        if (direction == 'down' && !animated) {
          
          $(section).removeClass('hidden-on-load');
          reapplyAnimation(blobElement, 'animated-fade-rotate');
          
          var relatedImage = $(blobElement).closest('.custom-image-text-section').find('.image-container img')[0];
          $(section).removeClass('hidden-on-load');
          reapplyAnimation(relatedImage, 'animated-slide-rotate');

          var textContainer = $(blobElement).closest('.custom-image-text-section').find('#text-container')[0];
          $(section).removeClass('hidden-on-load');
          reapplyAnimation(textContainer, 'animated-fade-in-slide-in-right');

          animated = true;
          this.destroy();
        }
      },
      offset: '45%' // Trigger point
    });
  });
});
```

It has been through many iterations so far to make the animation smooth and fade in from opacity 0 to 1 without firsth flashing (hence `void element.offsetWidth` to load the page again). At the moment on scroll only the first section correctly appears, the other three don't appear at all.

---

## 192. Checkout Page in Shopify
**Score:** 0 | **Tags:** shopify, liquid, checkout, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/78126280/checkout-page-in-shopify

I am working with a Shopify plus account, I have the Payment Screen page (3 pages).  
My problem is that I would like in the information screen under the contact section, to give the option to the user to choose the shipping method just like this:

[enter image description here](https://i.sstatic.net/l2vSA.png)

But I don't know how to do it, I have read about, checkout.liquid but it will stop being active in August and also about Checkout Extensibility but I can't figure out how to do it, no matter how much I read documentation.  
Any help?

---

## 193. Shopify Cart note not reliably submitting
**Score:** 0 | **Tags:** forms, shopify, shopify-template, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/77823210/shopify-cart-note-not-reliably-submitting

[![enter image description here](https://i.sstatic.net/6VYbL.png)](https://i.sstatic.net/6VYbL.png)

Hi!

I'm having an issue with a cart form submitting consistently.

Currently this is how [this page is code](https://haverford.com.au/cart).

1. I have a input box for customers to select their delivery notes (With a default option that writes to the Cart Note textbox).
2. This textbox is for customers so they can put in their own notes(optional).
3. There is a hidden textbox(css-display:none;) inside the form that has javascript to combine the options selected(from step 1 and 2) into the textbox.

Now the issue is it either submits the notes to shopify or the additional info but never both.
[![notes to shopify](https://i.sstatic.net/PIejq.png)](https://i.sstatic.net/PIejq.png)
[![additional info to shopify](https://i.sstatic.net/vVNoR.png)](https://i.sstatic.net/vVNoR.png)

```
<form data-cart-content="" data-cart-wrapper="" action="/cart" method="post" novalidate="" class="t4s-cartPage__form t4s-pr t4s-oh">
   <input
   id="delivery-leave"
   type="radio"
   name="attributes[Getting your delivery]"
   value="Leave in a safe place"
   >
   <select 
    id="choose-a-safe-location-to-leave-your-delivery" 
    name="attributes[Choose a safe location to leave your delivery.]"
   >
   <textarea 
    name="note" 
    id="CartSpecialInstructions" 
    class="t4s-cart-note__input" 
    placeholder="How can we help you?" spellcheck="false">
   </textarea>

   <textarea id="CartNote" placeholder="How can we help you?" spellcheck="false"></textarea>
</form>
```

I was expecting both the inputs and the cart note would submit to the order.

It only submits one or another, was there something I was missing? ie a shopify form submission limitation?

---

## 194. Shopify Increase and decrease product 2 by 2
**Score:** 0 | **Tags:** javascript, shopify, liquid, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/77805579/shopify-increase-and-decrease-product-2-by-2

I would like that on my shopify product page, the quantity selector adds 2 by 2 or decreases 2 by 2 the quantity sent in the cart.
The starting quantity must also be 2.
All that I succeeded, but where I block, it is that when we have already clicked on "+" and that we go down to 2, we can still click on "-" which makes us fall to 1 and it distorts everything...
How could I make that on the quantity 2 one can no longer click on the "-"?

Thank you very much for your help here is my current code:

```
                {% if product.tags contains 'Liquidation' and product.type contains 'Chaise' %}
                 
<div class="ProductForm__QuantitySelector" {{ block.shopify_attributes }}>
  {% if block.settings.show_label %}
    <span class="ProductForm__Label">{{ 'product.form.quantity' | t }}:</span>
  {% endif %}

  <div class="QuantitySelector QuantitySelector--large">
  <button type="button" class="QuantitySelector__Button Link Link--secondary" data-action="decrease-quantity" disabled>{% render 'icon' with 'minus' %}</button>
  <input type="text" id="quantity-input" class="QuantitySelector__CurrentQuantity" pattern="[0-9]*" name="quantity" value="2" aria-label="{{ 'product.form.quantity' | t }}">
  <button type="button" class="QuantitySelector__Button Link Link--secondary" data-action="increase-quantity">{% render 'icon' with 'plus' %}</button>
</div>

</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const decreaseButton = document.querySelector('[data-action="decrease-quantity"]');
  const increaseButton = document.querySelector('[data-action="increase-quantity"]');
  const quantityInput = document.getElementById('quantity-input');

  const updateDecreaseButtonState = () => {
    decreaseButton.disabled = parseInt(quantityInput.value) === 2;
  };

  // Mise à jour initiale de l'état du bouton de diminution
  updateDecreaseButtonState();

  decreaseButton.addEventListener('click', function() {
    let quantity = parseInt(quantityInput.value);
    if (quantity > 2) {
      quantity -= 1;
      quantityInput.value = quantity;
    } else {
      quantity -= 0;
      quantityInput.value = quantity;
    }
    updateDecreaseButtonState();
  });

  increaseButton.addEventListener('click', function() {
    let quantity = parseInt(quantityInput.value);
    quantity += 1;
    quantityInput.value = quantity;
    updateDecreaseButtonState();
  });

  quantityInput.addEventListener('change', function() {
    let quantity = parseInt(this.value);
    if (isNaN(quantity) || quantity < 2) {
      this.value = 2;
    } else if (quantity % 2 !== 0) {
      this.value = quantity + (2 - quantity % 2);
    }
    updateDecreaseButtonState();
  });
});



</script>

                    {% else %}
                  
                  <div class="ProductForm__QuantitySelector" {{ block.shopify_attributes }}>
                    {% if block.settings.show_label %}
                      <span class="ProductForm__Label">{{ 'product.form.quantity' | t }}:</span>
                    {% endif %}
                    
                  <div class="QuantitySelector QuantitySelector--large">
                      {% assign quantity_minus_one = line_item.quantity | minus: 1 %}
                      <button type="button" class="QuantitySelector__Button Link Link--secondary" data-action="decrease-quantity">{% render 'icon' with 'minus' %}</button>
                      <input type="text" class="QuantitySelector__CurrentQuantity" pattern="[0-9]*" name="quantity" value="1" aria-label="{{ 'product.form.quantity' | t }}">
                      <button type="button" class="QuantitySelector__Button Link Link--secondary" data-action="increase-quantity">{% render 'icon' with 'plus' %}</button>
                    </div>
                  </div>
        {% endif %}
```

---

## 195. Accessing metaobject referenced by variant metafield
**Score:** 0 | **Tags:** shopify, liquid, shopify-api, shopify-template, shopify-liquid | **Answered:** True
**Link:** https://stackoverflow.com/questions/77740395/accessing-metaobject-referenced-by-variant-metafield

This question was posted as a comment to a different question:

I'm trying to display color swatches in collection. I have metaobject defined which has color and its name. Then I have defined a metafield in variant and created link to metaobject.

Now, I am trying to access hex value of color through `variant.metafields.custom.color.value` (variant is current variant in for loop and custom is name space and color holds hex value) but instead of color I am getting gid links. @cyberspider789

---

## 196. Show out-of-stock shopify products at the last page of entire pagination
**Score:** 0 | **Tags:** pagination, shopify, liquid, shopify-template, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/77651033/show-out-of-stock-shopify-products-at-the-last-page-of-entire-pagination

I am trying to modify the **main-collection-product-grid.liquid** file to show the out-of-stock products to appear at the very end of the pagination on the Shopify collection page. To do that I have separated the products based on availability and ran two different loops.

First, I loop in-stock products, so they appear at top, and then the out-of-stock products which are displayed at the bottom. This works.

`{% assign in_stock_products = collection.products | where: 'available', true %} {% assign out_of_stock_products = collection.products | where: 'available', false %}`

The issue is, the out-of-stock products show up at the end of each page, but I want to show them at the very end of the page.

For example, I have a total 50 products and show 10 products per page. Five of them are out of stock. So, I have a total of 5 pages, and I want to show the out-of-stock product on the last page rather than at the end of each page.

Now, it's showing the out-of-stock products at the end of page 1, but what I am expecting is they should show up at the very last page.

Is it possible to achieve this with liquid?

I tried the following liquid code. It works but shows the out-of-stock products at the end of each pagination page, but I want to show them on the last page.

```
{%- paginate collection.products by 10 -%}

{% assign in_stock_products = collection.products | where: 'available', true %}
{% assign out_of_stock_products = collection.products | where: 'available',
false %}

<!-- Loop through in-stock products -->
{% for product in in_stock_products %} {{ product.title }}
<!-- ... out-of-stock product information ... -->
{% endfor %}

<!-- Loop through out-of-stock products -->
{% for product in out_of_stock_products %} {{ product.title }}
<!-- ... out-of-stck product information ... -->
{% endfor %} {% comment %}

{% endpaginate %}
```

---

## 197. How can I list products on a static page that are tagged by a tag that has the same name as my page?
**Score:** 0 | **Tags:** shopify, liquid, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/77098740/how-can-i-list-products-on-a-static-page-that-are-tagged-by-a-tag-that-has-the-s

I'd like to list products on my static page called "Haarentfernung". Each product that should be featured has a same named tag called "Haarentfernung".

So far I've managed to get the Products with the tag 'Haarentfernung'.

```
{% paginate collections.all.products by 999 %}
   {%- assign allItems = collections.all.products -%}
     {%- for items in allItems -%}
       {% assign testItem = items.tags | where: 'Haarentfernung'%}
         <p>{{ testItem }}test1</p> 
     {% endfor %}
{% endpaginate %}
```

However I'd like to make it dynamic with the element `page.title`. But using {{ page.title }} inside the where filter doesn't work

```
{% paginate collections.all.products by 999 %}
   {%- assign allItems = collections.all.products -%}
     {%- for items in allItems -%}
       {% assign testItem = items.tags | where: {{ page.title }} %}
         <p>{{ testItem }}test1</p> 
     {% endfor %}
{% endpaginate %}
```

also doesn't work with when in apostrophes

```
{% paginate collections.all.products by 999 %}
   {%- assign allItems = collections.all.products -%}
     {%- for items in allItems -%}
       {% assign testItem = items.tags | where: '{{ page.title }}' %}
         <p>{{ testItem }}test1</p> 
     {% endfor %}
{% endpaginate %}
```

Is there a solution that is simpler? Maybe totally different approach?

---

## 198. Trying to make a code only bundle in Shopify Dawn theme
**Score:** 0 | **Tags:** shopify, liquid, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/76050112/trying-to-make-a-code-only-bundle-in-shopify-dawn-theme

I'm trying to make a bundle in shopify using only liquid code. Like if I have a bag and it's added to cart, a jacket is added with it automatically. I'm a rookie in Shopify so if someone could give me some leads as in where should I start.

I tried adding an event listener for clicking on the ATC button but I can't extract the product id on the product page. I'm desperate for some leads on this 😭Thank you!
And how can I check that what's happening once the Add to cart button is clicked?

---

## 199. How to use multiple &#39;for&#39;, &#39;and&#39; in Shopify Liquid if statement?
**Score:** 0 | **Tags:** shopify, liquid, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/75779019/how-to-use-multiple-for-and-in-shopify-liquid-if-statement

I have this css with an 'if' statement:

```
    grid-template-columns: 1fr 1fr 1fr;
    {% if section.settings.video_position == 'top' and (section.settings.video_link != nil or section.settings.video != nil) %}
    grid-template-rows: 100px 50vw 2fr 1fr 1fr 1fr;
    {% else %}
    grid-template-rows: 1fr 2fr 1fr 1fr 1fr;
    {% endif %}
```

but this syntax throws an error:

> Liquid syntax error (line 404): Expected dotdot but found comparison in "section.settings.video\_position == 'top' and (section.settings.video\_link != nil or section.settings.video != nil)"

How can I use 'and' with multiple 'ors' in a statement like this?

---

## 200. Shopify Liquid Code for scalable image for desktop and mobile
**Score:** 0 | **Tags:** html, shopify, shopify-liquid | **Answered:** False
**Link:** https://stackoverflow.com/questions/75756201/shopify-liquid-code-for-scalable-image-for-desktop-and-mobile

Need some help with using Custom Liquid in Shopify. Basically I am using a custom liquid section to add an image. I know enough to get the image where I want, but the issue is when viewed on mobile, the image doesnt resize and flow off the screen.

I can do it with a video and get the results I am after, just need to do with video.

Below is the code I am putting in the custom liquid section for video and then also the code I am using for this image. **Basically I am just trying to get the image to scale like my video does.**
---Go easy on me, I dont know nada about this stuff--

**Code I use for video that gives the results I am after**

```
<style>
 
video { 
 
display: block;
margin: 0 auto;
width: 100%;
height: 30%;
 
}
 
</style> 
 
<video autoplay loop playsinline muted> 
<source src="VIDEO LINK HERE">
</video>
```

**What I have tried for this image that I need to scale the way the video does**

```
<center><p>
    <a href="PAGE LINK HERE">
    <img src=IMAGE LINK HERE" alt="">
    </a>
</p></center
```

Thanks for any help

---

