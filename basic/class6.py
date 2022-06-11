# class FourCal 작성
# 숫자2개, +, - , *, / 메소드 작성(연산결과 리턴)
# class FourCal:

#     def __init__(self,num1,num2) -> None:
#         self.num1 = num1
#         self.num2 = num2


#     def add(self):
#         return self.num1 + self.num2

#     def sub(self):
#         return self.num1 - self.num2

#     def mul(self):
#         return self.num1 * self.num2

#     def div(self):
#         return self.num1 / self.num2

# num1, num2 = 10, 5
# clac = FourCal(num1, num2)
# print("{} + {} = {}".format(num1, num2, calc.add()))
# print("{} - {} = {}".format(num1, num2, calc.sum()))
# print("{} * {} = {}".format(num1, num2, calc.mul()))
# print("{} / {} = {}".format(num1, num2, calc.div()))


# Audio 클래스
# power, volume
# switch 메소드(on_off 매개변수를 받아 power 변경)
# set_volume(volume 매개변수를 받아 volume 변경)
# tune() : power 값이 true 일 경우 "La La La...."
#                      else 일 경우 "turn it on"


class Audio:
    def __init__(self, power, volume) -> None:
        self.power = power
        self.volume = volume

    def switch(self, on_off):
        self.power = on_off

    def set_volume(self, volume):
        self.volume = volume

    def tune(self):
        msg = "La La La...." if self.power else "turn it on"
        print(msg)


audio1 = Audio(False, 9)
audio1.switch(Ture)
audio1.set_volume(15)
audio1.tune()
