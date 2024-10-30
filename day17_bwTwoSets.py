#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def condition1(i,arr):
    
    for j in arr:
        if i % j != 0:
            return False
    else:
        return True
        
def condition2(i, arr):
    
    for j in arr:
        if j % i != 0:
            return False
    else:
        return True


def getTotalX(a, b):
    # Write your code here
    
    s_int = 0
    for i in range(max(a),min(b) + 1):
        if condition1(i,a) and condition2(i,b):
            s_int += 1
        
    return s_int
            
    
    
  
    
    return s_int

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

