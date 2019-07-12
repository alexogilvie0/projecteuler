#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 6: Sum square difference
    
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""
import time
def compute():
    timer = time.time()
    values = list(range(1,101))
    total = sum(values)
    squares = map(lambda x: x*x, values)
    ans = total**2 - sum(squares)
    
    # Alternate solution using formula for sum of squares and square of sum
    #n=100
    #diff = (n**4 / 4) + (n**3 / 6) - (n**2 / 4) - (n / 6)
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans