Developer Docs
==============

.. contents::

{% from "dexy.jinja" import code, codes, ext with context %}

Models
------

The `models` module is imported from django:

{{ codes("example_com/polls/models.py|idio", "models") }}

We define a Poll class:

{{ codes("example_com/polls/models.py|idio", "poll") }}

And a Choice class:

{{ codes("example_com/polls/models.py|idio", "choice") }}

Here are the fields defined for Poll:

{{ codes("example_com/polls/models.py|idio", "poll-fields") }}

And for Choice:

{{ codes("example_com/polls/models.py|idio", "choice-fields") }}

Each defines a descriptive `__unicode__` method:

{{ codes("example_com/polls/models.py|idio", "poll-unicode") }}
{{ codes("example_com/polls/models.py|idio", "choice-unicode") }}

We also have a `was_published_recently` method defined on Poll:

{{ codes("example_com/polls/models.py|idio", "recent") }}

And some unit tests for this method:

{{ codes("example_com/polls/tests.py|idio", "old-poll") }}
{{ codes("example_com/polls/tests.py|idio", "recent-poll") }}
{{ codes("example_com/polls/tests.py|idio", "future-poll") }}

Here are the results of running unit tests on the polls app::
    
    {{ d['/scripts/run-tests.sh|shint'] | indent(4) }}


Site Config
-----------

URL routing is defined in a site-wide urls.py:

{{ code("example_com/example_com/urls.py|idio") }}

And a separate urls.py in the polls app:

{{ code("example_com/polls/urls.py|idio") }}


Admin Interface
---------------

Django provides a ready-made admin interface. The admin interface is activated
in `settings.py` as follows:

{{ codes('/example_com/example_com/settings.py|idio', 'installed-apps') }}

The base template for the admin section is:

{{ code("example_com/templates/admin/base_site.html|idio") }}

Here is what the main admin page looks like:

.. image:: logged-in-admin.png

The admin interface for polls is configured in the polls app:

{{ code('example_com/polls/admin.py|idio') }}

Further config is attached to the `Poll` class:

{{ codes("example_com/polls/models.py|idio", "admin-config") }}

Here is the polls admin:

.. image:: polls-admin.png

Let's add a new poll:

{{ codes("screenshots.js|idio", "add-new-poll") }}

.. image:: add-new-poll-filled-in.png

Here's our new poll:

.. image:: poll-added.png

Views
-----

Here is the URL routing for the polls app:

{{ code("example_com/polls/urls.py|idio") }}

Index
.....

{{ codes("example_com/polls/views.py|idio", "index") }}

{{ code("example_com/polls/templates/polls/index.html|idio") }}

Here's how this looked at the start:

.. image:: no-polls-available.png

Here's how this looks after adding a poll via the admin interface:

.. image:: index.png

Detail
......

{{ codes("example_com/polls/views.py|idio", "detail") }}

{{ code("example_com/polls/templates/polls/detail.html|idio") }}

.. image:: voting.png

Results
.......

{{ codes("example_com/polls/views.py|idio", "results") }}

{{ code("example_com/polls/templates/polls/results.html|idio") }}

.. image:: voted.png

.. image:: many-votes.png
