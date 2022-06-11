def merge_sort(list1):
    # 리스트 크기 구하기
    size = len(list1)

    # 종료 조건
    if size <= 1:
        return list1

    # 분해 작업
    mid = size // 2  # 중간 구하기

    g1 = list1[:mid]  # 재귀호출로 첫번째 그룹 g1 [6,8,3,9,10] => g1 [6,8], g2[3,9,10]
    g2 = list1[:mid]

    merge_sort(g1)
    merge_sort(g2)

    # 병합 작업
    i1, i2, ia = 0, 0, 0

    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            list1[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            list1[ia] = g2[i2]
            i2 += 1
            ia += 1
    # 남아 있는 자료 결과에 추가
    while i1 < len(g1):
        list1[ia] = g1[i1]
        i1 += 1
        ia += 1

    while i2 < len(g2):
        list1[ia] = g2[i2]
        i2 += 1
        ia += 1


if __name__ == "__main__":
    list1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    merge_sort(list1)
    print(list1)
