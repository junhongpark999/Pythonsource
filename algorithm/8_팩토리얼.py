# 팩토리얼

# 4! = 4 * 3 * 2 * 1

def fact(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result



if __name__=="__main__":
    print(fact(3))
    print(fact(5))
    print(fact(10))