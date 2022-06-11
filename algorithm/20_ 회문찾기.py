# 스택
# 스택(후입선출) 삽입 1 2 3 4 반출 4 3 2 1
# 큐(선입선출) 1 2 3 4 반출 1 2 3 4

# 리스트
# 회문 : 순서대로 읽어도, 거꾸로 읽어도 내용이 같은 낱말이나 문장
# 역삼역, 기러기, 일요일, 사진사, 복불복
# mom, wow, level, radar

# 주어진 문장이 회문인지 아닌지 찾기
# 회문이면 True, 아니면 False


def palindrome(s):
    qu = []  # queue
    st = []  # stack

    # 받는 문자를 큐와 스택에 담기(알파벳인 경우만 소문자로 변경 후 담기)
    # for
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())

    # 큐와 스택에 들어있는 문자를 꺼내면서 비교
    # 큐에 문자가 남아 있는 동안 반복
    # 큐와 스택에서 꺼낸 문자가 다르면 return false
    # pop() : 뒤에서 부터 인출
    # pop(번호지정) : 해당번호 인출
    if qu.pop(0) != st.pop():
        return False

    # 루프 종료 후 true 리턴
    return True


# 문장의 앞뒤를 차례로 비교
def palindrome2(s):

    # 시작 위치 지정
    start = 0
    # 끝 위치 지정
    end = len(s) - 1

    while start < end:
        # start 위치에 있는 문자가 알파벳 문자가 아니면 start + 1
        if not s[start].isalpha():
            start += 1
        # end 위치에 있는 문자가 알페벳 문자가 아니면 end - 1
        elif not s[end].isalpha():
            end -= 1
        # start 와 end 위치에 있는 문자를 소문자로 변경한 후 비교해서 같지 않으면 False 리턴
        elif s[start].lower() != s[end].lower():
            return False
        # 위 세가지 경우가 아니라면 start + 1, end - 1
        else:
            start += 1
            end -= 1
    # 반복문 종료 후  True 리턴
    return True


if __name__ == "__main__":
    print(palindrome("Wow"))
    print(palindrome("Madam, I'm Adam."))
    print(palindrome("Madam, I am Adam."))
    print()
    print(palindrome2("Wow"))
    print(palindrome2("Madam, I'm Adam."))
    print(palindrome2("Madam, I am Adam."))
