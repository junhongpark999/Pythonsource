from fake_useragent import UserAgent
from urllib.request import urlopen


userAgent = UserAgent()

print(userAgent.ie)
print(userAgent.msie)
print(userAgent.chrome)
print(userAgent.safari)
print(userAgent.opera)
print(userAgent.firefox)
print(userAgent.random)
