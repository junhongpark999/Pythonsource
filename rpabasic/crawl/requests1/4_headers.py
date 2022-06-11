from email import header
from urllib import response
import requests
from fake_useragent import UserAgent

headers = {"user-agent": UserAgent().chrome}

url = "https://httpbin.org/get"
res = requests.get(url, headers=headers)
print(res.text)
