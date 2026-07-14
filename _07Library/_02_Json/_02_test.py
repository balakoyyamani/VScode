#python dictionary to Json
import json
x={"name":"Bala",
    "age":21,
    "dept":"IT"}
y=json.dumps(x)
print(x)
print(y)
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print(json.dumps(x, indent=4, sort_keys=True))