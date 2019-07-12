#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 38: Pandigital multiples

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""
import time
timer = time.time()
def isPandigital(n):
    digits = sorted([d for d in n])
    return digits == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def compute():
    max_number = 0
    for i in range(10000):
        number = str(i)
        multiplier = 2
        while len(number) < 9:
            number = number + str(i*multiplier)
            multiplier += 1
        if len(number) == 9 and isPandigital(number) and int(number) > max_number:
                max_number = int(number)
    print ("Answer is " + str(max_number) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return max_number
