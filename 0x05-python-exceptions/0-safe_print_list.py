#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''A function that prints x elements of a list.'''
    count = 0
    try:
        for elements in range(x):
            print(my_list[elements], end="")
            count += 1
        print()
        return count
    except:
        print()
        return count
    print()
    return count
