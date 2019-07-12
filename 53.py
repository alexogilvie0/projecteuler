#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 53: Combinatoric selections

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3=10

In general, nCr=n!r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1

It is not until n=23, that a value exceeds one-million: 23C10=1144066

How many, not necessarily distinct, values of nCr
for 1≤n≤100, are greater than one-million?

"""
import time
from math import factorial
def compute():
    timer = time.time()
    ans = sum(1 for n in range(23,101) for r in range(n) if factorial(n)/(factorial(r) * factorial(n-r)) > 1000000)
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans