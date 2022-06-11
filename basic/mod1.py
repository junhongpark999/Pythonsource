# 사용자 정의 모듈
from unittest import result


def sum(a, b):
    return a + b


def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 없습니다.")
        return
    else:
        result = sum(a, b)
    return result


# 테스트
if __name__ == "__main__":
    print(safe_sum('a',1))
    print(safe_sum(2,1))
    print(sum(2,1))