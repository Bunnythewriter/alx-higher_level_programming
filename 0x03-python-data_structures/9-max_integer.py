#!/usr/bin/python3
def max_integer(my_list=[]):
    '''a function that finds the biggest integer of a list.'''
    if len(my_list) == 0:
        return None
    else:
        '''List Index for each item'''
        i = len(my_list) - 1
        '''Outer loop that decreases'''
        while i > 1:
            '''Inner loop that increases'''
            j = 0
            while j < i:
                if my_list[j] > my_list[j + 1]:
                    '''Swap values'''
                    temp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = temp
                j += 1
            i -= 1
        '''Print Max number'''
        return my_list[-1]
