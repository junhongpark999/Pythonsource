# 최대공약수
# 두 개 이상의 정수의 공통 약수 중에서 가장 큰 값
"""
두 수의 약수 중에서 공통된 것을 찾아 그 값 중 최댓값 찾기
문제 : 4와 6의 최대 공약수 찾기
알고리즘:
1)두 수 중 더 작은 값을 i 에 저장
2)i 가 두 수의 공통된 약수인지 확인
3)공통된 약수라면 이 값을 결과값으로 돌려주기
4)공통된 약수가 아니면 i를 1만큼 감소시키고 2번으로 돌아가 반복
"""


def gcd(a, b):
    i = min(a, b)

    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1


if __name__ == "__main__":
    print(gcd(1, 5))
    print(gcd(3, 6))
    print(gcd(60, 24))
    print(gcd(81, 27))
