#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 33: Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""
import time
def compute():
    timer=time.time()
    fractions = [[n,d] for n in range(10,100) for d in range(10,100) if n!=d and isCurious(n,d)]
    totnum=1
    totden=1
    for frac in fractions:
        totnum *= frac[0]
        totden *= frac[1]
    ans = totden//totnum
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans

def isCurious(num,den):
    curious = 0
    if str(num)[1] == str(den)[0] and str(den)[1] != '0':
        curious = int(str(num)[0])/int(str(den)[1])
    if num/den == curious:
        return True