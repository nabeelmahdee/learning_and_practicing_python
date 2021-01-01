import datetime

d=datetime.date.today()

print(d.year)
print(d.day)
print(d.month)

print(d.weekday()) #monday 0 tuesday 1
print(d.isoweekday()) # monday 1 tuesday 2

timedelta = datetime.timedelta(days=7)

print(d+timedelta)

bday = datetime.date(2021, 12, 24)

till_bday=bday - d

print(till_bday.total_seconds())

import datetime.time

dt = 
