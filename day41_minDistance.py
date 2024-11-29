#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    
    x = set(a)
    duplicates = [ (i, a.count(i)) for i in x if a.count(i) > 1]
    
    if len(duplicates) == 0:
        return -1
        
    d = []
    
    tracker = 10**6
    
    for i,j in duplicates:
        
        idx = a.index(i)
        while j > 1:
            j = j - 1
            distance = a[idx+1:].index(i) +1
            idx = idx + distance
            tracker = min(tracker,distance)
        
    return tracker
    
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

