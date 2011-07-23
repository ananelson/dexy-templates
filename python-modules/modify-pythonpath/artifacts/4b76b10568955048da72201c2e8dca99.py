### @export "add-parent-to-pythonpath"
import sys
sys.path.append("..")

### @export "call-module"
import demomodule
print demomodule.abc()

