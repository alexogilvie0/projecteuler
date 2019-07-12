#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 14: Longest Collatz sequence
    
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Which starting number, under one million, produces the longest chain?
    
"""
import time
timer = time.time()
def compute():
    ans = 0
    largest = 0
    chains = [0, 0]
    for i in range(2, 1000000):
        chain = 0
        value = i
        while i <= value:
            chain += 1
            if value % 2 == 0:
                value /= 2
            else:
                value = 3*value+1
        chains.append(chains[int(value)] + chain)
        if chains[-1] > largest:
            ans = i
            largest = chains[-1]
    print ("Answer is " + str(ans) + " with chain length " + str(largest) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans