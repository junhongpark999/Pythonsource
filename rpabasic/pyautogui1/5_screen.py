import pyautogui as p

# 모니터 전체 화면 캡쳐
# p.screenshot("./rpabasic/pyautogui1/screen.png")

# img = p.screenshot()
# img.save("./rpabasic/pyautogui1/screen.png")

# 특정 영역 캡쳐
p.screenshot("./rpabasic/pyautogui1/screen.png", region=(0, 0, 300, 400))
