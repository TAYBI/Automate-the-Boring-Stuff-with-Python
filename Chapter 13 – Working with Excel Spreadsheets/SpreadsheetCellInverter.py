import openpyxl
from openpyxl.utils import get_column_letter

print('openning workbook...')
wb = openpyxl.load_workbook('spreadsheet.xlsx')

sheet = wb['Sheet']
columns = []
rows = []

for column in range(1, sheet.max_column + 1):
    columns.append(get_column_letter(column))
for row in range(1, sheet.max_row + 1):
    rows.append(row)

DATA = {}

for column in columns:
    for row in rows:
        key = f'{column}{row}'
        value = sheet[f'{column}{row}'].value
        DATA[key] = value

for key, value in DATA.items():
    print(key, ':', value)
