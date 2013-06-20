### @export "fix-python-path"
import sys
sys.path.append("..")

### @export "import-fib"
from sharedcode.fibonacci import fib

### @export "call"
fib(10)
