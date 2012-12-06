This is a report.

![Plot](plot.png)

## ks test

Here is ks-test:

{{ "\n".join(d['storage.json'].json_as_dict()['ks-test']) }}

## mtcars

Here is a table with mtcars info:

{{ d['storage.json'].json_as_dict()['mtcars'] }}

