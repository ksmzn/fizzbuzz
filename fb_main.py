#!/usr/bin/env python
#coding:utf-8
"""
"""

import sys

def fizzbuzz(num):
    maybeInt = str(num)
    isPositive = num>0
    isInt = isinstance(num,int)
    if not isInt or not isPositive:
        return maybeInt
    else:
        isDivisibleBy3 = num % 3 == 0
        isDivisibleBy5 = num % 5 == 0

    if isDivisibleBy3 and isDivisibleBy5:
        return "FizzBuzz"
    elif isDivisibleBy3:
        return "Fizz"
    elif isDivisibleBy5:
        return "Buzz"
    else:
        return maybeInt

def main():
    argvs = sys.argv
    argc = len(argvs)
    if argc != 2:
        print 'Usage: # python %s filename' % argvs[0]
        quit()

    try:
        argvs[1] = int(argvs[1])
    except ValueError:
        pass

    print fizzbuzz(argvs[1])


if __name__ == '__main__':
    main()

