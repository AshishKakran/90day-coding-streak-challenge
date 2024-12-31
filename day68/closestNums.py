#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    
    arr = sorted(arr)
    diffs = {}
    
    min_diff = max(arr)
    for i in range(len(arr) - 1):
        diff = abs(arr[i+1] - arr[i])
        if diff < min_diff:
            min_diff = diff
        if diff not in diffs:
            diffs[diff] = [arr[i], arr[i+1]]
        else:
            diffs[diff] += [arr[i], arr[i+1]]
        
    return diffs[min_diff]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

