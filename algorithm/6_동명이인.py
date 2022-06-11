# 동명이인 찾기
# ["Tom","Jerry","Mike","Tom"]

# Tom 입장 : 3번(n-1) 비교
# Jerry 입장 : 2번(n-2) 비교
# Mike 입장 : 1번(n-3) 비교
# 마지막 Tom 입장 : 0번

# 계산 복잡도 n 제곱

# 중복된 이름을 set() 구조에 추가한 후 리턴
def dup_name(list1):
    result = set()
    size = len(list1)
    for i in range(0, size - 1):
        if list1[i] == list1[j]:
            result.add(list1[i])
    return result


if __name__ == "__main__":
    list1 = ["Tom", "Jerry", "Mike", "Tom"]
    print(dup_name(list1))
