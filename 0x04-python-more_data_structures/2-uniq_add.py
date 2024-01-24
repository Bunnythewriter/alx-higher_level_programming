#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''a function that adds all unique integers in a list'''
    a = set(my_list)
    result = sum(a)
    return result
