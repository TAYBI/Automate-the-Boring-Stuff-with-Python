import sys
import openpyxl

if len(sys.argv) != 4:
    print('Usage: python blankRowInserter.py N M filename')
    sys.exit()
n = int(sys.argv[1])
m = int(sys.argv[2])
filename = sys.argv[3]

wb = openpyxl.load_workbook(filename)
sheet = wb.active
sheet.insert_rows(n, amount=m)

print(n, m, filename)

wb.save(filename)
print(f"{m} blank rows have been inserted starting at row {n} in {filename}")
