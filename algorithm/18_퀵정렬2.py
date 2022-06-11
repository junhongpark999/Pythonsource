def quick_sort(list1, start, end):
    # 리스트 크기 구하기
    size = len(list1)

    # 종료
    if end - start <= 0:
        return

    # 기준값 정하기
    pivot = list1[end]

    i = start

    for j in range(start, end):  # 마지막 값은 기준값이기 때문에 제외
        if list1[j] < pivot:
            list1[i], list1[j] = list1[j], list1[i]
            i += 1
    
    list1[i], list1[end] = list1[end], list1[i]

    # 재귀호출
    quick_sort(list1,start,i - 1)
    quick_sort(list1, i + 1, end)


if __name__ == "__main__":
    list1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    quick_sort(list1, 0, len(list1) - 1)
    print(list1)
