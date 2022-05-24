# list 자료형(배열과 같은 개념)
# 다양한 형태의 자료들을 담을 수 있음

# 생성
list1 = []
list2 = list(["a", "b", "c"])
list3 = ["a", "b", "c", 1, 2]
list4 = [1, 2, 3, 4, 5, 6.5]
list5 = [1, 2, ["Life", "is", "short"]]
list6 = list()

# print(list1)
# print(list2)
# print(list3)
# print(list4)
# print(list5)
# print(list6)


# 인덱싱
print("list2[0]", list2[0])  # a
print("list3[-1]", list3[-1])  # 2
print("list4[3]", list4[3])  # 4
print("list4[3] + list5[1]", (list4[3] + list5[1]))  # 6
print("list5[2][0]", list5[2][0])  # Life
print("list5[-1][2]", list5[-1][2])  # short

# 슬라이싱
print("list2[0:3]", list2[0:3])  # ['a', 'b', 'c']
print("list3[1:3]", list3[1:3])  # ['b', 'c']
print("list5[2:]", list5[2:])  # [['Life', 'is', 'short']]


# list6 = [1, 2["a", "b", ["Life", "is"]]]

# is 출력
# print("list6[2][2][1] =", list6[2][2][1])
# print("list6[-1][-1][-1] =", list6[-1][-1][-1])
# print("list6[2][-1][-1] =", list6[2][-1][-1])

# 연산자
# + : 연결, 인덱싱에서의 + : 산술연산자
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = ["a", "b", "c"]

print("list1 + list2 =", (list1 + list2))
print("list1 + list3 =", (list1 + list3))
print("list1[0] + list2[1] =", (list1[0] + list2[1]))
# print("list1[0] + list3[1] =", (list1[0] + list3[1])) # 1+a , TypeError: unsupported operand type(s) for +: 'int' and 'str'

print()

# * : 반복
print("list1 * 3 =", (list1 * 3))  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print("list1[0] * 3 =", (list1[0] * 3))  # 3

print()
# 리스트 요소 값 변경
print("list1 = ", list1)  # [1, 2, 3]
list1[1] = 7
print("list1 = ", list1)  # [1, 7, 3]
list1[2] = "Life"
print("list1 = ", list1)  # [1, 7, 'Life']

print()
print("list2 = ", list2)  # [4, 5, 6]
list2[1:2] = [10, 11]
print("list2 = ", list2)  # [4, 10, 11, 6]
list2[1] = [15, 16, 17]
print("list2 = ", list2)  # [4, [15, 16, 17], 11, 6]


print()
# 리스트 요소 삭제 : del, []
print("list1 = ", list1)  # [1, 7, 'Life']
# del list1[2]
# del list1[1:3]
list1[1:3] = []
print("list1 = ", list1)  # [1]

print()
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
for num in list1:
    print(num, end=" ")

print()
numbers = [273, 103, 5, 32, 65, 9, 72, 809, 99]
# 리스트 안의 숫자 중 100이상인 숫자 출력
for num in numbers:
    if num >= 100:
        print(num)


# 리스트 안의 숫자가 홀수/짝수인지 판별하기
for num in numbers:
    if num % 2 == 0:
        print("{}는 짝수".format(num))
    else:
        print("{}는 홀수".format(num))


# 리스트 안의 숫자들의 자릿수 출력하기
# 273은 3자리, 103은 3자리, 5는 1자리
for num in numbers:
    print("{}은 {}자리".format(num, len(str(num))))


# 함수
# append() : 리스트에 요소 추가
list1 = [1, 2, 3]
list1.append(4)
list1.append([5, 6, 7])
print(list1)  # [1, 2, 3, 4, [5, 6, 7]]

print()

# 1~100까지의 숫자 중에서 짝수 리스트 생성
even = []
for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
print(even)

print()


# sort : 오름차순정렬(기본) , sort(reverse=True)내림차순 정렬
list1 = [1, 4, 3, 2]
print("정렬 전  ", list1)  # [1, 4, 3, 2]
list1.sort()
print("정렬 후  ", list1)  # [1, 2, 3, 4]

list2 = ["k", "z", "a", "b", "r"]
print("정렬 전 ", list2)
list2.sort()
print("정렬 후 ", list2)

list2 = ["k", "z", "a", "b", "r"]
print("정렬 전 ", list2)
list2.sort(reverse=True)  # 내림차순 정렬
print("정렬 후 ", list2)  # ['z', 'r', 'k', 'b', 'a']

# A : 65, a : 97
list3 = ["k", "z", "K", "b", "A"]
print("정렬 전 ", list3)  # ['k', 'z', 'K', 'b', 'A']
list3.sort()
print("정렬 후 ", list3)  # ['A', 'K', 'b', 'k', 'z']

list4 = ["ㄷ", "ㄱ", "ㄴ", "ㅁ", "ㅅ"]
print("정렬 전 ", list4)  # ['ㄷ', 'ㄱ', 'ㄴ', 'ㅁ', 'ㅅ']
list4.sort()
print("정렬 후 ", list4)  # ['ㄱ', 'ㄴ', 'ㄷ', 'ㅁ', 'ㅅ']

# reverse() : 리스트 뒤집기
list1 = ["a", "c", "b", "z"]
list1.reverse()  # 내림차순 정렬아닌 리스트를 그대로 뒤집어서 보여줌
print("list", list1)  # ['z', 'b', 'c', 'a']


# sort() + reverse() : 내림차순 정렬
list1 = [3, 12, 1, 5, 9, 2, 7]
print("정렬 전 ", list1)
list1.sort()
list1.reverse()
print("정렬 후 ", list1)

print()
# index() : 위치 반환
print("list", list1)
print("list1 에 9가 있는지 확인", list1.index(9))  # 1
# 못 찾으면 ValueError 발생
# print("list1 에 45가 있는지 확인", list1.index(45))


print()
# insert(삽입위치,삽입할 요소)
list1 = [1, 2, 3]
list1.insert(0, 4)
print("list1 요소 삽입 후", list1)  # [4, 1, 2, 3]

print()
# remove(제거할 요소) : 첫번째로 나오는 요소 삭제
list1.remove(2)
print("list1 요소 제거 후", list1)

print()
# pop() : 리스트 맨 마지막 요소 끄집어 내기
# pop(위치) : 해당 위치 요소 끄집어 내기
list1 = [1, 2, 3, 4, 5, 6, 7]
print("list1", list1)
list1.pop()
print("list1 pop() 후", list1)
list1.pop(2)
print("list1 pop() 후", list1)

print()
# count(x) : 리스트에 포함된 요소 x 의 개수 세기
print("list1.count(2)", list1.count(2))  # 1

print()
# extend(X 리스트) : 원래 리스트에 x 리스트 더하기 (+ 개념과 같음)
list2 = [16, 17, 18]
print("list1 + list2 =", (list1 + list2))
list1.extend(list2)
print("list1 extend ", list1)


print()
# pop은 끄집어내면서 그걸 바로 반환해줘서 제거+반환 역할을 해준다
print("list1.pop():", list1.pop())  # 18


print()
# clear() : 요소 모두 삭제
list1.clear()
print("list1 clear 후", list1)

print()
# 요소 in 리스트명 : 리스트 안에 해당 요소가 있느냐?
fruits = ["딸기", "바나나", "수박", "시과", "참외"]
print("딸기" in fruits)  # True
print("두리안" in fruits)  # False


# 리스트가 비어 있으면 거짓(내용이 들어있나 안들어있나 바로 판별가능)
list1 = []
if list1:
    print("참")
else:
    print("거짓")


# 리스트 요소 출력
for num in enumerate(numbers):
    print(num)  # (0, 273)(1, 103)(2, 5)(3, 32) ... : (인덱스,값) => 튜플 자료형 형태로 반환

print()

# enumerate() : 하나씩 가지고 나올 수 있는 자료형에 사용 가능
# idx, num = (0, 273)
for idx, num in enumerate(numbers, start=1):
    print(idx, num)


print()
# 실습
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다
# 70,66,55,75,90,95,80,85,100,87
# 중간고사 점수를 리스트로 생성하고 A학급의 평균을 구하시오
A_class = [70, 66, 55, 75, 90, 95, 80, 85, 100, 87]
total = 0
for num in A_class:
    total += num
print("A학급의 평균 ㅣ %.2f" % (total / len(A_class)))

# for 사용 안하고
print("A학급의 평균 ㅣ %.2f" % (sum(A_class) / len(A_class)))


# 다음 리스트에서 Apple 항목만 삭제하고 출력하기
# ["Banana","Apple","Orange","Grape"]
fruits = ["Banana", "Apple", "Orange", "Grape"]
fruits.remove("Apple")  # del fruits[1]<=이거도 가능함
print(fruits)
