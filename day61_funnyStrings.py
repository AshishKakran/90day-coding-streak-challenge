#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    
    f = [ord(c) for c in s]
    r = [ord(c) for c in s[::-1]]
    
    f = [ abs(f[x + 1] - f[x]) for x in range(len(f) - 1)]
    r = [ abs(r[x + 1] - r[x]) for x in range(len(r) - 1)]
    
    return "Funny" if f == r else "Not Funny"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()

