#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    
    t = []
    
    for i in s:
        if i.isalpha():
            if i.isupper():
                t.append(chr(65 + (ord(i) + k - 65) %26))
            else:
                t.append(chr(97 + (ord(i) + k - 97) %26))
        else:
            t.append(i)
            
    return ''.join(t)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

