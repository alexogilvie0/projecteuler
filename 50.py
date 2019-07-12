#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 50: Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""
import time
from util import isPrime, getPrimes
def compute():
    timer = time.time()
    primes = getPrimes(1000000)
    longest = 0
    for i in range(len(primes)//4):
        chain = 1
        total = primes[i]
        while total + primes[i+chain] < 1000000:
            total += primes[i+chain]
            chain += 1
        if chain > longest and isPrime(total):
            longest = chain
            ans = total
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans