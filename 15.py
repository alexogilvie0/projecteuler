#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 15: Lattice paths
    
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

This is a combinations problem. There are a total of 40 moves to get from one corner to the other, and 20 of these need to be down.
Hence the answer is 40C20 = 40!/(20!*20!)

"""
import time
import math
def compute():
    timer = time.time()
    ans = int(math.factorial(40)/math.factorial(20)**2)
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans