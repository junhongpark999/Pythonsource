# 인스턴스 메소드 : self 키워드 필요

# class UserInfo:
#     """
#     UserInfo class
#     Author : 홍길동
#     Date : 2022-05-26
#     Description : 클래스 작성법
#     """

#     def user_info(self):
#         print("메소드 실행")


# # 객체 생성
# user1 = UserInfo()

# # 메소드 호출
# user1.user_info()


# 멤버 변수 선언,

# class Car:
#     color = ""
#     speed = 0

#     def upSpeed(self, value):
#         self.speed += value

#     def downSpeed(self, value):
#         self.speed -= value


# # 객체 생성
# car1 = Car()
# car1.speed = 0
# car1.color = "Red"

# car2 = Car()
# car2.speed = 0
# car2.color = "Blue"

# car3 = Car()
# car3.speed = 0
# car3.color = "Yellow"

# car1.upSpeed(30)
# print("car1 색상 : {}, 속도 {}km".format(car1.color, car1.speed))

# car1.upSpeed(100)
# car1.downSpeed(20)
# print("car2 색상 : {}, 속도 {}km".format(car2.color, car2.speed))

# car3.upSpeed(40)
# print("car3 색상 : {}, 속도 {}km".format(car3.color, car3.speed))


# 생성자 __init__, 멤버변수

# class UserInfo:
#     """
#     UserInfo class
#     Author : 홍길동
#     Date : 2022-05-26
#     Description : 클래스 작성법
#     """

#     # default 생성자와 동일
#     def __init__(self) -> None:
#         self.name = "홍길동"
#         self.age = 25

#     def user_info(self):
#         return "name : {}, age : {}".format(self.name, self.age)


# # 객체 생성
# user1 = UserInfo()
# print(user1.user_info())



class Car:
    """
    UserInfo class
    Author : 홍길동
    Date : 2022-05-26
    Description : 클래스 작성법
    """
    def __init__(self) -> None:
            self.color = "Red"
            self.speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value
# 객체 생성
car1 = Car()

car2 = Car()
car2.speed = 0
car2.color = "Blue"

car1.upSpeed(30)
print("car1 색상 : {}, 속도 {}km".format(car1.color, car1.speed))

car2.upSpeed(100)
car2.downSpeed(20)
print("car2 색상 : {}, 속도 {}km".format(car2.color, car2.speed)) 


print(Car.__doc__) #""" """ <= 이걸 읽어올 수 있음