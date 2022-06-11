# 1 ~ n까지 연속한 숫자의 제곱 합 구하기
# for 사용
# n = 10, 1의 제곱 + 2의 제곱 + 3의 제곱.....10의 제곱

# 복잡도 : O(n)
def sum_squares(n):
    s = 0

    for i in range(1, n + 1):
        s += i * i
    
    return s

# 공식 : n(n+1)(2n+1)/6
# 복잡도 : O(1)
def sum_squares2(n):
    return n*(n+1)*((2*n)+1)/6


if __name__=="__main__":
    print(sum_squares(10))