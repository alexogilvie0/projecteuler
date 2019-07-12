#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 2: Even Fibonacci numbers
    
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""
import time
def compute():
    timer = time.time()
    fib = [1,2]
    while fib[-1] + fib[-2] < 4000000:
        fib.append(fib[-1]+fib[-2])
    ans = sum(x for x in fib if (x % 2 == 0))
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans