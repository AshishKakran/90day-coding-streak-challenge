#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    # Write your code here
        
    n = len(arr) 
    D =  { v:k for k,v in enumerate(arr) } # dict lookup >>> arr.index()
    
    c = 0
    for i in range(n): 
        if arr[i]!=n-i:  # In sorted array, n-i should be at index i
            D[arr[i]] = D[n-i] # if not then update indexes
            arr[i],arr[D[n-i]]=n-i,arr[i] # do swap
            c = c + 1

        if c == k: #break if runs out of swaps
            break
    return arr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

