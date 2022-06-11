# 파일 읽고 쓰기

# open("파일명",모드,encoding...) : 파일을 읽거나 쓸때 사용
# with + open() : close()를 알아서 해 줌

# f = open("data/test1.txt","w",encoding="UTF-8")
# f.write("안녕하세요\n반갑습니다.")
# f.close()
# print(dir(f))

with open("data/test1.txt","w",encoding="UTF-8") as f:
    f.write("안녕하세요\n반갑습니다.")









# w : 기존에 있던 내용은 무시하고 새로 작성  :  write
# a : 기존에 있던 내용 뒤로 덧붙이기  : append

# 1 ~ 10까지 파일로 작성
# f = open("data/test1.txt","a",encoding="utf-8")
# for i in range(1,11):
#     f.write("%d\n" % i)
# f.close()

with open("data/test1.txt","a",encoding="utf-8") as f:
    for i in range(1,11):
        f.write("%d\n" % i)




# list 를 파일로 작성
# list = ["홍길동","김길동","최길동"]
# list = ["홍길동\n","김길동\n","최길동\n"]
# f = open("data/test1.txt","w",encoding="utf-8")
# f.write(list) # TypeError: write() argument must be str, not list
# f.writelines(list)
# f.close()

# list 를 파일에 쓰려면 for문 + write()
#              or         writelines()
# list = ["홍길동", "김길동", "최길동"]
# f = open("data/test1.txt", "w", encoding="utf-8")
# for i in list:
#     f.write(i + "\n")
# f.close()


# 딕셔너리 파일로 작성
# dict1 = {"name": "hong", "age": 25, "addr": "서울"}
# f = open("data/test1.txt","w",encoding="utf-8")
# f.writelines(dict1) 키 값만 기록됨
# for k,v in dict1.items():
#     f.writelines("{} : {}\n".format(k, v))
# f.close()


# 1000 명의 키와 몸무게를 랜덤으로 생성한 후 파일 작성
# import random

# list1 = list("가나다라마바사아자차카타파하")
# # print(list1) #['가', '나', '다', '라', '마', '바', '사', '아', '자', '차', '카', '타', '파', '하']

# f = open("data/info.txt", "w", encoding="utf-8")

# # choice(list1) : list1 에서 무작위로 하나
# # randrange(40, 100) : 40~100 사이 임의의 숫자

# for i in range(1000):
#     name = random.choice(list1) + random.choice(list1)
#     weight = random.randrange(40, 100)
#     height = random.randrange(140, 200)
#     f.writelines("{}, {}, {}\n".format(name, weight, height))

# f.close()
