# Take two dates and display number of days between them
from datetime import datetime, timedelta

d1_st = input("Enter first date [yyyymmdd]  :")

try:
    fd = datetime.strptime(d1_st, "%Y%m%d")
except ValueError:
    print(f"Sorry! Invalid first date : {d1_st}")
    exit(1)

d2_st = input("Enter second date [yyyymmdd] :")
try:
    sd = datetime.strptime(d2_st, "%Y%m%d")
except ValueError:
    print(f"Sorry! Invalid second date : {d2_st}")
    exit(2)

days = (sd - fd).days
print("No. of days = ", days)
