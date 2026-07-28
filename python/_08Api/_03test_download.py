import requests,json

url="https://jsonplaceholder.typicode.com/posts"
response=requests.get(url)
data=response.json()

#file=open("_01download.json","x")

with open("_01download.json","w") as file:
    title=[i["title"] for i in data[:5]]
    print(title)
        
    json.dump(title,file,indent=4)