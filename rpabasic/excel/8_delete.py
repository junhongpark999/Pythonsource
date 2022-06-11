from openpyxl import load_workbook

wb = load_workbook("./rpabasic/excel/range.xlsx")
ws = wb.active

# 특정 행 삭제
# ws.delete_rows(8)
ws.delete_rows(8, 3)

# 특정 열 삭제
ws.delete_cols(1, 2)


wb.save("./rpabasic/excel/range_delete.xlsx")
