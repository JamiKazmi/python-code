"""
    time module have many methods that are useful
    time() method calculates the time in seconds from
    'epoch' which is 1-1-1997
"""
import time

print(time.time())
# current date and time it takes seconds as parameter
print(time.ctime(1580836023))
# localtime() method returns local time in struct fromat
a = time.localtime()
# mktime() returns the seconds since epoch
b = time.mktime(a)
print(b)
# asctime() method give us time in local format
c = time.asctime(a)
print(c)
# strftime() method return time in given format
print(time.strftime('%m\\%d\\%Y'))
# strptime() method return time in struct format
y = '05 February 2020'
x = time.strptime(y, '%d %B %Y')
print(x)
