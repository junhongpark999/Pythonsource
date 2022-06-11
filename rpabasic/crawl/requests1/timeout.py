import requests

url = "https://api.github.com/events"

res = requests.get(url, timeout=0.001)  # url이 시간안에 오지않으면 에러로 처리
print(res.text)
