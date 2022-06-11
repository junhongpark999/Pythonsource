# 키보드 다루기

from time import sleep
import pyautogui as p

# 입력 : write()
# p.write("write")

# 메모장에 문자열 타이핑
# 현재 화면에 메모장 활성화
notepad = p.getWindowsWithTitle("새 텍스트 문서")[0]
notepad.activate()
sleep(3)
# p.write("write")
p.write(
    "dkssudgktpdy wjsrldnjssla. wlrmaqnxj rpdladmf tlwkrgkrpTtmqslek wkfldp ckrtjrgkdu wntlqtldh..... ekdtlsdml ahaanrpsms auczlfh dlqslRk.....?  3chdksdp eoekqgktlqtldh...................dk dlfjs Rho anrjqrnsdy rkatkgkqslek wjsrldnjssla.........rpdladmf whdfygkqslek.....whgdms ekqqus rkatkemflqslek. whgdmstlrks qhsotlqtldh....!......(whdfyehla)",
    interval=0.7,
)
# p.write("안녕하세요")  # 한글지원 안함

# 해야 할 작업을 리스트로 작성
# p.write(
#     ["h", "e", "l", "l", "o", "left", "left", "right", "l", "o", "enter"], interval=0.75
# )


# hotkey(조합키)
# import pyperclip  # 클립보드  한글을 사용하려면 이렇게 해야함

# pyperclip.copy("안녕하세요")
# p.hotkey("ctrl", "v")
# p.hotkey("ctrl", "a")
# p.hotkey("ctrl", "shift", "esc")  # 작업관리자 단축키


# keyDown() + KeyUp() == press()
# p.keyDown("Shift")
# p.press("4")
# p.keyUp()

# p.press(["a", "b", "c"], 2)
# p.press(["#", "%", "%"], 2, 1)
