#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 31: Coin sums

How many different ways can £2 be made using any number of coins?

"""
import time
def compute():
    timer = time.time()
    sums = [1] + [0] * 200
    # We calculate the number of ways to create every value, and use this to calculate higher numbers
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
    	for i in range(len(sums) - coin):
             sums[i + coin] += sums[i]
    print ("Answer is " + str(sums[-1]) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return sums[-1]