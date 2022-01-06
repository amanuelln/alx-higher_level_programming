#!/usr/bin/python3
if __name__ == "__main__":
        import sys

        sys.argv.pop(0)
        total = 0
        for numbers in sys.argv:
                total = total + int(numbers)
        print("{:d}".format(total))
