Creating Django Projects
------------------------

{% from 'dexy.jinja' import code, codes, ext with context %}

First, check the django version:

    {{ codes('/scripts/create-project.sh|idio', 'check-version') }}

Next, create a project:

    {{ codes('/scripts/create-project.sh|idio', 'create-project') }}

Here are the files:

    {{ codes('/scripts/create-project.sh|idio', 'tree') }}
