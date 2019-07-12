#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 39: Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

"""
import time
from math import sqrt
def compute():
    timer = time.time()
    ways = [0 for i in range(1001)]
    for a in range(1,1000):
        for b in range(a,1000):
            c = sqrt(a**2 + b**2)
            if c.is_integer() and a+b+c<=1000:
                ways[int(a+b+c)] += 1
    ans = ways.index(max(ways))
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans
