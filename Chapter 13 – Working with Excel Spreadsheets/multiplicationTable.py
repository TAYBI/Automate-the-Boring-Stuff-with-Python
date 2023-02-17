import sys
import openpyxl
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
sheet = wb.active
number = int(sys.argv[1])

for i in range(1, number):
    letter = get_column_letter(i)
    for j in range(1, number):
        sheet[letter + str(j)] = str(i*j)

wb.save(f'multiplicationTable{number}.xlsx')
