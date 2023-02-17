import openpyxl


items1 = ['ITEM', 'Eggplant', 'Cucumber', 'Green cabl',
          'Eggplant', 'Garlic', 'Parsnips', 'Asparagus', 'Avocados']
items2 = ['SOLD', '334', '252', '238', '516', '98', '16', '335', '84']
wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1, 9):
    sheet['A' + str(i)] = items1[i - 1]
    sheet['B' + str(i)] = items2[i - 1]

wb.save('spreadsheet.xlsx')
