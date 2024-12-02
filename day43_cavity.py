#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    
    if n < 3:
        return grid
    
    
    for idx, row in enumerate(grid[1:-1]):
        for jdx, i in enumerate(row[1:-1]):
            if all([grid[idx][jdx+1]<i, grid[idx+2][jdx+1]<i, row[jdx] < i , row[jdx+2] < i]):
                grid[idx+1] = grid[idx+1][:jdx+1] + 'X' + grid[idx+1][jdx+2:]
    return grid
    
    
            
        
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

