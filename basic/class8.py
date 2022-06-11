# # 오버라이딩

# class Parent():
#     def func1(self):
#         print("Parent func1()")

#     def func2(self):
#         print("Parent func2()")

# class Child(Parent):
#     def func1(self):
#         print("Child func1()")

#     def func3(self):
#         print("Child func2()")

# parent, child = Parent(), Child()
# parent.func1()
# child.func1()
# parent.func2()
# child.func2()
# child.func3()


class Car:

    speed = 0

    def up_speed(self, value):
        self.speed = self.speed + value
        print("현재 속도(부모 클래스) : {}".format(self.speed))

    def down_speed(self, value):
        self.speed = self.speed - value


class Sedan(Car):

    seatNum = 0

    def up_speed(self, value):
        self.speed = self.speed + value

        # 현재 속도가 150 보다 크면 현재 속도를 150으로 변경
        if self.speed > 150:
            self.speed = 150
            print("현재 속도(부모 클래스) : {}".format(self.speed))

    def getSeatNum(self):
        return self.seatNum


class Truck(Car):

    capacity = 0

    def getCapscity(self):
        return self.capacity


sedan1, truck1 = Sedan(), Truck()

sedan1.up_speed(200)
truck1.up_speed(80)

sedan1.seatNum = 5
truck1.capacity = 50

print("승용차의 속도는 {}km, 좌석수는 {}개".format(sedan1.speed, sedan1.getSeatNum()))
print("트럭의 속도는 {}km, 총 중량은 {}톤".format(truck1.speed, truck1.getCapscity()))
