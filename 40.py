#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 40: Champernowne's constant

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

"""
import time
def compute():
    timer = time.time()
    s = '0.'
    i = 1
    while len(s) < 1000002:
        s = s + str(i)
        i += 1
    ans = int(s[2])*int(s[11])*int(s[101])*int(s[1001])*int(s[10001])*int(s[100001])*int(s[1000001])
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans
