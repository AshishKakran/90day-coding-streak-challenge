#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

def beautifulPairs(A, B):
    # Write your code here
    
    freq_A = Counter(A) # build a frequency dictionary
    
    paired = 0
    for i in B:
        if freq_A[i] > 0:
            paired += 1
            freq_A[i] -= 1
            
    common = freq_A.most_common(1)[0] #returns a tuple (number, frequency)
    
    if common[1] > 0:   #at least one unmatched item in A
        return paired + 1
    else:               # A and B are similar
        return paired - 1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()

