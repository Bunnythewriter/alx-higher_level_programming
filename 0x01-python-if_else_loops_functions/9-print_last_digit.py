#!/usr/bin/python3
def print_last_digit(number):
    '''a function that prints the last digit of a number.'''
    lastDigit = abs(number) % 10
    print(lastDigit, end='')
