import pyautogui

# 좌표 인식 - position()

# pos = pyautogui.position()
# print(pos)  # Point(x=531, y=877)
# print(pos.x, ", ", pos.y)

# 마우스 이동
# moveTo(x,y,시간) : 절대좌표
# pyautogui.moveTo(100, 100, duration=1)
# pyautogui.moveTo(200, 200, duration=1)
# pyautogui.moveTo(300, 300, duration=1)

# moveRel()(x,y,시간) : 상대좌표
pyautogui.moveTo(300, 300, duration=1)
pyautogui.moveRel(100, 100, duration=0.5)
print(pyautogui.position())  # Point(x=400, y=400)  ↑ 300 + 100 = 400
