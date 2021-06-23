# Take month number and display number of days

month = int(input("Enter month :"))
if month == 2:
    year = int(input("Enter year :"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days = 29
    else:
        days = 28
# elif month == 4 or month == 6 or month == 9 or month == 11:
elif month in [4, 6, 9, 11]:
    days = 30
else:
    days = 31

print('No. of days = ', days)
