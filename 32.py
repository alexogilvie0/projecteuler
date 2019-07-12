#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 32: Pandigital products

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

"""
import time
from math import sqrt
def compute():
    timer = time.time()
    products = [n for n in range(10000) if isPandigitalProduct(n)]        
    ans = sum(set(products))
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans

def isPandigitalProduct(n):
    for i in range(1, int(sqrt(n) +1)):
        if n%i == 0:
            digits = sorted([d for d in str(n)+str(i)+str(n//i)])
            if digits == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return True
    return False      