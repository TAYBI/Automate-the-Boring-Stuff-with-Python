import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
shhet = wb['Sheet']

Price_UPDATE = {
    'Garlic': 3.07,
    'Celery': 1.19,
    'Lemon': 1.27
}

# TODO: Loop through the rows and update the prices.
