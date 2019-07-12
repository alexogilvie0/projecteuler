#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 13: Large sum
    
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    
"""
import time
def compute():
    timer = time.time()
    file = open('13.txt')
    ans = 0
    for line in file:
        ans += int(line)
    ans = str(ans)[:10]
    print ("Answer is " + ans + ". Completed in "+str(time.time()-timer)+" seconds.")
    return int(ans)