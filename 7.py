#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

The prime number theorem estimates the number of primes under n to be n/ln(n) which is 120,000, 
Using a sieve of Eratosthenes, we calculate the primes up to 120,000 and find the 10001st.

"""
import time
from util import getPrimes
def compute():
    timer = time.time()
    ans = getPrimes(120000)[10001]
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans