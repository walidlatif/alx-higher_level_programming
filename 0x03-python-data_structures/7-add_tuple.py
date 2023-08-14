#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    sum_first_elements = a[0] + b[0]
    sum_second_elements = a[1] + b[1]
    return sum_first_elements, sum_second_elements
