#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    
    i = 0
    e = 100
    while True:
        jump = (i + k) % len(c)
        e = e - 1
        if c[jump] == 1:
            e = e - 2
        i = jump
        #print(i, " ", e)
        if i == 0:
            break
    return e
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

