"""
    datetime module consists many functions
    coresponds to date and time
"""
import datetime

# datetime() construct datetime in format
print(datetime.datetime(2020, 2, 5, 15, 41, 34))
# current date and time
t = datetime.datetime.today()
# accessing single single
print(t.year, end='-')
print(t.month, end='-')
print(t.day, end='-')
print(t.hour, end='-')
print(t.minute, end='-')
print(t.second)
print(datetime.datetime.now())
# date() method to create date
print(datetime.date(2020, 2, 5))
# time() method to create time
print(datetime.time(14, 55, 30))

# timedelta class
"""
    timedelta class used for performing differnet
    mathematical operations on datetime
"""
b1 = datetime.timedelta(days=30, hours=14)
b2 = datetime.timedelta(days=20, hours=11)
b3 = b1 - b2
print(b3)
print(type(b3))
