#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 41: Pandigital Prime

What is the largest n-digit pandigital prime that exists?

"""
import time
from itertools import permutations
from util import isPrime
def compute():
    timer = time.time()
    ans = 0
    for length in range(9,0,-1):
        if ans == 0:
            perms = sorted(list(permutations([str(i) for i in range(1,length+1)])), reverse=True)
            for p in perms:
                s = ''
                for d in p:
                    s = s + d
                if isPrime(int(s)):
                    ans = int(s)
                    break
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans
