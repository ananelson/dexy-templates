## Working with Python Modules

Here is a module we wish to include in our Dexy document:

{{ d['demomodule.py|pyg'] }}

And we want to call this in a script, like so:
{{ d['demo-script.py|idio']['call-module'] }}

This works when you run this from the command line, but it won't work within Dexy. This is because Python looks for a file named demomodule.py somewhere in the pythonpath. The pythonpath automatically includes the "." directory, but when Dexy runs your file it actually runs a copy of your file sitting in the artifacts/ directory.

There are several ways to include your module. The best way is to put your module into a proper Python package and install this on your system. If you install this with the 'develop' option then any changes you make will appear straight away.

However, this might be overkill if you just have a small module. In this case the easiest thing to do is to add ".." to the pythonpath. you can do this like so:

{{ d['demo-script.py|idio']['add-parent-to-pythonpath'] }}

Because Dexy is running your python script in artifacts, this line adds your dexy project root to the pythonpath and so it will find your original file.

If you use idiopidae to divide your script into sections, then you don't need to show this part of the script. You can just show the interesting part:

{{ d['demo-script.py|idio|pycon|pyg']['call-module'] }}

You should [read more](http://docs.python.org/tutorial/modules.html#the-module-search-path) about Python module search paths if you try this.

It is possible for Dexy to be set up to do this automatically, if you are interested in this then you may wish to follow [this story](https://www.pivotaltracker.com/story/show/16163251).
