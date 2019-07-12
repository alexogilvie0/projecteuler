#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

import time
def compute():
    timer = time.time()
    ans = 0
    for i in range(999, 100, -1):
        for j in range(999, 100,-1):
            prod = str(i*j)
            if(prod == prod[::-1] and i*j > ans):
                ans = i*j
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans