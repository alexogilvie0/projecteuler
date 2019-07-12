#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 47: Distinct prime factors

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

"""
import time
from util import getFactors, isPrime

def compute():
    timer = time.time()
    i = 644
    consecutive = []
    while len(consecutive) < 4:
        if len([x for x in getFactors(i) if isPrime(x)]) == 4:
            consecutive.append(i)
        else:
            consecutive = []
        i += 1
    print ("Answer is " + str(consecutive[0]) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return consecutive[0]