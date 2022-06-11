# 셀 이동
from openpyxl import load_workbook

wb = load_workbook("./rpabasic/excel/range.xlsx")
ws = wb.active

# rows 는 그대로 놔두고, cols 오른쪽 옆으로 한칸
# - 를 주게 되면 왼쪽 / 위로,
ws.move_range("B1:C11", rows=0, cols=1)

wb.save("./rpabasic/excel/range_move.xlsx")
