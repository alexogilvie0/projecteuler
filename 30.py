#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 30: Digit fifth powers

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""
import time
def compute():
    timer = time.time()
    ans = sum(i for i in range(2,1000000) if i == sum(int(v)**5 for v in str(i)))
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans