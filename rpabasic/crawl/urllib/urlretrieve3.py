# 저장하고 싶은 이미지
from email import header
import urllib.request as req

img_url = "http://upload2.inven.co.kr/upload/2019/02/02/bbs/i16230877122.gif"


# 다운로드 받을 경로
path = "./rpabasic/crawl/download/"


try:
    file1, header1 = req.urlretrieve(img_url, path + "son2.png")
except Exception as e:
    print(e)
else:
    print(header1)
