#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 12: Highly divisible triangular number
    
What is the value of the first triangle number to have over five hundred divisors?
    
"""
import time
import math
def compute():
    timer = time.time()
    triangular = 0
    i = 1
    factors = 0
    while factors <= 500:
        triangular = triangular + i
        factors = sum(2 for j in range(1, int(math.sqrt(triangular))+1) if triangular % j == 0)
        if math.sqrt(triangular)**2 == triangular:
            factors -= 1
        i += 1
    print ("Answer is " + str(triangular) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return triangular