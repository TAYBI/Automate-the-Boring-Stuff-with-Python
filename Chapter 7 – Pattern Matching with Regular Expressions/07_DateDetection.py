import re


# regular Expression to find the date
regExp = re.compile(r'''
      (0[0-9]|1[0-9]|2[0-9]|3[0-1])
      /
      (0[0-9]|1[0-2])
      /
      (1\d{3}|2\d{3})
''', re.VERBOSE)


datesList = []

mo = regExp.findall(
    '01/12/2012/ bla bla bla bla 31/02/2018 bla bla bla bla 28/02/2018 bla bla bla bla 31/06/2000   bla bla bla bla 17/04/2018')


def validDate(day, month, year):

    # February has 28 days
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if day > 29:
                return
        if day > 28:
            return False

    # pril, June, September, and November have 30 days
    if(month == 4 or month == 6 or month == 9 or month == 11):
        if day > 30:
            return False

    return True


for date in mo:
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])

    if validDate(day, month, year):
        datesList.append('/'.join(date))


print(datesList)
