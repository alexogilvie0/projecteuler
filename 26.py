#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 26: Reciprocal cycles
    
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""
import time
def compute():
    timer = time.time()
    length = 0
    ans = 0
    for i in range(2,1001):
        if i%2 != 0 and i%5 != 0:
            k = 1
            while 10**k % i != 1:
                k+=1
            if k > length:
                length = k
                ans = i
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans