#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = "-" + str(number)[-1]
else:
    n = str(number)[-1]
cond = ""
if int(n) > 5:
    cond = "and is greater than 5"
elif int(n) == 0:
    cond = "and is 0"
else:
    cond = "and is less than 6 and not 0"
print(f"Last digit of {number:d} is {n} {cond}")
