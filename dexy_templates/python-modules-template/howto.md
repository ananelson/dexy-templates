This is an overview of using dexy to run a project where you
have library code which is shared among several scripts.

## Using Local Python Modules

There are two basic approaches to re-using python code in several different
scripts or examples, you can create a standalone python package which is
installed on the system, or you can have the shared code in local files.

The local file approach is simpler for the most part, and that's what we're
covering here.

The file we want to re-use is `fibonacci.py` located in the `sharedcode`
directory. Here is the whole file:

{{ d['sharedcode/fibonacci.py|pyg'] }}

There is an `__init__.py` file in the `sharedcode` directory as needed to make
the directory visible to python.

We want to use the `fib` method in a script `example1.py`:

{{ d['example1.py|pyg'] }}

Here is the output:

<pre>
{{ d['example1.py|py'] }}
</pre>

In order to be able to run the `example1.py` script using dexy, the
`fibonacci.py` file will need to be specified as an input to `example1.py`.
It's simplest to use a wildcard to make all `.py` files be inputs:

{{ d['dexy.yaml|idio']['example1'] }}

Specifying ".py" means that all the .py files are copied unchanged - they
aren't executed.

## Examples in a Subdirectory

The `example2` directory contains a file `use-fib.py`. Because we are in a
subdirectory we need to modfiy the python path to include the `sharedcode`
directory.

{{ d['example2/use-fib.py|idio|pycon|pyg']['fix-python-path'] }}

Then we can import the `fib` method in the usual way:

{{ d['example2/use-fib.py|idio|pycon|pyg']['import-fib'] }}

We can use the method:

{{ d['example2/use-fib.py|idio|pycon|pyg']['call'] }}

## Configuration

Here is the full `dexy.yaml` file for this project:

{{ d['dexy.yaml|pyg'] }}
