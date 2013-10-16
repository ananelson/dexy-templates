### @export "assign-variables"
x = 5
y = 7

### @export "multiply"
x * y

### @export "save-some-json-data"

data = {
        'foo' : 123,
        'bar' : "this is a string",
        'baz' : None
        }

import json
with open("data.json", 'wb') as f:
    json.dump(data, f)
