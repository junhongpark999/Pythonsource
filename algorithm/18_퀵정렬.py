def quick_sort(list1):
    # 리스트 크기 구하기
    size = len(list1)

    # 종료
    if size <= 1:
        return list1

    # 기준값 정하기
    pivot = list1[-1]  # 5
    # 기준값 보다 작은 요소 담기
    g1 = []
    # 기준값 보다 큰 요소 담기
    g2 = []

    for i in range(0, size - 1):  # 마지막 값은 기준값이기 때문에 제외
        if list1[i] < pivot:
            g1.append(list1[i])  # g1 = [3,1,2,4] g1 = [3,1,2], g2=[], g1=[1], g2=[3]
        else:
            g2.append(list1[i])  # g2 = [6,8,9,10,7]

    return quick_sort(g1) + [pivot] + quick_sort(g2)


if __name__ == "__main__":
    list1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    print(quick_sort(list1))
