#!/usr/bin/python3
def safe_print_integer(value):
    ''' A function that prints an integer with "{:d}".format()'''
    try:
        if isinstance(value, int):
            print('{:d}'.format(value))
    except TypeError:
        return False
    return True
