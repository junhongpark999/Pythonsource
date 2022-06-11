from openpyxl import Workbook
import random

wb = Workbook()
# 기본 시트 활성화
ws = wb.active
ws.title = "test"

# 셀에 데이터 입력 - 반복문
for x in range(1, 11):
    for y in range(1, 11):
        ws.cell(row=x, column=y, value=random.randint(0, 100))


wb.save("./rpabasic/excel/sample.xlsx")
