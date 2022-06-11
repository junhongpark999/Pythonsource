# get(), post(), delete(), put() == REST

import requests


url = "https://httpbin.org/get"

param = {"name": "hong"}

# parameter 없을 때
# res = requests.get(url)
res = requests.get(url, params=param)

print(res.headers)
print(res.text)

# post 방식 : data 속성
# url = "https://httpbin.org/post"
# data = {"name": "hong"}

# res = requests.post(url, data=data)
# print(res.text)


# delete 방식
# url = "https://httpbin.org/delete"
# res = requests.delete(url)
# print(res.text)

# put 방식
# url = "https://httpbin.org/put"

# data = {"name": "kim"}

# res = requests.put(url, data=data)
# print(res.text)
