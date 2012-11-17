# Code Journal

## A Python/Numpy/Matplotlib Example

First we import matplotlib and other libraries:
{{ d['code001.py|idio|pycon|pyg']['imports'] }}

We tell pyplot to use Agg backend, since we want to save graphs to images. Then we import pyplot:
{{ d['code001.py|idio|pycon|pyg']['pyplot'] }}

Generate random data and plot a histogram:
{{ d['code001.py|idio|pycon|pyg']['hist'] }}

Save the histogram to a png file:
{{ d['code001.py|idio|pycon|pyg']['save'] }}

Here is the graph:

![A Histogram](pyplot-hist-example.png)

## A Python CSV Example

Here is some CSV data

<pre>
{{ d['data.csv'] }}
</pre>

{{ d['code002.py|idio|pycon|pyg']['import-data'] }}

{{ d['code002.py|idio|pycon|pyg']['graph-data'] }}

![xy plot from csv data](pyplot-xy-example.png)
