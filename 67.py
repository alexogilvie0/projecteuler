#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 67: Maximum path sum II
    
Find the maximum total from top to bottom of the triangle, by starting at the top of the triangle and moving to adjacent numbers on the row below,

"""
import time
def compute():
    timer = time.time()
    file = open('67.txt')
    numbers = []
    for line in file:
        numbers.append([int(number) for number in line.split(' ')])
    maxsum = []
    for i in range(len(numbers)):
        maxsum.append([])
    maxsum[len(numbers)-1] = numbers[len(numbers)-1]
    for i in range(len(numbers)-2, -1, -1):
        for j in range(len(numbers[i])):
            maxsum[i].append(max(numbers[i][j] + maxsum[i+1][j], numbers[i][j] + maxsum[i+1][j+1]))
    print ("Answer is " + str(maxsum[0][0]) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return maxsum[0][0]