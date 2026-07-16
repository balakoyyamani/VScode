import requests
url="https://jsonplaceholder.typicode.com/posts"
response=requests.get(url)
data=response.json()
print(response.status_code)

#loop

for i in data[-1:-3]:
    print("\n")
    print(i["title"])