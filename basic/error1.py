# 예외 처리
# 문법 에러

# a, b = 10, 15
# print(a, b)
# print(c) #NameError: name 'c' is not defined

# 런타임 에러 (실행했을때 발생하는 에러)
# print(10 / 0) # ZeroDivisionError: division by zero

# x = [10,20,30]
# print(x[3]) # IndexError: list index out of range

# dict1 = {"name":"hong","age":25,"city":"seoul"}
# print(dict1["addr"]) # KeyError: 'addr'

# x.index(40) # ValueError: 40 is not in list

# f = open("data/111.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: 'data/111.txt'

# x = [1, 2]
# y = (1, 2)
# print(x + y) # TypeError: can only concatenate list (not "tuple") to list


#### 예외 처리 기법
# try ~ except 문 : 오류 종류와 상관없이 오류가 발생하기만 하면 except 블록 수행
# try ~ except 발생오류 : except에 정해놓은 오류 시 except 블록 수행
# try ~ except ~ else
# try ~ finally : 오류 발생 여부와 상관없이 무조건 실행


name = ["Kim", "Park", "Choi"]

# try:
#     z = "let"
#     x = name.index(z)
#     print("{} Found it! in name {}".format(z, x + 1))
# except:
#     print("Not found")


# try:
#     z = "let"
#     x = name.index(z)
#     print("{} Found it! in name {}".format(z, x + 1))
# except ValueError: # ValueError 만 잡기
#     print("Not found")


# try:
#     number = int(input("정수입력 >> "))

#     print("원 반지를 : ",number)
#     print("원 둘레 : ",2 * 3,14 * number)
#     print("원 넓이 : ",3.14 * number * number)
# except:
#     print("입력 숫자를 확인해 주세요")


# try:
#     number = int(input("정수입력 >> "))

#     print("원 반지를 : ",number)
#     print("원 둘레 : ",2 * 3,14 * number)
#     print("원 넓이 : ",3.14 * number * number)
# except ValueError:
#     print("입력 숫자를 확인해 주세요")


# try:
#     pass
# except:
#     pass
# else: # 예외가 발생하지 않은 경우에 실행(except 절 바로 다음에 위치해야 함)
#     pass


# try:
#     z = "Kim"
#     x = name.index(z)
#     print("{} Found it! in name {}".format(z, x + 1)) # 이것도 나오고~
# except ValueError:
#     print("Not found") # (이건 안나옴)
# else:
#     print("OK! Else") # 이것도 나옴~


# try:
#     number = int(input("정수입력 >> "))
# except ValueError:
#     print("입력 숫자를 확인해 주세요")
# else:
#     print("원 반지를 : ",number)
#     print("원 둘레 : ",2 * 3,14 * number)
#     print("원 넓이 : ",3.14 * number * number)


# Exception : 어떤 오류가 나는지 모를 때
try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! in name {}".format(z, x + 1))
except Exception:
    print("Not found")


# exception 발생오류 as 오류 메세지 변수

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)


try:
    f = open("data/info.txt", "r")
finally:
    f.close()


try:  # 예외 발생 구문
    pass
except:  # 예외가 발생한 경우
    pass
else:  # 예외가 발생하지 않은 경우에 실행(except 절 바로 다음에 위치해야 함)
    pass
finally:  # 예외 발생 여부 상관없이 무조건 실행
    pass
