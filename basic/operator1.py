# 연산자
# 산술연산자 : +, -, *, /(실수), //(정수), %, **

a,b = 5,3
print(a+b,a-b,a*b,a/b,a//b,a%b,a**b)

print()
s1,s2,s3 = "100","100.123","999999999"
print(s1,s2,s3)
print(s1+s2+s3) # + : 연결 => 100100.123999999999
print(float(s1)+float(s2)+float(s3))
print(int(s1) + 1) #TypeError: can only concatenate str (not "int") to str

# 복합대입연산자 : +=, -=, *=, /=, //=, %=, **=
a = 10

a += 5
print("a",a)
a == 5
print("a",a)
a *= 5
print("a",a)
a /= 5
print("a",a)
a //= 5
print("a",a)
a %= 5
print("a",a)
a **= 5
print("a",a)
# 실습 : 777,777 원
# 화폐교환 : 5만원/1만원/5천원/1천원권 으로 각각 몇장씩 나오는가
money = 777777

m50000 = money // 50000
money %= 50000

m10000 = money // 10000
money %= 10000

m5000 = money // 5000
money %= 5000

m1000 = money // 1000
money %= 1000

print("50,000원 : %d 장" % m50000)
print("10,000원 : %d 장" % m10000)
print("5,000원 : %d 장" % m5000)
print("1,000원 : %d 장" % m1000)
print("나머지 돈 : %d" % money)

print()
# 관계연산자 : ==, !=, >, <, >=, <=
a,b = 10,0
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)

# 논리연산자 : and, or, not
print(100 > 60 and 60 > 15)
# print(100 > 60 && 60 > 15)
print(100 > 60 or 60 > 15)
print(not 60 < 15)
print(not False)
print(not True)
# print(!True) 
print()

#비트연산자
print(10 & 7)
print(10 | 7)
print((100> 60) & (60 > 15))