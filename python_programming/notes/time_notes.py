#RA yth notes about time

import time 

import datetime

current = time.time()

readabletime = time.ctime(current)

print(f"The time in seconds since Jan 1 1970: {current}")
print(f"the time is {readabletime}")

now = datetime.datetime.now()

seconds = now.second

hour = now.hour

minutes = now.minute

print(f"the time is {now}")
print(f"the hour is {hour}")
print(f"the minutes is {minutes}")
print(f"the number of seconds is {seconds}")

