#!/usr/bin/python3
def uppercase(str):
    '''a function that prints a string in uppercase followed by a new line.'''
    uppercase_str = ''.join([c if not 'a' <= c <= 'z' else
                            chr(ord(c) - ord('a') + ord('A')) for c in str])
    print('{}'.format(uppercase_str))
