#!/usr/bin/python3
if __name__ == "__main__":
    ''' print sum sub mul div from module'''
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{} + {} = {}\n{} - {} = {}".format(a, b, add(a, b), a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, add(a, b)))
