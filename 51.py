#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 51: Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

"""
import time
from util import isPrime
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)  # allows duplicate elements
    return chain.from_iterable(combinations(s, r) for r in range(1,len(s)))

def countPrimes(n, exc):
    primes = []
    if 0 in exc:
        a = 1
    else:
        a = 0
    for x in range(a, 10):
        s = str(n)
        for val in exc:
            s = s[:val] + str(x) + s[val + 1:]
        if s[0] != '0' and isPrime(int(s)):
            primes.append(int(s))
    return primes

def compute():
    timer = time.time()
    i = 56003
    ans = 0
    while ans == 0:
        if isPrime(i):
            for j, combo in enumerate(powerset(range(len(str(i)))), 1):                
                primes = countPrimes(i, combo)
#                print(i, combo, primes)
                if len(primes) > 7:
                    ans = min(primes)
        i += 1
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans