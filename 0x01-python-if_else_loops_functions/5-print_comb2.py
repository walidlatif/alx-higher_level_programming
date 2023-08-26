#!/usr/bin/python3
for number in range(0, 100):
    separator = ", "
    if number == 99:
        separator = "\n"
    print("{:02d}".format(number), end=separator)
