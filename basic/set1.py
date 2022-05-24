# set : 집합자료형
# 자바 Set 과 같은 개념
# 중복 허용 안됨
# 순서 없음 - 인덱싱, 슬라이싱 사용할 수 없음

set1 = set()
set2 = set("Hello")
set3 = set([1, 2, 3, 4])
set4 = set([1, 2, 3, 4, 6, 6])
set5 = set({"no": "1", "name": "hong", "age": 24})

print(set1)  # set()
print(set2)  # {'l', 'H', 'e', 'o'}
print(set3)  # {1, 2, 3, 4}
print(set4)  # {1, 2, 3, 4, 6}
print(set5)  # {'no', 'name', 'age'}


print()

# set ==> tuple 변환
print(tuple(set3))  # (1, 2, 3, 4)

# set ==> list 변환
print(list(set3))  # [1, 2, 3, 4]


# 교집합, 합집합, 차집합구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print("s1,s2 교집합", s1 & s2)  # {4, 5, 6}
print("s1,s2 교집합", s1.intersection(s2))  # {4, 5, 6}

print()

print("s1,s2 합집합", s1 | s2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("s1,s2 합집합", s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print()

print("s1,s2 차집합", s1 - s2)  # {1, 2, 3}
print("s1,s2 차집합", s1.difference(s2))  # {1, 2, 3}


# 함수
# add() : 값 하나 추가
print(s1) # {1, 2, 3, 4, 5, 6}
s1.add(17)
print(s1) # {1, 2, 3, 4, 5, 6, 17}

# update() 여러 개의 값을 한꺼번에 추가
s1.update([18, 19, 20])
print(s1) # {1, 2, 3, 4, 5, 6, 17, 18, 19, 20}

# remove() : 특정 값 제거
s1.remove(2)
print(s1) # {1, 3, 4, 5, 6, 17, 18, 19, 20}

