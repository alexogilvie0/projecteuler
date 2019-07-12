#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 27: Quadratic primes
    
Considering quadratics of the form:

    n^2+an+b,

where |a|<1000 and |b|≤1000

Find the product of the coefficients, a and b, for the quadratic expression that produces
the maximum number of primes for consecutive values of n, starting with n=0.

"""
import time
from util import isPrime
def compute():
    timer = time.time()
    ans = 0
    maxprimes = 0
    for b in range(1000,0,-1):
        if isPrime(b): # b must be positive and prime as when n=0, ans = b which must be prime
            for a in range(-999,1000):
                primes = 1
                for n in range(1,b):
                    if isPrime(n**2+a*n+b):
                        primes += 1
                    else:
                        break
                if primes > maxprimes:
                    maxprimes = primes
                    ans = a*b
            if maxprimes == b: # Break when we find the largest value b where for all x, f(x) < b is prime
                break
            
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans