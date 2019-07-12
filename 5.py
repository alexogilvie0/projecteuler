#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
from math import gcd
import time
def compute():
    timer = time.time()
    ans = 1
    for i in range(1, 21):
        ans *= i // gcd(i, ans)
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans