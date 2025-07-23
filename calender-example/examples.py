import calendar

'''Prints all 2025 calender months'''
print(calendar.calendar(2025))

'''Print month of 2025'''
print(calendar.month(2025, 7))

'''set first day of week from sunday to monday'''
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2025, 7)

'''Gives day of the week, monday is 0'''
print(calendar.weekday(2025, 7, 14))

'''check leap year methods'''
print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.

'''Returns weekdays from 0 - 6'''
c = calendar.Calendar(calendar.SUNDAY)
for weekday in c.iterweekdays():
    print(weekday, end=" ")

print("")
'''print week headers'''
print(calendar.weekheader(3))
