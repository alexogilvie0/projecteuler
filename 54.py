#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 54: Poker hands

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

"""
import time
VALUES = "123456789TJQKA"
SUITS = "SHCD"

def p1_wins(h1, h2):
    return score(h1) > score(h2)

#.    High Card: Highest value card. 1 - 13
#.    One Pair: Two cards of the same value. 101 - 1313
#.    Two Pairs: Two different pairs. 1401 - 3913
#.    Three of a Kind: Three cards of the same value. 4000 - 5300 (high card does not matter)
#.    Straight: All cards are consecutive values. 10001 - 10013
#.    Flush: All cards of the same suit. 11001 - 11013
#.    Full House: Three of a kind and a pair. 12000 - 26300
#.    Four of a Kind: Four cards of the same value. 27000 - 28300 (high card does not matter)
#.    Straight Flush: All cards are consecutive values of same suit. 30001 - 30012
#.    Royal Flush: 30013 
def score(cards):
    values = [VALUES.index(card[0]) for card in cards]
    suits = [SUITS.index(card[1]) for card in cards]
    freq = [values.count(i) for i in range(len(VALUES))]
    if len(set(suits)) == 1:
        if sorted(values)[-1] - sorted(values)[0] == 4:
            return 30000 + max(values)
        else:
            return 11000 + max(values)
    elif len(set(sorted(values))) == 5 and (sorted(values)[-1] - sorted(values)[0] == 4 or (sorted(values)[-1] == 12 and sorted(values)[-2] == 3)):
        return 10000 + max(values)
    elif max(freq) == 4:
        return 27000 + 100 * freq.index(max(freq))
    elif max(freq) == 3:
        pairs = [i for i, x in enumerate(freq) if x == 2]
        if pairs == 1:
            return 12000 + 1000 * freq.index(max(freq)) + 100 * pairs[0]
        else:
            return 4000 + 100 * freq.index(max(freq))
    elif max(freq) == 2:
        pairs = [i for i, x in enumerate(freq) if x == 2]

        if len(pairs) == 2:
            return 1300 + 100 * pairs[0] + 100 * pairs[1] + max([x for x in values if x not in pairs])
        else:
            return 100 * pairs[0] + max([x for x in values if x not in pairs])
    else:
        return max(values)

def compute():
    timer = time.time()
    ans = 0
    f = open('54.txt')
    ans = sum(1 for line in f if p1_wins(line.split(' ')[:5], line.split(' ')[5:]))
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans