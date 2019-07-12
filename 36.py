#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 36: Double-base palindromes

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

"""
import time
def compute():
    timer = time.time()
    ans = sum(i for i in range(1000000) if isPalindrome(i) and isPalindrome(bin(i)[2:]))
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans

def isPalindrome(n):
    s = str(n)
    return s == s[::-1]