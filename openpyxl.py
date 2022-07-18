from openpyxl import load_workbook

wb = load_workbook(r'C:\test\test.xlsx')
sheet = wb.active
max_row = sheet.max_row
print(max_row)

sheet['A1'] = 'School name'
sheet['B1'] = 'school url'
sheet.cell(row=max_row + 1, column=4).value = 5

wb.save(r'C:\test\test.xlsx')
