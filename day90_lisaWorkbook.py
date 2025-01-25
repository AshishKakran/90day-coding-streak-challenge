#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
  
    ch = []
    
    # step 1: create chapters
    for i in arr:
        c = list(range(1,i+1))
        for j in range(1,i//k+1):
            ch.append(c[:k])
            c = c[k:] # this might add some empty chapters
        ch.append(c)
        
    ch = list(filter(lambda i: len(i) != 0, ch)) # remove empty chapters

    #step 2: find special problems
    count = 0
    for i,j in enumerate(ch):
        if i + 1 in j:
            count +=1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

