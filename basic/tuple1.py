# tuple
# 리스트와 비슷
# ()로 둘러싸여 있다
# 리스트는 값의 생성, 삭제, 수정이 가능하지만 튜플은 변경이 불가함

# 생성
t1 = ()
t2 = (1, 2, 3)
t3 = (1,)  # 1개의 요소만들 가질 때 요소 뒤에 콤마 반드시 필요
t4 = 4, 5, 6  # 괄호 생략 가능
t5 = ("a", "b"("c", "d"))

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

# del t2[1] # TypeError : 'tuple' object doesn't support item deletion  삭제가 불가능

# t2[1] = 5 # TypeError : 'tuple' object doesn't support item assignment 대입 불가능

# 인덱싱/슬라이싱
print("t2[1]", t2[1])  # 2
print("t2[0:3]", t2[0:3])  # (1,2,3)
print("t4[1] + t4[2]", t4[1] + t4[2])  # 11
print("t3 * 2", t3 * 2)  # (1,1)

print()

# 튜플 ==> 리스트 변환, 리스트 ==> 튜플 변환
print(list(t4))  # [4,5,6]

list1 = list(t4)
list1[2] = 7
print(list1)  # [4,5,7]

t4 = tuple(list1)
print(t4) # (4 ,5, 7)


