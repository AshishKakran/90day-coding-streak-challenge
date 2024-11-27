#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    k = []
    
    for i in range(p, q + 1):
        d = len(str(i))
        square = str(i**2)
        s = [ square[-d:], square[:-d]]
        if '' in s:
            s.remove('')
        s = list(map(int, s))
        if sum(s) == i:
            k.append(i)
    
    if len(k):
        for i in k:
            print(i, end=" ")
    else:
        print("INVALID RANGE")
        

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)

