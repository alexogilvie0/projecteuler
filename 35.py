#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 35: Circular primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""
import time
from util import isPrime
def compute():
    timer = time.time()
    primes = []
    for i in range(1000000):
        s = str(i)
        l = [int(s[j:] + s[:j]) for j in range(len(s))]
        if all(isPrime(val) for val in l):
            primes = primes + l
    ans = len(set(primes))
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans