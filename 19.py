#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 19: Counting Sundays
    
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""
import time
import datetime
def compute():
    timer = time.time()
    ans = sum(1 for y in range(1901, 2001) for m in range(1, 13) if datetime.date(y, m, 1).weekday() == 6)
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans
