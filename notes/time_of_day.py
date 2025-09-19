#RA 7th Time of Day assignment

import time 

import datetime

current = time.time()

readabletime = time.ctime(current)

now = datetime.datetime.now()

hour = 21

if hour >= 6 and not hour >= 13: 
    print(f"Goodmorning my friend it is {hour}")
elif hour >= 13 and not hour >= 21:
    print(f"Good afternoon my friend it is {hour}")
else:
    print(f"Goodnight my friend it is {hour}")
