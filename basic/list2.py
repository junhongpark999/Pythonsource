# 주차장 프로그램

from curses.panel import top_panel


parking_lot = []

top, car_name = 0, "A"

# ord("A") => 65 : 문자열의 아스키 코드값을 돌려줌
# chr(65) => A : 반대로 아스키 코드값을 문자열로 돌려줌
# print(ord(car_name))  # 65
# print(ord(car_name) + 1)  # 66
# print(chr(ord(car_name) + 1))  # B

while True:
    no = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 : "))

    if no <= 3:
        if no == 1:
            if top >= 5:
                print("주차장이 꽉 찼음")
            else:
                parking_lot.append(car_name)
                print("%c 자동차 들어감. 주차장 상태 ==> %s" % (car_name, parking_lot))

                top += 1
                car_name = chr(ord(car_name) + 1)
        elif no == 2:
            if top > 0:
                out_car = parking_lot.pop()
                print("%c 자동차 나감. 주차장 상태 ==> %s" % (out_car, parking_lot))

                top -= 1
                car_name = chr(ord(car_name) - 1)
            else:
                print("빠져나갈 자동차가 없음")
        else:
            print("프로그램 종료")
            break
    else:
        print("번호를 확인해 주세요")
