#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 34: Digit factorials

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

"""
import time
from math import factorial
def compute():
    timer=time.time()
    # If n has 7 digits, the max digit factorial sum is 7*9! = 2540160, so no value larger than this can fit this formula
    # This is an upper bound and may be able to be reduced further (the actual highest is 40585)
    ans = sum(n for n in range(10, 2540161) if sum(factorial(int(d)) for d in str(n)) == n)
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans