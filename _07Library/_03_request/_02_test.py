import requests
data={"name":"Bala",
      "Age":21}
response=requests.post("https://httpbin.org/post",
                       json=data)
print(response.json())
print(response.status_code)