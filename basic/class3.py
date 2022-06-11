# 클래스 변수 - 반드시 선언 필요, 클래스이름.클래스변수 사용

class UserInfo:
    """
    UserInfo class
    Author : 홍길동
    Date : 2022-05-26
    Description : 클래스 작성법
    """

    user_cnt = 0

    def __init__(self, name, age) -> None:
        # 멤버변수
        self.name = name
        self.age = age
        # 클래스 변수 : static 과 같은 개념
        UserInfo.user_cnt += 1

    def user_info(self):
        return "name : {}, age : {}".format(self.name, self.age)

    def __del__(self):
        UserInfo.user_cnt -= 1


user1 = UserInfo("홍길동", 25)
user2 = UserInfo("성춘향", 26)

print(user1.user_info)
print(user2.user_info)

print("현재 생성된 User {}명".format(UserInfo.user_cnt))

# 객체 삭제
del user1 # __del__ 호출됨
print("현재 생성된 User {}명".format(UserInfo.user_cnt))

