#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result_tuple = ()
    for in range(len(tuple_a)):
        sum_element = tuple_a[0] + tuple_b[0]
        result_tuple += (sum_element,)
    return result_tuple
