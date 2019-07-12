#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 3: Largest prime factor
    
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import time
def compute():
    timer = time.time()
    value = 600851475143
    factors = []
    i=2
    while value > 1:
        if (value % i == 0):
            factors.append(i)
            value = value / i
        i+=1
    ans = max(factors)
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans