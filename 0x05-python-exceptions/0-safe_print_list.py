#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for elem in my_list:
            if count < x:
                print("{:d}".format(elem), end='')
                count += 1
            else:
                break
        print()
        return count
    except Exception as e:
        print("An error occurred:", e)
        return count
