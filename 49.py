#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 49: Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

"""
import time
from util import isPrime
def compute():
    timer = time.time()
    for i in range(1000, 3341):
        if isPrime(i) and isPrime(i+3330) and isPrime(i+6660) and set([d for d in str(i)]) == set([d for d in str(i+3330)]) and set([d for d in str(i)]) == set([d for d in str(i+6660)]) and i != 1487:
            ans = int(str(i) + str(i+3330) + str(i+6660))
            break
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans