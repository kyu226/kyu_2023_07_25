import openpyxl

# 創建新的 Excel 檔案
workbook = openpyxl.Workbook()

# 選取工作表
sheet = workbook.active

# 寫入資料到儲存格
sheet['A1'] = 'Name'
sheet['B1'] = 'Age'

# 寫入多行資料
data = [('Alice', 25), ('Bob', 30), ('Carol', 28)]
for row_data in data:
    sheet.append(row_data)

# 儲存 Excel 檔案
workbook.save('output.xlsx')
