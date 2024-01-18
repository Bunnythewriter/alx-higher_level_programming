#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    import sys
    arguments = sys.argv
    argc = len(arguments)
    a = int(arguments[1])
    b = int(arguments[3])
    operator = arguments[2]

    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if operator != '+' and operator != '-'\
            and operator != '*' and operator != '/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    print("{:d} {} {:d} = {:d}".format(a, operator, b,
                                    add(a, b) if operator == '+' else
                                    sub(a, b) if operator == '-' else
                                    mul(a, b) if operator == '*' else
                                    div(a, b)))
