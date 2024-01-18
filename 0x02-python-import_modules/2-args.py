#!/usr/bin/python3

def argCount(argv):
    '''counts and prints args'''
    if len(argv) > 2:
        print('{} arguments:'.format(len(argv) - 1))
        for i, arg in enumerate(argv[1:], 1):
            print('{}: {}'.format(i, arg))
    elif len(argv) == 2:
        print('1 argument:')
        print('1: {}'.format(argv[1]))
    else:
        print('0 arguments.')


if __name__ == "__main__":
    '''A program that prints the num of arguments'''
    import sys

    argv = sys.argv
    argCount(argv)
