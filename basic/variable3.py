# type() : 변수 타입 확인

a = 3.5
print(type(a)) # <class 'float'>

b = True
print(type(b)) # <class 'bool'>

c = 123
print(type(c)) # <class 'int'>

d = "123"
print(type(d)) # <class 'str'>

# 형변환 : str(), int(), float(), bool()
print()
print(str(True),type(str(True))) # True
print(str(1),type(str(1)))       # 1
print(str(98.6),type(str(98.6))) # 98.6

print()
print(int(True),type(int(True))) # 1
print(int(False),type(int(False)))# 0
print(int("1"),type(int("1")))   # 1
print(int(98.6),type(int(98.6))) # 98
# print(int("98.6"),type(int("98.6"))) #ValueError: invalid literal for int() with base 10: '98.6'

print()
print(float(True),type(float(True))) # 1.0
print(float(False),type(float(False)))# 0.0
print(float("1"),type(float("1")))   # 1.0
print(float(98),type(float(98))) # 98.0

print() #0만 false
print(bool("True"),type(bool("True"))) # Ture
print(bool("False"),type(bool("False")))# Ture
print(bool("1.0"),type(bool("1.0")))   # Ture
print(bool(98),type(bool(98))) # Ture
print(bool(1),type(bool(1))) # Ture
print(bool(0),type(bool(0))) # False
print(bool(1.0),type(bool(1.0))) # Ture
print(bool(96.5),type(bool(96.5))) # True



