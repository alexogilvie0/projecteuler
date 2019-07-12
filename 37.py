#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 37: Truncatable primes

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

"""
import time
from util import isPrime
def compute():
    timer = time.time()
    tp = []
    i = 11
    while len(tp) < 11:
        if isPrime(i):
            s = str(i)
            if all(isPrime(int(s[:j])) and isPrime(int(s[j:])) for j in range(1,len(s))):
                tp.append(i)
        i+=2
    print ("Answer is " + str(sum(tp)) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return sum(tp)