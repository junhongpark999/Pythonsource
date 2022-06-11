# 영화진흥위원회 어제 날짜 박스 오피스 파일 저장
import urllib.request as req

# 다운로드 받을 경로
path = "./rabasic/crawl/download/"


try:

    url = "https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=f5eef3421c602c6cb7ea224104795888&targetDt=20220608"

    contents = req.urlopen(url).read().decode("utf-8")
except Exception as e:
    print(e)
else:

    with open(path + "movie.txt", "w", encoding="utf-8") as f:
        f.write(contents)

    print("성공")
