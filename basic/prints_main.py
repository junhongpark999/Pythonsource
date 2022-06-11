# 사용자가 정의한 모듈 실습

import prints

prints.prt1()
prints.prt2()


import mod1

print(mod1.sum(15, 25))
print()
print(mod1.safe_sum(15,25))
print()
print(mod1.safe_sum(15,"25"))  # 리턴을 걸었는데 가져오는것이 없다면 None 이 무조건 출력된다

# from mod1 import safe_sum
# print(sum(45, 25)) # 70

print()

from prints import prt1
prt1()


import calc import FourCal

num1, num2 = 10, 5
# four1 = calc.FourCal(num1, num2)

four1 = FourCal(num1, num2)
print("{} + {} = {}".format(num1, num2, four1.add()))
print("{} - {} = {}".format(num1, num2, four1.sum()))
print("{} * {} = {}".format(num1, num2, four1.mul()))
print("{} / {} = {}".format(num1, num2, four1.div()))


