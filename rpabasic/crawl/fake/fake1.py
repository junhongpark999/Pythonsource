from email import header
from urllib.request import Request, urlopen
from fake_useragent import UserAgent


url = "https://sports.news.naver.com/news?oid=477&aid=0000364142"
try:
    UserAgent = UserAgent()
    headers = {"user_agent": UserAgent.chrome}

    request_url = Request(url, headers=headers)
    res = urlopen(request_url).read().decode("utf-8")
    # print(res)
    print(
        request_url.header_items()
    )  # [('Host', 'sports.news.naver.com'), ('User-agent', 'Python-urllib/3.10')]
except Exception as e:
    print(e)
