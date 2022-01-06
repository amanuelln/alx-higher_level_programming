#!/usr/bin/python3
if __name__ == '__main__':
        import sys

        num_arg = len(sys.argv) - 1

        if num_arg == 0:
            print("{:d} argument:".format(num_arg))
        elif num_arg == 1:
            print("{:d} argument:".format(num_arg))
            print("{:d} {}".format(num_arg, sys.argv[num_arg]))
        else:
            print("{:d} argument:".format(num_arg))
            number = 1
            for i in sys.argv:
               print("{:d} {}".format(number, i))
               number = number + 1
