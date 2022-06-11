# 모듈 : 함수나 변수 또는 클래스들을 모아 놓은 파일

# import sys

# print(sys.builtin_module_names)


# import math # math 안에 있는 모든 것들이 import

# print(dir(math))
# print(math.__doc__) #  defined by the C standard
# print(math.ceil(3.14))
# print(math.sin(1))
# print(math.cos(1))
# print(math.floor(2.4))


# import random

# # 0.0 <= x < 1.0 리턴
# print(random.random())

# # 지정한 범위 사이의 임의의 수 리턴
# print(random.uniform(10, 20))


# # randrange(max) : 0 ~ max 사이의 임의의 수 리턴
# # randrange(min, max) : min ~ max 사이의 임의의 수 리턴
# print(random.randrange(10))

# # choice(list) : 리스트 내부의 요소 중에서 임의의 수 리턴
# print(random.choice([1, 2, 3, 4, 5, 6, 7]))

# # shuffle(list) : 리스트 내부의 요소 섞기
# list1 = [1, 2, 3, 4, 5, 6, 7]
# print("Shuffle 전 ", list1)
# random.shuffle(list1)
# print("shuffle 후 ", list1)

# # sample(list, 숫자) : 리스트 요소 중에서 숫자 만큼 추출
# print(random.sample([1, 2, 3, 4, 5, 6, 7], k=2))



import time

print("지금부터 5초간 정지")
time.sleep(5)
print("프로그램 종료")