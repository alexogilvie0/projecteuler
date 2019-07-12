#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 16: Power digit sum
    
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?


"""
import time
def compute():
    timer = time.time()
    digits = list(str(2**1000))
    ans = 0
    for i in range(len(digits)):
        ans += int(digits[i])
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans