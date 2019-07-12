#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 20: Factorial digit sum
    
Find the sum of the digits in the number 100!
"""
import time
from math import factorial
def compute():
    timer = time.time()
    ans = sum(int(i) for i in str(factorial(100)))
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans