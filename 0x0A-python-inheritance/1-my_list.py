#!/usr/bin/python3
'''
Module prints the list, but sorted (ascending sort)
'''


class MyList(list):
    '''
    prints the list, but sorted (ascending sort)
    '''
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
