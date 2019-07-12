#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 21: Amicable numbers
    
Evaluate the sum of all the amicable numbers under 10000.

Amicable numbers are when the sum of the proper divisors d(a) = b and d(b) = a where a != b 

"""
import time
from util import getFactors
def compute():
    timer = time.time()
    ans = 0
    for i in range(10001):
        di = sum(getFactors(i))
        if di < 10001 and di != i and sum(getFactors(di)) == i:
            ans = ans + di + i    
    print ("Answer is " + str(int(ans/2)) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return int(ans/2)