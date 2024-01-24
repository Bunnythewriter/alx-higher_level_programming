#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''a function that prints a dictionary by ordered keys.'''
    sortedKeys = sorted(a_dictionary)
    for k in sortedKeys:
        print('{}: {}'.format(k, a_dictionary[k]))
