# 리스트 안에서 가장 큰 숫자 찾기
# [17,92,18,33,58,7,33,42]

def find_max(list1):
    # 리스트 크기
    size = len(list1)
    # 리스트 첫번째 요소 max 에 담기
    max = list1[0]

    for i in range(1, size):
        if max < list[i]:
            max = list[i]
    return max

# 가장 큰 값이 있는 위치 번호 돌려받기
def find_max1(list1):
     # 리스트 크기
    size = len(list1)
    # 리스트 첫번째 요소 max_idx 에 담기
    max_idx = 0

    for i in range(1, size):
        if list1[max_idx] < list[i]:
            max_idx = i
    return max_idx


    # 테스트
if __name__=="__main__":
    list1 = [17,92,18,33,58,7,33,42]

    print("가장 큰 숫자",find_max(list1))
    max_idx = find_max1(list1)
    print("가장 큰 숫자가 있는 위치{}, 가장 큰 숫자{}".format(max_idx, list1[max_idx]))