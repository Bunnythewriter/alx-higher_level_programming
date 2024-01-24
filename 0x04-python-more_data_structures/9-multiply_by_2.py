#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ''' a function that returns a new dictionary with all values multiplied by 2'''
    if a_dictionary is not None:
        new = a_dictionary.copy()
        for key in a_dictionary:
            new[key] = a_dictionary[key] * 2
        return new
    else:
        return