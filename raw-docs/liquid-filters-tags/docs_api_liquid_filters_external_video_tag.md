---
source: https://shopify.dev/docs/api/liquid/filters/external_video_tag
---

9

1

variable | external\_video\_tag

returns [string](/docs/api/liquid/basics#string)

Generates an HTML `<iframe>` tag containing the player for a given external video. The input for the `external_video_tag`
filter can be either a [`media` object](/docs/api/liquid/objects/media) or [`external_video_url`](/docs/api/liquid/filters/external_video_url).

If [alt text is set on the video](https://help.shopify.com/en/manual/products/product-media/add-alt-text), then it's
included in the `title` attribute of the `<iframe>`. If no alt text is set, then the `title` attribute is set to the
product title.

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

[Anchor to HTML attributes](/docs/api/liquid/filters/external_video_tag#external_video_tag-html-attributes)

### HTML attributes

9

1

variable | external\_video\_tag: attribute: string

You can specify [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attributes) by adding a parameter that matches the attribute name, and the desired value.

9

1

2

3

4

5

6

7

{% for media in product.media %}

{% if media.media\_type == 'external\_video' %}

{% if media.host == 'youtube' %}

{{ media | external\_video\_url: color: 'white' | external\_video\_tag: class:'youtube-video' }}

{% endif %}

{% endif %}

{% endfor %}

##### Code

```liquid
{% for media in product.media %}
  {% if media.media_type == 'external_video' %}
    {% if media.host == 'youtube' %}
      {{ media | external_video_url: color: 'white' | external_video_tag: class:'youtube-video' }}
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

<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" class="youtube-video" src="https://www.youtube.com/embed/vj01PAffOac?color=white&amp;controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>

##### Output

```liquid
<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" class="youtube-video" src="https://www.youtube.com/embed/vj01PAffOac?color=white&amp;controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>
```

Was this page helpful?

YesNo