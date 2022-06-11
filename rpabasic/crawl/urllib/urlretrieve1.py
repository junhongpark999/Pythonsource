# URL 작업 - urllib 라이브러리 존재

# request - 1) urlretrieve() : 요청하는 url의 정보를 파일로 저장
#                            : 리턴값이 튜플 형태로 옴
#                            : csv 파일, api 데이터 등 많은 양의 데이터를 한번에 저장

import urllib.request as req

url = "http://google.com"
# 다운로드 받을 경로
path = "./rpabasic/crawl/download/"

try:
    file1, header1 = req.urlretrieve(url, path + "google.html")
except Exception as e:
    print(e)
else:
    print(header1)
    print("성공")
