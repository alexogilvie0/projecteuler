#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Utility functions

"""

from math import ceil, sqrt

def getPrimes(n): # Get all the prime numbers under n using a Sieve of Eratosthenes
    isprime = [True for i in range(n+1)]
    for i in range(2, ceil(sqrt(len(isprime)))):
        if isprime[i] == True:
            p = i
            for j in range(p**2,len(isprime), p):
                isprime[j] = False
    return [i for i in range(len(isprime)) if isprime[i] == True and i != 1]

def isPrime(n): # Returns if a value is prime or not
    if n <= 1:
        return False
    elif n%2 == 0 and n != 2:
        return False
    else:
        for i in range(3, ceil(sqrt(n)+1), 2):
            if n%i == 0:
                return False
        return True

def getFactors(n):
    factors = []
    step = 2 if n%2 else 1
    for i in range(1, int(sqrt(n))+1, step):
        if n % i == 0:
            factors.append(i)
            if i != 1:
                factors.append(n//i)
    return factors      
    