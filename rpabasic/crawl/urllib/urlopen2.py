from logging import exception
import urllib.request as req

try:
    url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
    res = req.urlopen(url)
    content = res.read().decode("euc-kr")
except Exception as e:
    print(e)
else:
    print(res[:3000])
    print(res.info())
