#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 59: XOR Decryption

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

"""
import time
def decrypt(ciphertext, key):
    return [(c ^ key[i % len(key)]) for (i, c) in enumerate(ciphertext)]


# Use a scoring system to calculate the best trio of characters
def get_score(decryption):
    result = 0
    for c in decryption:
        if 97 <= c <= 122:  # Lowercase A-Z
            result += 2
        if 65 <= c <= 90:  # Uppercase a-z
            result += 1
        elif c < 0x20:  # ASCII control characters
            result -= 10
    return result


def compute():
    timer = time.time()
    file = open('59.txt')
    numbers = []
    for line in file:
        numbers.append([int(number) for number in line.split(',')])
    numbers = numbers[0]
    best_score = 0
    key = [0,0,0]
    for x in range(97, 123):
        for y in range(97, 123):
            for z in range(97, 123):
                score = get_score(decrypt(numbers, [x,y,z])) 
                if score > best_score:
                    best_score = score
                    key = [x,y,z]
    ans = sum(decrypt(numbers, key))
    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans