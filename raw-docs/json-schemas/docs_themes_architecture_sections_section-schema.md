---
source: https://shopify.dev/docs/themes/architecture/sections/section-schema
---

`{% schema %}` tag for sections allows you to define the following section attributes and settings:

* [name](#name)
* [tag](#tag)
* [class](#class)
* [limit](#limit)
* [settings](#settings)
* [blocks](#blocks)
* [max\_blocks](#max_blocks)
* [presets](#presets)
* [default](#default)
* [locales](#locales)
* [enabled\_on](#enabled_on)
* [disabled\_on](#disabled_on)

These attributes and settings enable different customization options and preconfigurations of the section inside the theme editor.

Note

The `{% schema %}` tag is a Liquid tag. However, it doesn't output its contents, or render any Liquid included inside it.

**Note:**

The `{% schema %}` tag is a Liquid tag. However, it doesn't output its contents, or render any Liquid included inside it.

The following is an example of a valid section schema for the `Slideshow` section:

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

{% schema %}

{

"name": "Slideshow",

"tag": "section",

"class": "slideshow",

"limit": 1,

"settings": [

{

"type": "text",

"id": "title",

"label": "Slideshow"

}

],

"max\_blocks": 5,

"blocks": [

{

"name": "Slide",

"type": "slide",

"settings": [

{

"type": "image\_picker",

"id": "image",

"label": "Image"

}

]

}

],

"presets": [

{

"name": "Slideshow",

"settings": {

"title": "Slideshow"

},

"blocks": [

{

"type": "slide"

},

{

"type": "slide"

}

]

}

],

"locales": {

"en": {

"title": "Slideshow"

},

"fr": {

"title": "Diaporama"

}

},

"enabled\_on": {

"templates": ["\*"],

"groups": ["footer"]

}

}

{% endschema %}

Each section can have only a single `{% schema %}` tag, which must contain only valid JSON using the attributes listed below. The tag can be placed anywhere within the section file, but it can't be nested inside another Liquid tag.

Caution

Having more than one `{% schema %}` tag, or placing it inside another Liquid tag, will result in a syntax error when editing your theme code.

**Caution:**

Having more than one `{% schema %}` tag, or placing it inside another Liquid tag, will result in a syntax error when editing your theme code.

Consider making your section compatible with [app blocks](/docs/storefronts/themes/architecture/blocks/app-blocks). When you create app blocks, merchants can add app content to their theme without directly editing their theme code.

---

## [Anchor to name](/docs/storefronts/themes/architecture/sections/section-schema#name)name

The `name` attribute determines the section title that is shown in the theme editor. For example, the following schema returns the following output:

9

1

2

3

4

5

{% schema %}

{

"name": "Slideshow"

}

{% endschema %}

![name example](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/theme-editor/section-title-example-r-YQs7jr.png)

---

## [Anchor to tag](/docs/storefronts/themes/architecture/sections/section-schema#tag)tag

By default, when Shopify renders a section, it's wrapped in a `<div>` element with a unique `id` attribute:

9

1

2

3

<div id="shopify-section-[id]" className="shopify-section">

// Output of the section content

</div>

If you don't want to use a `<div>`, then you can specify which kind of HTML element to use with the `tag` attribute. The following are the accepted values:

* `article`
* `aside`
* `div`
* `footer`
* `header`
* `section`

For example, the following schema returns the following output:

9

1

2

3

4

5

6

{% schema %}

{

"name": "Slideshow",

"tag": "section"

}

{% endschema %}

9

1

2

3

<section id="shopify-section-[id]" className="shopify-section">

// Output of the section content

</section>

---

## [Anchor to class](/docs/storefronts/themes/architecture/sections/section-schema#class)class

When Shopify renders a section, it's wrapped in an HTML element with a class of `shopify-section`. You can add to that class with the `class` attribute:

9

1

2

3

4

5

6

7

{% schema %}

{

"name": "Slideshow",

"tag": "section",

"class": "slideshow"

}

{% endschema %}

9

1

2

3

<section id="shopify-section-[id]" class="shopify-section slideshow">

// Output of the section content

</section>

---

## [Anchor to limit](/docs/storefronts/themes/architecture/sections/section-schema#limit)limit

By default, there's no limit to how many times a section can be added to a template or section group. You can specify a limit of 1 or 2 with the `limit` attribute:

9

1

2

3

4

5

6

7

8

{% schema %}

{

"name": "Slideshow",

"tag": "section",

"class": "slideshow",

"limit": 1

}

{% endschema %}

---

## [Anchor to settings](/docs/storefronts/themes/architecture/sections/section-schema#settings)settings

You can create section specific [settings](/docs/storefronts/themes/architecture/settings/input-settings) to allow merchants to customize the section with the `settings` object:

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

{% schema %}

{

"name": "Slideshow",

"tag": "section",

"class": "slideshow",

"settings": [

{

"type": "text",

"id": "header",

"label": "Header"

}

]

}

{% endschema %}

Caution

All section setting IDs must be unique within each section. Having duplicate IDs within a section will result in an error.

**Caution:**

All section setting IDs must be unique within each section. Having duplicate IDs within a section will result in an error.

### [Anchor to Access section settings](/docs/storefronts/themes/architecture/sections/section-schema#access-section-settings)Access section settings

Section settings can be accessed through the [`section` object](/docs/api/liquid/objects/section#section-settings). Refer to [Access settings](/docs/storefronts/themes/architecture/settings#access-settings) to learn more.

Tip

If a section is [statically rendered](/docs/storefronts/themes/architecture/sections#statically-render-a-section), then there's only one instance of the section across all static renderings, as a result they all share the same section setting values.

**Tip:**

If a section is [statically rendered](/docs/storefronts/themes/architecture/sections#statically-render-a-section), then there's only one instance of the section across all static renderings, as a result they all share the same section setting values.

---

## [Anchor to blocks](/docs/storefronts/themes/architecture/sections/section-schema#blocks)blocks

You can create blocks for a section. Blocks are reusable modules of content that can be added, removed, and reordered within a section.

Blocks have the following attributes:

blocks attributes

| Attribute | Description | Required |
| --- | --- | --- |
| `type` | The block type. This is a free-form string that you can use as an identifier. You can access this value through the `type` attribute of the [`block` object](/docs/api/liquid/objects/block#block-type). | Yes |
| `name` | The block name, which will show as the block title in the theme editor. | Yes |
| `limit` | The number of blocks of this type that can be used. | No |
| `settings` | Any [input](/docs/storefronts/themes/architecture/settings/input-settings) or [sidebar](/docs/storefronts/themes/architecture/settings/sidebar-settings) settings that you want for the block. Certain settings might be used as the [title of the block in the theme editor](#show-dynamic-block-titles-in-the-theme-editor). | No |

The following is an example of including blocks in a section:

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

{% schema %}

{

"name": "Slideshow",

"tag": "section",

"class": "slideshow",

"settings": [

{

"type": "text",

"id": "title",

"label": "Slideshow"

}

],

"blocks": [

{

"name": "Slide",

"type": "slide",

"settings": [

{

"type": "image\_picker",

"id": "image",

"label": "Image"

}

]

}

]

}

{% endschema %}

Caution

All block names and types must be unique within each section, and all setting IDs must be unique within each block. Having duplicates will result in an error.

**Caution:**

All block names and types must be unique within each section, and all setting IDs must be unique within each block. Having duplicates will result in an error.

### [Anchor to Access block settings](/docs/storefronts/themes/architecture/sections/section-schema#access-block-settings)Access block settings

Block settings can be accessed through the [`block` object](/docs/api/liquid/objects/block#block-settings). Refer to [Access settings](/docs/storefronts/themes/architecture/settings#access-settings) to learn more.

Tip

If a section is [statically rendered](/docs/storefronts/themes/architecture/sections#statically-render-a-section), then there's only one instance of the section across all static renderings, meaning they all share the same block setting values.

**Tip:**

If a section is [statically rendered](/docs/storefronts/themes/architecture/sections#statically-render-a-section), then there's only one instance of the section across all static renderings, meaning they all share the same block setting values.

### [Anchor to Render blocks](/docs/storefronts/themes/architecture/sections/section-schema#render-blocks)Render blocks

You can render a section's blocks by looping over the `blocks` attribute of the [`section` object](/docs/api/liquid/objects/section#section-blocks):

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

{% for block in section.blocks %}

{% case block.type %}

{% when 'slide' %}

<div className="slide" {{ block.shopify\_attributes }}>

{{ block.settings.image | image\_url: width: 2048 | image\_tag }}

</div>

...

{% endcase %}

{% endfor %}

In the example above, each block's content is included inside a parent container, and that container has `{{ block.shopify_attributes }}` added as an attribute. Shopify's theme editor uses that attribute to identify blocks in its [JavaScript API](/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks#javascript-events).

If your block is a single element, then ensure that the element has this attribute.

Caution

Don't rely on the literal value of a [block's ID](/docs/api/liquid/objects/block#block-id) when you iterate over blocks. The ID is dynamically generated and is subject to change. The following is an example of relying on a literal value of a block's ID, which may break functionality in your theme if the ID changes:

9

1

2

3

4

5

{% for block in section.blocks %}

{%- if block.id == 'J6d9jV' -%}

<h1>{{ block.settings.heading }}</h1>

{% endif %}

{% endfor %}

**Caution:**

Don't rely on the literal value of a [block's ID](/docs/api/liquid/objects/block#block-id) when you iterate over blocks. The ID is dynamically generated and is subject to change. The following is an example of relying on a literal value of a block's ID, which may break functionality in your theme if the ID changes:

9

1

2

3

4

5

{% for block in section.blocks %}

{%- if block.id == 'J6d9jV' -%}

<h1>{{ block.settings.heading }}</h1>

{% endif %}

{% endfor %}

### [Anchor to Recommended blocks](/docs/storefronts/themes/architecture/sections/section-schema#recommended-blocks)Recommended blocks

You can highlight specific theme blocks in the block picker to make them easier to find. To do this, include the `@theme` block type along with your recommended blocks in the `blocks` array.

In this example, the `text`, `button`, and `_marquee` blocks appear immediately in the picker. Other available theme blocks remain accessible by selecting **Show all**.

9

1

2

3

4

5

6

"blocks": [

{ "type": "@theme" },

{ "type": "button" },

{ "type": "text" },

{ "type": "\_marquee" }

]

![Recommended blocks
example](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/theme-editor/recommended-blocks-B66-W9l_.png)

### [Anchor to Show dynamic block titles in the theme editor](/docs/storefronts/themes/architecture/sections/section-schema#show-dynamic-block-titles-in-the-theme-editor)Show dynamic block titles in the theme editor

In certain cases, the theme editor can display an input setting value as the title of a block in the theme editor sidebar. This can help merchants to identify and rearrange blocks in a section.

The theme editor checks [the `id` values](/docs/storefronts/themes/architecture/settings/input-settings#standard-attributes) of the settings in a block to determine the best one to use for the block title.

The theme editor uses settings with the following `id` values, in order of precedence:

1. `heading`
2. `title`
3. `text`

If a setting with a matching `id` value doesn't exist, then the block name is used as the title.

For example, this block with a setting `id` of `heading` displays in the sidebar with the title `Welcome to our store`.

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

"blocks": [

{

"name": "Announcement",

"type": "announcement",

"settings": [

{

"type": "text",

"id": "heading",

"default": "Welcome to our store",

"label": "Heading"

}

]

}

]

---

## [Anchor to max\_blocks](/docs/storefronts/themes/architecture/sections/section-schema#max_blocks)max\_blocks

There's a limit of 50 blocks per section. You can specify a lower limit with the `max_blocks` attribute.

Note

[Static blocks](/docs/storefronts/themes/architecture/blocks/theme-blocks/static-blocks) don't count toward this limit.

**Note:**

[Static blocks](/docs/storefronts/themes/architecture/blocks/theme-blocks/static-blocks) don't count toward this limit.

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

{% schema %}

{

"name": "Slideshow",

"tag": "section",

"class": "slideshow",

"max\_blocks": 5,

"settings": [

{

"type": "text",

"id": "title",

"label": "Slideshow"

}

],

"blocks": [

{

"name": "Slide",

"type": "slide",

"settings": [

{

"type": "image\_picker",

"id": "image",

"label": "Image"

}

]

}

]

}

{% endschema %}

![max_blocks example](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/theme-editor/max_blocks-example-BLBQCOHd.png)

---

## [Anchor to presets](/docs/storefronts/themes/architecture/sections/section-schema#presets)presets

Presets are predefined section configurations that merchants can select when adding sections to a [JSON template](/docs/storefronts/themes/architecture/templates/json-templates). Presets help you quickly provide merchants with different layouts and use cases by adjusting section settings. For example, a "Testimonials" section might include presets for a single testimonial, a carousel, and a grid layout.

Note

Section presets are different from the presets used to define [theme presets](/docs/storefronts/themes/architecture/config/settings-data-json#theme-presets) in the `settings_data.json` file.

**Note:**

Section presets are different from the presets used to define [theme presets](/docs/storefronts/themes/architecture/config/settings-data-json#theme-presets) in the `settings_data.json` file.

Presets appear in the **Add section** picker as follows:

![add_section_example](https://cdn.shopify.com/shopifycloud/shopify-dev/production/assets/assets/images/themes/theme-editor/add-section-DdDu-n_F.png)

| Number | Description |
| --- | --- |
| 1 | Presets appear alphabetically based on their `name` attribute. |
| 2 | Presets can optionally be grouped into collapsible categories using the `category` attribute. |
| 3 | Uncategorized presets are always displayed first. |
| 4 | The theme editor automatically generates a preset preview. You can further customize this preview using [visual preview mode](/docs/storefronts/themes/best-practices/editor/integrate-sections-and-blocks#detect-the-theme-editor-visual-preview). |

Section presets have the following attributes:

| Attribute | Description | Required |
| --- | --- | --- |
| `name` | The preset name displayed in the theme editor's **Add section** picker and sidebar, and is persisted in the JSON template when you add a section. | Yes |
| `category` | Groups related presets together in the theme editor's **Add section** picker. | No |
| `settings` | Default values for settings you want to pre-populate. Each entry includes the setting name and its value. | No |
| `blocks` | Default blocks included in the preset. Each block entry must include a `type` attribute matching the block type, and a `settings` object formatted similarly to the `settings` attribute above.   Optionally, include a `name` attribute to display when merchants add the block in the editor. | No |

Here's an example of how presets are defined within a section schema:

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

{% schema %}

{

"name": "Slideshow",

"tag": "section",

"class": "slideshow",

"max\_blocks": 5,

"settings": [

{

"type": "text",

"id": "title",

"label": "Slideshow"

}

],

"blocks": [

{

"name": "Slide",

"type": "slide",

"settings": [

{

"type": "image\_picker",

"id": "image",

"label": "Image"

}

]

}

],

"presets": [

{

"name": "Slideshow",

"category": "Banners",

"settings": {

"title": "Slideshow"

},

"blocks": [

{

"type": "slide"

},

{

"type": "slide"

}

]

}

]

}

{% endschema %}

Tip

Sections with presets shouldn't be [statically rendered](/docs/storefronts/themes/architecture/sections#statically-render-a-section). If you're going to statically render a section, then you should use [default settings](#default).

**Tip:**

Sections with presets shouldn't be [statically rendered](/docs/storefronts/themes/architecture/sections#statically-render-a-section). If you're going to statically render a section, then you should use [default settings](#default).

---

## [Anchor to default](/docs/storefronts/themes/architecture/sections/section-schema#default)default

If you statically render a section, then you can define a default configuration with the `default` object, which has the same attributes as the [preset object](#presets).

The following is an example of including a default in a section:

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

{% schema %}

{

"name": "Slideshow",

"tag": "section",

"class": "slideshow",

"max\_blocks": 5,

"settings": [

{

"type": "text",

"id": "title",

"label": "Slideshow"

}

],

"blocks": [

{

"name": "Slide",

"type": "slide",

"settings": [

{

"type": "image\_picker",

"id": "image",

"label": "Image"

}

]

}

],

"default": {

"settings": {

"title": "Slideshow"

},

"blocks": [

{

"type": "slide"

},

{

"type": "slide"

}

]

}

}

{% endschema %}

Tip

You should only use the section `default` attribute for sections that will be reused, or installed on multiple themes or shops. Statically rendered sections that come pre-installed on a theme should have their default configuration defined by the `default` attribute for each individual setting.

**Tip:**

You should only use the section `default` attribute for sections that will be reused, or installed on multiple themes or shops. Statically rendered sections that come pre-installed on a theme should have their default configuration defined by the `default` attribute for each individual setting.

---

## [Anchor to locales](/docs/storefronts/themes/architecture/sections/section-schema#locales)locales

Sections can provide their own set of translated strings through the `locales` object. This is separate from the `locales` directory of the theme, which makes it a useful feature for sections that are meant to be installed on multiple themes or shops.

The `locales` object has the following general format:

9

1

2

3

4

5

6

7

{

"locales": {

"language": {

"translation\_key": "translation\_value"

}

}

}

For example:

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

{% schema %}

{

"name": "Slideshow",

"tag": "section",

"class": "slideshow",

"max\_blocks": 5,

"settings": [

{

"type": "text",

"id": "title",

"label": "Slideshow"

}

],

"blocks": [

{

"name": "Slide",

"type": "slide",

"settings": [

{

"type": "image\_picker",

"id": "image",

"label": "Image"

}

]

}

],

"default": {

"settings": {

"title": "Slideshow"

},

"blocks": [

{

"type": "slide"

},

{

"type": "slide"

}

]

},

"locales": {

"en": {

"title": "Slideshow"

},

"fr": {

"title": "Diaporama"

}

}

}

{% endschema %}

Any translations will show up under the **Sections** tab of the language editor for merchants to edit. When edits are made, the changes are saved directly to the applicable locale file, and the section schema is unchanged.

These translations can be accessed through the Liquid [translation filter](/docs/api/liquid/filters/translate) (`t` filter) where the key will be in the following format:

9

1

sections.[section-name].[translation-description]

For example, if you want to reference the `title` translation from the example above, then use the following:

9

1

{{ 'sections.slideshow.title' | t }}

---

## [Anchor to enabled\_on](/docs/storefronts/themes/architecture/sections/section-schema#enabled_on)enabled\_on

You can restrict a section to certain template page types and section group types by specifying them through the `enabled_on` attribute.

`enabled_on`, along with `disabled_on`, replaces the `templates` attribute.

Caution

You can use only one of `enabled_on` or [`disabled_on`](#disabled_on).

**Caution:**

You can use only one of `enabled_on` or [`disabled_on`](#disabled_on).

`enabled_on` must have at least one of the following attributes:

enabled\_on attributes

| Attribute | Description |
| --- | --- |
| `templates` | A list of the template page types where the section can be used.  Accepted values:   * A list of [page types](/docs/api/liquid/objects/request#request-page_type) * `["*"]` (all template page types) |
| `groups` | A list of the section groups where the section can be used.  Accepted values:   * A list of the section group types. Accepted values: `header`, `footer`, `aside`, and custom types in the format `custom.<NAME>`. * `["*"]` (all section group types) |

In the following example, the section is available to all templates, and to the `footer` section group:

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

{% schema %}

{

"name": "Slideshow",

"tag": "section",

"class": "slideshow",

"max\_blocks": 5,

"settings": [

{

"type": "text",

"id": "title",

"label": "Slideshow"

}

],

"blocks": [

{

"name": "Slide",

"type": "slide",

"settings": [

{

"type": "image\_picker",

"id": "image",

"label": "Image"

}

]

}

],

"default": {

"settings": {

"title": "Slideshow"

},

"blocks": [

{

"type": "slide"

},

{

"type": "slide"

}

]

},

"locales": {

"en": {

"title": "Slideshow"

},

"fr": {

"title": "Diaporama"

}

},

"enabled\_on": {

"templates": ["\*"],

"groups": ["footer"]

}

}

{% endschema %}

---

## [Anchor to disabled\_on](/docs/storefronts/themes/architecture/sections/section-schema#disabled_on)disabled\_on

You can prevent a section from being used on certain template page types and section group types by setting them in the `disabled_on` attribute. When you use `disabled_on`, the section is available to all templates and section groups except the ones that you specified.

`disabled_on`, along with `enabled_on`, replaces the `templates` attribute.

Caution

You can use only one of [`enabled_on`](#enabled_on) or `disabled_on`.

**Caution:**

You can use only one of [`enabled_on`](#enabled_on) or `disabled_on`.

`disabled_on` must have at least one of the following attributes:

disabled\_on attributes

| Attribute | Description |
| --- | --- |
| `templates` | A list of the template page types where the section can't be used.  Accepted values:   * A list of [page types](/docs/api/liquid/objects/request#request-page_type) * `["*"]` (all template page types) |
| `groups` | A list of the section groups where the section can't be used.  Accepted values:   * A list of the section group types. Accepted values: `header`, `footer`, `aside`, and custom types in the format `custom.<NAME>`. * `["*"]` (all section group types) |

In the following example, the section is available to all templates other than `password` templates, and to all section groups other than `footer` section groups.

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

{% schema %}

{

"name": "Slideshow",

"tag": "section",

"class": "slideshow",

"max\_blocks": 5,

"settings": [

{

"type": "text",

"id": "title",

"label": "Slideshow"

}

],

"blocks": [

{

"name": "Slide",

"type": "slide",

"settings": [

{

"type": "image\_picker",

"id": "image",

"label": "Image"

}

]

}

],

"default": {

"settings": {

"title": "Slideshow"

},

"blocks": [

{

"type": "slide"

},

{

"type": "slide"

}

]

},

"locales": {

"en": {

"title": "Slideshow"

},

"fr": {

"title": "Diaporama"

}

},

"disabled\_on": {

"templates": ["password"],

"groups": ["footer"]

}

}

{% endschema %}

---

Was this page helpful?

YesNo