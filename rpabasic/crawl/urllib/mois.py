# 행정안전부 게시판 목록 가져오기

from urllib.request import urlopen
from urllib.parse import urlencode

url = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# print(params)

try:
    for c in params:
        param = urlencode(c)

        url = url + "?" + param
        print("url {}".format(url))

        data = urlopen(url).read().decode("utf-8")
        print()
        print(data)
except:
    print("Error")
