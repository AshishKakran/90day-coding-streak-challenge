#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations, combinations


#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    
    count = 0
    
    if len(arr) < 3:
        return 0
    
    
    good_pairs = []
    
    for j in range(1, len(arr) - 1):
        for i in range(0, j):
            if arr[j] - arr[i] == d:
                good_pairs.append(j)
                
    for j in good_pairs:
        for k in range(j+1, len(arr)):
            if arr[k] - arr[j] == d:
                count += 1
            

            
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

