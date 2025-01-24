#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    # Write your code here
    
    count = 0
    x = b.find('010')
    
    while x != -1:
       b = b[x: x+2] + '1' + b[x+3:]
       count +=1
       x = b.find('010')
    
    return count
        
        
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()

