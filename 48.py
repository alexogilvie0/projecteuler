#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 48: Self powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""
import time

def compute():
    timer = time.time()
    ans = str(sum(i**i for i in range(1,1000)))[-10:]
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return int(ans)


""" 
Pj = j(3j-1)/2
Pk = k(3k-1)/2
Pd = Pj - Pk = j(3j-1)/2 - k(3k-1)/2 = d(3d-1)/2
Ps = Pj + Pk = j(3j-1)/2 + k(3k-1)/2 = s(3s-1)/2
3d^2 - d - 3j^2 + 3k^2 + j - k = 0 => a=1, b=-1, c= 3k^2 - 3j^2 + j - k
3s^2 - s - 3j^2 - 3k^2 + j + k = 0 => a=1, b=-1, c= -3k^2 - 3j^2 + j + k

-b+-sqrt(b^2-4ac)/2a

1+-sqrt(1-4(3k^2 - 3j^2 + j - k))/2
"""