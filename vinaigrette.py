"#hadasa-web"
# from datetime import date, datetime, timedelta
from datetime import date, datetime
import time
import random

date_input = input("enter a date1:")
date_input2 = input("enter a date2:")
datea = date_input.split("-")
year1 = int(datea[0])
m1 = int(datea[1])
day1 = int(datea[2])
d = date(year1, m1, day1)
datea2 = date_input2.split("-")

year2 = int(datea2[0])
m2 = int(datea2[1])
day2 = int(datea2[2])
d2 = date(year2, m2, day2)
try:
    d1 = random.randrange(time.mktime(d.timetuple()), time.mktime(d2.timetuple()))
    dnew = time.localtime(d1)
    ddate = time.strftime("%Y-%m-%d", dnew)
    print(ddate)
    if dnew.tm_wday == 0:
        print("I have no vinaigrette")

except:
    print("error")

# enter a data1:2022-02-14
# enter a data2:2022-03-14
