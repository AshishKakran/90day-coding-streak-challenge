#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def insertionSort2(n, arr):
    # Write your code here
    
    for i in range(n-1):
        x = arr[i+1]
        j = i
        while x < arr[j] and j >=0:
            arr[j+1] = arr[j]
            j = j - 1
        
        arr[j+1] = x
        print(*arr)
        
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

