<h2 class="title">Sites in Dexy</h2>

<p class="subtitle">How to Use the Website Reporter</p>

Contents:

[TOC]

### The WebsiteReporter

The WebsiteReporter helps you generate a website from your Dexy output. It
helps you do things like apply HTML templates and automatically generate page
navigation.

The WebsiteReporter won't run by default. You need to use the `--reports` command line option to customize which reports dexy runs. If you are making a website, you will probably want the WebsiteReporter to run every time you run dexy, so instead of typing this on the command line each time, you can put it in a config file like this:

{{ d['/dexy.conf|pyg'] }}

This means that only the WebsiteReporter and RunReporter will run, so you won't see the `output/` and `output-long/` directories you're used to. You can always add them to the list if you still want them. You can see a list of all the available reporters like this:

{{ d['/list-reports.sh|shint|pyg'] }}

The alias is what you add to the --reports list, which should be a string where each alias is separated by a space.

The WebsiteReporter will copy all non-HTML files to the `output-site/` directory unchanged. When it encounters a HTML file, it will look to see if there is already a header and, if so, it will leave that file alone. If the HTML appears to be just internal page content, then the WebsiteReporter will look for a file named `_template.html` and will apply that template.

### Finding Templates

The WebsiteReporter looks first in the same directory as the file being processed, then it looks in each succeeding parent directory as far up as the project root, until it finds a file named `_template.html`. It uses the first one it finds (i.e. the one closest to the HTML document being processed). If it does not find one, it raises a UserFeedback exception to let you know. You can tell the WebsiteReporter not to try to apply a template by setting the `ws_template` argument to False, as in this example:

{{ d['/dexy.yaml|idio']['source'] }}

You can also specify another file to use as a template, as in this example:

{{ d['/dexy.yaml|idio']['docs'] }}

### The content Tag

The templates are jinja templates. Here is a very simple template which only uses a single tag, `content`, to insert the content of the page it is processing:

{{ d['_simple_template.html|pyg'] }}

{{ d['simple_content.html|pyg'] }} [link to page rendered in template](simple_content.html)

If the page content is split into named sections, these sections can be referenced as attributes of `content`.

{{ d['_head_body_template.html|pyg'] }}

For example, this HTML source is split into sections by the `htmlsections` filter, and then the named sections are placed into the relevant spots in the template.

{{ d['head_body_content.html|pyg'] }} [link to page rendered in template](head_body_content.html)

Here is the `dexy.yaml` for these pages:

{{ d['dexy.yaml|idio']['content-demos'] }}

### Jinja Templates and Macros

The WebsiteReporter lets you make use of jinja's [template inheritance](http://jinja.pocoo.org/docs/templates/#template-inheritance) and [macros](http://jinja.pocoo.org/docs/templates/#macros). The dexy project root and the directory containing the page being processed are passed to jinja's FileSystemLoader, so you can reference templates and macro files relative to either of these locations.

For this website, we define a `_base.html` template:

{{ d['/_base.html|pyg'] }}

We can break our layout into manageable sections by using jinja's include statements to insert snippets into our template, and by defining blocks we can use jinja's inheritance to customize these blocks in other templates. Here is our generic site-side `_template.html`

{{ d['/_template.html|pyg'] }}

And here is a custom template for the home page:

{{ d['/_home_template.html|pyg'] }}

### Navigation and Meta Goodies

In addition to referencing the page content of the page the template is being applied to, the WebsiteReporter also generates helpers for site navigation and similar utilities.

We can see this in the navigation menu macro:

{{ d['/macros/nav.jinja|pyg'] }}

Here is a page showing all the objects which are available to WebsiteReporter templates:

[link to page which introspects on other stuff](introspect.html)
