# 엑셀 라이브러리 - openpyxl, pandas

from openpyxl import Workbook

# 엑셀 파일 생성

# 1) 새 워크북 생성
wb = Workbook()

# 2) 현재 활성화 된 시트 가져오기
ws = wb.active

# 3) 워크 시트 이름 변경
ws.title = "test"

# 워크북 저장
# . : pythonsource
wb.save("./rpabasic/excel/sample.xlsx")
