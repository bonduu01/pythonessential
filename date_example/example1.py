import time
from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

'''timestamp'''
timestamp = time.time()
print("Timestamp:", timestamp, end='\n')
print(time.ctime(timestamp))

d = date.fromtimestamp(timestamp)
print("Date:", d)

'''Replace method'''
d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=10, day=26)
print(d)

'''Returns weekday'''
d = date(2025, 7, 14)  # 0 is monday, sunday is 6
print(d.weekday())

'''Also returns weekday'''
d = date(2025, 7, 14)  # 1 is Monday, and 7 is Sunday
print(d.isoweekday())

from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)

from datetime import datetime, UTC

'''Return current day'''
print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.now(UTC))

'''format date'''
from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

from datetime import time

t = time(14, 53)
print(t.strftime("%H:%M:%S"))
