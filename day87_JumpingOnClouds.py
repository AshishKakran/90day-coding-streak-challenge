#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here

    
    if len(c) == 2:
        return 1
    
    counter = 0
    i = 0
    
    while i + 2 <= len(c) - 1:
        counter += 1
        if c[i + 2 ] == 0:
            i += 2
        else:
            i += 1
    
    if i == len(c) - 2:
        return counter + 1
    else:
        return counter
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

