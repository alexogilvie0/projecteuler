#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 28: Number spiral diagonals
    
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed 
starting with the number 1 and moving to the right in a clockwise direction

"""
import time
def compute():
    timer = time.time()
    value = 1
    ans = 1
    increment = 2
    while value < (1001*1001):
        for i in range(4):
            value += increment
            ans += value
        increment += 2
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans