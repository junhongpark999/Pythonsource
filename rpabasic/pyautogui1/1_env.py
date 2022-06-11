import pyautogui

# pyautogui : 윈도우의 화면상 마우스 조정, 키보드 조정, 좌표 인식...


# 윈도우 화면의 스크린 크기를 가져오기
size = pyautogui.size()
print(size) # Size(width=1920, height=1080)
print(size[0]) # width
print(size[1]) # height
