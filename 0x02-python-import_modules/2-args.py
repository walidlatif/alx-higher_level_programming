#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) > 1:
        print("{:d} argument{:s}".format(len(argv) - 1, "s:" if len(argv) > 2 else ":"))
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))
