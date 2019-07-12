#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 22: Names scores
    
Using names.txt, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

What is the total of all the name scores in the file?

"""
import time
def compute():
    timer = time.time()
    names = open('22.txt').read().split(',')
    names = sorted(names)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = 0
    for i, name in enumerate(names):
        ans += (i+1)*(sum(alphabet.index(letter)+1 for letter in name if letter in alphabet))
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans