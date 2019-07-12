#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 43: Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

"""
import time
from itertools import permutations
def compute():
    timer = time.time()
    perms = sorted(list(permutations([str(i) for i in range(10)])), reverse=True)
    ans = 0
    for x in perms:
        if int(x[1] + x[2] + x[3]) % 2 == 0 and int(x[2] + x[3] + x[4]) % 3 == 0 and int(x[3] + x[4] + x[5]) % 5 == 0 and int(x[4] + x[5] + x[6]) % 7 == 0 and int(x[5] + x[6] + x[7]) % 11 == 0 and int(x[6] + x[7] + x[8]) % 13 == 0 and int(x[7] + x[8] + x[9]) % 17 == 0:
            s = ''
            for d in x:
                s = s + d
            ans += int(s)
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans