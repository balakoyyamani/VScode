import json

x={"Name":"Bala",
   "Age":21,
   "Dept":"IT"}

with open("basic.json","w") as file:
    json.dump(x,file,indent=4)
