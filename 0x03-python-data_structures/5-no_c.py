#!/usr/bin/python3
def no_c(my_string):
    stringList = list(my_string)

    for i in stringList:
        if i.lower() == 'c':
            stringList.remove(i)
        newString = ''.join(stringList)
    return newString
