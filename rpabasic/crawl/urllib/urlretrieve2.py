from email import header
import urllib.request as req

# 이미지, html 파일 다운로드


img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5486%2F2022%2F05%2F23%2F0000211916_004_20220523104202986.jpg&type=sc960_832"
file_url = "https://www.naver.com"

# 다운로드 받을 경로
path = "./rpabasic/crawl/download/"

try:
    file1, header1 = req.urlretrieve(img_url, path + "son.png")
    file2, header2 = req.urlretrieve(file_url, path + "naver.html")
except Exception as e:
    print(e)
else:
    print(header1)
    print()
    print(header2)
