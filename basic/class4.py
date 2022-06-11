from itertools import count
from typing_extensions import Self


class Car:
    """
    UserInfo class
    Author : 홍길동
    Date : 2022-05-26
    Description : 클래스 작성법
    """

    # 클래스 변수ㅡ
    car_count = 0

    def __init__(self, color, speed) -> None:
        self.color = color
        self.speed = speed

        Car.car_count += count

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

    def __del__(Self):
        Car.car_count -= 1


# 객체 생성
car1 = Car(1, "Red", 20)
car1.upSpeed(50)
print(
    "자동차 1 현재 속도 {}km, 색상 : {}, 생산된 자동차 대수 : {}대".format(
        car1.speed, car1.color, Car.car_count
    )
)

car2 = Car(1, "Black", 30)
car2.upSpeed(80)
print(
    "자동차 2 현재 속도 {}km, 색상 : {}, 생산된 자동차 대수 : {}대".format(
        car2.speed, car2.color, Car.car_count
    )
)

car3 = Car(1, "Yello", 0)
car3.upSpeed(100)
print(
    "자동차 3 현재 속도 {}km, 색상 : {}, 생산된 자동차 대수 : {}대".format(
        car3.speed, car3.color, Car.car_count
    )
)


del car1
print("생산된 자동차 대수 {}대".format(Car.car_count))
