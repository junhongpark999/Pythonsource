# pip install requests
# requests
# urllib 라이브러리 보다 간단한 방법으로 request 처리
# 디토딩도 알아서 해줌
# json 처리도 편함

import requests

# get 방식
res = requests.get("http://www.naver.com")

# 응답 확인
print(res.text)

# 응답 상태
print(res.status_code)  # 200

print(res.ok)  # True
