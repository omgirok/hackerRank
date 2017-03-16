#!/bin/python

import sys

"""
# n is length of unencrypted string (no idea why this is relevant)
n = int(raw_input().strip())
# s is the string itself
s = raw_input().strip()
# k is the number of rotations in the encryption
k = int(raw_input().strip())
"""

def caesarCipher(s, k):
    result = ""
    # range of uppercase letters: 65 to 90
    # lowercase range: 97 to 122
    k = k % 26
    for x in s:
        # check if uppercase or lowercase
        if ord(x) in range(65,91):
            # uppercase letter
            newOrd = ord(x)+k
            # check the new ASCII value
            if newOrd not in range(65,91):
                leftOver = k - (91 - ord(x))
                newX = chr(65+leftOver)
            else:
                newX = chr(newOrd)
        elif ord(x) in range(97,123):
            # lowercase letter
            newOrd = ord(x)+k
            if newOrd not in range(97,123):
                leftOver = k - (123 - ord(x))
                newX = chr(97+leftOver)
            else:
                newX = chr(newOrd)
        else:
            newX = x
        result+=newX
        
    return result