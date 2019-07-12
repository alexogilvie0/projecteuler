#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 46: Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

"""
import time
from util import isPrime
def isGoldbach(n):
    if n % 2 == 0 or isPrime(n): # Not a composite
        return True
    for i in range(1,n+1):
        remainder = n - 2 * i**2
        if remainder <= 0:
            return False
        elif isPrime(remainder):
            return True

def compute():
    timer = time.time()
    i = 1
    goldbach = True
    while goldbach:
        i += 1
        goldbach = isGoldbach(i)
    ans = i
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans