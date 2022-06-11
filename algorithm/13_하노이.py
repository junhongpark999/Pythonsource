# 하노이 탑

# 입력값 : 움직이려고 하는 원반 개수
# 출력값 : 원반을 옮기는 순서
# from_pos : 출발점 기둥
# to_pos : 도착점 기둥
# aux_pos : 보조 기둥


def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, "====>", to_pos)
        return
    # 원반 n-1 개를 보조기둥으로 움직이기
    hanoi(n - 1, from_pos, aux_pos, to_pos)

    # 가장 큰 원반을 목적지로 이동
    print(from_pos,"====>",to_pos)

    # 보조기둥에 있는 원반 n-1 개를 목적지로 이동
    hanoi(n-1, aux_pos, to_pos, from_pos)
if __name__ == "__main__":
    # 원반 1개
    print("n = 1(원반 1개)")
    hanoi(1, 1, 3, 2)
    print()
    print("n = 2(원반 2개)")
    hanoi(2, 1, 3, 2)
    print()
    print("n = 3(원반 3개)")
    hanoi(3, 1, 3, 2)
    
