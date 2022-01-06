#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    sys.argv.pop(0)
    num_arg = len(sys.argv)

    if num_arg == 0:
        print("0 argument.")
    elif num_arg == 1:
        print("1 argument:")
        print("{:d}: {}".format(num_arg, sys.argv[0]))
    else:
        print("{:d} argument:".format(num_arg))
        number = 1
        for i in sys.argv:
            print("{:d}: {}".format(number, i))
            number = number + 1
