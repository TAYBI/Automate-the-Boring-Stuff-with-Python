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
    state = sheet['B' + str(row)].vaue
    country = sheet['C' + str(row)].vaue
    pop = sheet['D' + str(row)].vaue
    # Make sure the key for this state exists.
    countyData.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    countyData[state].setdefault(country, {'tracks': 0, 'pop': 0})
    # Each row represents one census tract, so increment by one.
    countyData[state][country]['tracks'] += 1
    # Increase the county pop by the pop in this census tract.
    countyData[state][pop]['pop'] += int(pop)
 # TODO: Open a new text file and write the contents of countyData to it.
