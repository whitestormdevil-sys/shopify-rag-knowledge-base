---
source: https://shopify.dev/docs/api/liquid/objects/template
---

Information about the current [template](/docs/themes/architecture/templates).

## Properties

[Anchor to](/docs/api/liquid/objects/template#template-directory) 

directory**directory** [string](/docs/api/liquid/basics#string)

:   The name of the template's parent directory.

    Returns `nil` if the template's parent directory is `/templates`.

[Anchor to](/docs/api/liquid/objects/template#template-name) 

name**name** [string](/docs/api/liquid/basics#string) from a set of values

:   The name of the template's [type](/docs/themes/architecture/templates#template-types).

    | Possible values |
    | --- |
    | 404 |
    | article |
    | blog |
    | cart |
    | collection |
    | list-collections |
    | customers/account |
    | customers/activate\_account |
    | customers/addresses |
    | customers/login |
    | customers/order |
    | customers/register |
    | customers/reset\_password |
    | gift\_card |
    | index |
    | page |
    | password |
    | product |
    | search |

[Anchor to](/docs/api/liquid/objects/template#template-suffix) 

suffix**suffix** [string](/docs/api/liquid/basics#string)

:   The custom name of an [alternate template](/themes/architecture/templates#alternate-templates).

    Returns `nil` if the default template is being used.

9

1

2

3

4

5

{

"directory": null,

"name": "product",

"suffix": null

}

##### Example

```liquid
{
  "directory": null,
  "name": "product",
  "suffix": null
}
```

Was this section helpful?

YesNo