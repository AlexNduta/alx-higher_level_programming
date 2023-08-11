#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s1 = "and is greater than 5"
s2 = " and is 0"
s3 = "and is less than 6 and not 0"
last_dig = abs(number) % 10
if last_dig > 5:
    print(f"Last digit of {number} {s1}")
elif last_dig == 0:
    print(f"Last digit of {number} {s2}")
else:
    print(f"Last digit of {number} {s3}")
