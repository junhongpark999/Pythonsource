# 숫자 n 개를 리스트로 입력받아 최솟값 구하기

# 숫자 입력받은 후 list1 에 추가
# q라는 문자가 입력되면 리스트 추가하는 걸 종료
def num_input(list1):
    
    i = 1

    print("리스트에 추가할 숫자를 입력하세요\n숫자 추가를 끝내기 위해서는 q를 입력하세요")
    while True:
        print(str(i),": ",end="")
        num = input()

        if num != 'q':
            list1.append(int(num))
        else:
            break
        i = i + 1


# 최솟값 구하기
def find_min(list1):
    min = list1
    size = len(list1)

    for i in range(1, size):
        if min > list1[i]:
            min = list1[i]

    return min

if __name__=="__main__":
    list1 = list() # 비어 있는 리스트 생성
    num_input(list1)
    print("최솟값 ",find_min(list1))



if __name__=="__main__":
    list1 = list() # 비어 있는 리스트 생성
    num_input(list1)
    print("최솟값 ",min(list1))