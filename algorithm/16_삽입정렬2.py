# 1번 삽입정렬과 다르게 하나의 리스트에서 구현

# 오름차순 정렬
def insertion_sort1(list1):
    # 현재 리스트 길이 구하기
    size = len(list1)
    # for 1 ~ n
    for i in range(1, size):
    # i번 위치에 있는 값을 key 변수에 저장
        key = list1[i]
    # j를 i 바로 왼쪽 위치로 지정
        j = i - 1
    # 리스트의 j번 위치에 있는 값과 key를 비교해 key가 삽입될 위치 찾기
    # while문
    while j >= 0 and list1[j] > key:
        list1[j+1] = list1[j]
        j -= 1

    # while문 종료 후 찾은 삽입 위치에 key 저장
    list1[j + 1] = key





if __name__ == "__main__":
    list1 = [2, 4, 5, 1, 3]

    insertion_sort1(list1)
    print(list1)