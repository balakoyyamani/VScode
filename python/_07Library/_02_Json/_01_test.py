import json
#json to python distionary
x='{"name":"bala","age":21,"Dept":"IT"}'

y=json.loads(x)

print("Res : ",y)
print(y["name"])
print(x)