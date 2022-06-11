# result에 v가 들어가야 할 위치를 리턴하는 함수
def find_ins_idx(r, v):
    
    # r 은 이미 정렬된 리스트 상태
    # r 의 자료를 앞에서부터 확인
    for i in range(0, len(r)):
        # v가 어느 위치에 들어가는지 찾기
        if v < r[i]:
            return i
    # 적절한 위치를 못찾을 경우에는 v가 이미 정렬된 리스트보다
    # 크다는 뜻이므로 맨 뒤에 삽입
    return len(r)

def insertion_sort1(list1):
    result = []

    while list:
        value = list1.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)

    return result

if __name__ == "__main__":
    list1 = [2, 4, 5, 1, 3]
    print(insertion_sort1(list1))
