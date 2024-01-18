#!/usr/bin/python3

if __name__ == "__main__":
    '''program'''
    import sys

    def args(argv):
        arguments = argv[1:]

        if arguments:
            result = sum(map(int, arguments))
            print(result)
    args(sys.argv)
