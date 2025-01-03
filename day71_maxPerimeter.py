#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def triangulate(x):
    
    a,b,c = x
    if a + b > c:
        if a + c > b:
            if b + c > a:
                return True
    
    return False

def maximumPerimeterTriangle(sticks):
    # Write your code here
    
    sides = list(combinations(sticks, 3))
    sides = sorted(sides, key=sum, reverse=True)
    sides = list(filter(triangulate, sides))
    
    if not sides:
        return [-1]
        
    valid = list({x for x in sides if sum(x) == sum(sides[0])})
    
    if len(valid) == 1:
        return sorted(valid[0])
        
    valid = sorted(valid, key=max, reverse=True)
    valid =list(filter(lambda x: max(x) == max(valid[0]), valid))
    
    if len(valid) == 1:
        return sorted(valid[0])
        
    valid = sorted(valid, key=min, reverse=True)
    valid = list(filter(lambda x: min(x) == min(valid[0]), valid))
    
    return sorted(valid[0])
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

