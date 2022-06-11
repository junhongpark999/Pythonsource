# 리스트 안에 특정한 요소가 있는지 검색


# 순차 탐색 : 특정한 요소의 위치 리턴(찾는경우), 못찾으면 -1
from unittest import result


def seq_search(list1, key):
    size = len(list1)

    for i in range(size):
        if key == list1[i]:
            return i
    return -1


# 찾는 숫자가 여러 개 있다면 모든 위치를 리스트로 리턴
# 못 찾는 경우 빈 리스트
def seq_search2(list1, key):
    size = len(list1)

    result = []  # result = list()
    for i in range(size):
        if key == list1[i]:
            result.append(i)
    return result


if __name__ == "__main__":
    list1 = [17, 92, 18, 33, 58, 7, 33, 42]

    print("18 값", seq_search(list1, 18))
    print("33 값", seq_search(list1, 33))
    print("800 값", seq_search(list1, 800))
    print()
    print("18 값", seq_search2(list1, 18))
    print("33 값", seq_search2(list1, 33))
    print("800 값", seq_search2(list1, 800))
