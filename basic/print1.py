# print() 알아보기 - 화면출력
# 옵션 
# 1) sep : ,로 들어오는 출력문자들의 구분을 어떻게 할 것인가?
# 2) end : 줄바꿈을 하지 않고 다음 줄과 연결해서 출력

print("Hello Python!!") # 문자열 - 쌍따옴표, 홑따옴표 허용
print('Hello Python!!')
print(100)
print("100")
print("25.3")
print(25)
print()
# type() : 변수 타입 확인
print(type(100))  # <class 'int'>
print(type("100"))# <class 'str'>
print(type(25.5)) # <class 'float'>
print(type(True)) # <class 'bool'>
print()
print('T','E','S','T') # T E S T
print('T','E','S','T',sep='') # TEST
print('2022','05','19',sep='-') # 2022-05-19
print("niceman","naver.com",sep="@") # niceman@naver.com
print()
print("파이썬은",end=' ')
print("쉬운 언어입니다.")