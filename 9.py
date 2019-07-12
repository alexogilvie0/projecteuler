#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 9: Special Pythagorean triplet
    
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Euclid's formula for a Pythagorean triple

    a = 2 m n , b = m^2 − n^2 , c = m^2 + n^2 
"""
import time

def result():
    for n in range(0,1000):
        for m in range(n+1,1000):
            a = 2 * m * n
            b = m**2 - n**2
            c = m**2 + n**2
            if a + b + c == 1000:
                return [a,b,c,a*b*c]

def compute():
    timer = time.time()    
    ans = result()
    print ("Answer is " + str(ans[0:3]) + ", product is " + str(ans[3]) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans[3]
