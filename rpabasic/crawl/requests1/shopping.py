import requests

url = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=GMP&durationDays=30&count=100&_=1654833643285"

# 순위, 제품명

res = requests.get(url)

for idx, item in enumerate(res.json(), 1):
    print(idx, item["product_name"])
