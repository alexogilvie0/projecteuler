#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 52: Permuted multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""
import time
def compute():
    timer = time.time()
    i = 1
    while True:
        if (set([d for d in str(i)]) == set([d for d in str(2*i)]) and 
                set([d for d in str(i)]) == set([d for d in str(3*i)]) and 
                set([d for d in str(i)]) == set([d for d in str(3*i)]) and
                set([d for d in str(i)]) == set([d for d in str(3*i)]) and
                set([d for d in str(i)]) == set([d for d in str(3*i)])):
            ans = i
            break
        i += 1
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans