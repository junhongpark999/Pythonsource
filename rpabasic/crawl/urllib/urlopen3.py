from importlib.resources import contents, path
import urllib.request as req


target_url = [
    "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5486%2F2022%2F05%2F23%2F0000211916_004_20220523104202986.jpg&type=sc960_832",
    "https://www.naver.com",
]

# 다운로드 받을 경로
path_list = [
    "./rabasic/crawl/download/son.png",
    "./rabasic/crawl/download/naver.html",
]


for i, url in enumerate(target_url):

    try:
        res = req.urlopen(url)
        contents = res.read()

        print("--------------------")
        print("Header info-{} : {}".format(i, res.info))
        print("http status : {}".format(i, res.info))
        print("--------------------")

        with open(path_list[i], "wb") as c:
            c.write(contents)
    except Exception as e:
        print(e)
    else:
        print("성공")
