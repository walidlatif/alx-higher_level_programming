#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside quotient: {}".format(quotient))
        return quotient
