import requests,json
url="https://jsonplaceholder.typicode.com/posts"
response=requests.get(url)
if response.status_code == 200:
    data=response.json()

    print(len(data))
    print(data[0]["title"])
    print(data[-1]["title"])
    title=[i["title"] for i in data[:5]]
    print(title)
