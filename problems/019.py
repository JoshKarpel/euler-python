import time
from math import sqrt
from math import ceil
import numpy as np


def days_per_month(year):
    if year % 4 == 0:
        return 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    else:
        return 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

def days_per_year(year):
    return sum(days_per_month(year))

def first_day_of_month(year):
    if year % 4 == 0:
        return 1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336
    else:
        return 1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335


start_time = time.clock()

# print(days_per_month(1901))
# print(sum(days_per_month(1901)))
# print(days_per_month(1904))
# print(sum(days_per_month(1904)))
#
# print(np.cumsum(days_per_month(1903)))
# print(np.cumsum(days_per_month(1904)))
#
# number_of_days = sum([sum(days_per_month(year)) for year in range(1901, 2001)])
# print(number_of_days)
#
# days = range(366, number_of_days + 1)
# sundays = [day % 7 == 1 for day in days]
# print(list(days))
# print(sundays)
#
# days_mod_year = [day % 365 for day in days]
# print(days_mod_year)

days = []
sundays = []

current_day = 365
for year in range(1901, 2001):
    for day in range(days_per_year(year)):
        current_day += 1
        days.append(current_day)
        if day in first_day_of_month(year) and current_day % 7 == 1:
            sundays.append(current_day)

print(days)
print(sundays)
print(len(sundays))

end_time = time.clock()

print('Elapsed Time: ' + str(end_time - start_time))
