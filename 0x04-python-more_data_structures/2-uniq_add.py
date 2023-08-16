#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    unique_num = set()
    for i in my_list:
        if i not in unique_num:
            unique_num.add(i)
            res += i
    return res
