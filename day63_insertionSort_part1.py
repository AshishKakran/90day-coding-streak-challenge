#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    
    x = arr[-1]
    i = len(arr) - 2
    
    while x < arr[i] and i >= 0:
        arr[i+1] = arr[i]
        print(*arr)
        i = i - 1
        
    if i != len(arr) - 2:
        arr[i+1] = x
    
    print(*arr)
        
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

