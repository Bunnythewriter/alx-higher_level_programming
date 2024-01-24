#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''a function that replaces all occurrences of \
        an element by another in a new list.'''
    list = [replace if item == search else item for item in my_list]
    return list
