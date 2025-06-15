#!/usr/bin/env python3

""" module.py - an example of a Python module """

__counter = 0

def sum_l(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prod_l(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(my_list)
    print(sum_l(my_list) == 15)
    print(prod_l(my_list) == 120)

