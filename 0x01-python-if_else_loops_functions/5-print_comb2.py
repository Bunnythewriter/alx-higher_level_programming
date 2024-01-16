#!/usr/bin/python3
'''A program that prints numbers from 0 to 99'''
for i in range(100):
    if i < 10:
        print('0{:d}'.format(i), end=", ")
    else:
        print('{:d}'.format(i), end=", " if i != 99 else "\n")
