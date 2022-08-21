import time
from calendar import isleap

def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

def month_days(month, leap_year):
    if month in [1,3,5,7,8,9,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        if leap_year:
            return 29
        else:
            return 28

name = input("Please enter your name:")
age = int(input("Please enter your age: "))
localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

for y in range(begin_year, end_year):
    if judge_leap_year(y):
        day += 366
    else:
        day += 365

leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day += month_days(m, leap_year)

day += localtime.tm_mday
print("%s's age is %d years or " %(name, year))
print("%d months or %d days" %(month, day))