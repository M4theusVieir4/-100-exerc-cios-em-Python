
from datetime import date
year = int(input('Which year are you?Choice 0 to analized the actual year : '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print('{} This is a leap year! '.format(year))

else:
    print('{} This is not a leap year! '.format(year))