#!/usr/bin/python3
'''This program will assign a random signed number\
    to the variable number each time it is executed'''
import random
number = random.randint(-10000, 10000)

lastDigit = abs(number) % 10

if number > 0:
    if lastDigit > 5:
        print(f'Last digit of {number} is {lastDigit} and is greater than 5')
    elif 0 < lastDigit < 6:
        print(f'Last digit of {number} is {lastDigit} \
        and is less than 6 and not 0')
elif number < 0:
        print(f'Last digit of {number} is -{lastDigit} \
        and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is {lastDigit} and is 0')
