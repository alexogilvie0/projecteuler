#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 17: Number letter counts
    
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

"""
import time
def compute():
    timer = time.time()
    ans = 0
    for i in range(1, 1001):
        ans += countLetters(i)
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans

def countLetters(n):
    digits = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
    tens = [0,0,6,6,5,5,5,7,6,6]
    hundred = 7
    if n < len(digits):
        return digits[n]
    elif n < 100:
        return tens[int(str(n)[0])] + digits[int(str(n)[1])]
    elif n < 1000:
        return digits[int(str(n)[0])] + hundred + (3 + countLetters(n % 100) if n % 100 != 0 else 0) 
    else:
        return 11