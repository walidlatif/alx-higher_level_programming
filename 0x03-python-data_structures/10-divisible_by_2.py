#!/usr/bin/python3
def divisible_by_2(my_list=None):
    if my_list is None or len(my_list) == 0:
        return []

    new_list = [True if num % 2 == 0 else False for num in my_list]
    return new_list
