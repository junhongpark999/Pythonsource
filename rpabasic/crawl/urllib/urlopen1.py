# request - 2) urlopen(): 다운로드는 하지 않고 정보를 메모리에 올려서 분석
#                read() :


import urllib.request as req

weather_url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"

res = req.urlopen(weather_url).read().decode("utf-8")

print(res[:4000])
