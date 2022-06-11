from urllib.request import urlopen
from urllib.parse import urlencode


param = {"query": "영화"}
url = (
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&"
    + urlencode(param)
)

try:
    res = urlopen(url).read().decode("utf-8")
except:
    print("URL Error")
else:
    print(res)
