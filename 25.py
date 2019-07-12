#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 25: 1000-digit Fibonacci number
    
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""
import time
def compute():
    timer = time.time()
    fib = [1,1]
    while len(str(fib[-1])) < 1000:
        fib.append(fib[-1]+fib[-2])
    print ("Answer is " + str(len(fib)) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return len(fib)