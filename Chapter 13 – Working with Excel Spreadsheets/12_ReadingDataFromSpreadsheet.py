import openpyxl
import pprint

print('Openning workbook....')
wb = openpyxl.load_workbook('censuspopdata.xlsx')

sheet = wb['Population by cencus Tract']
countyData = {}

# TODO: Fill in countyData with each county's population and tracts.
print('Reading Rowas...')

for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    stat = sheet['B' + str(row)].vaue
    country = sheet['C' + str(row)].vaue
    pop = sheet['D' + str(row)].vaue

 # TODO: Open a new text file and write the contents of countyData to it.
