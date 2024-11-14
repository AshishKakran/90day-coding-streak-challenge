#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    
    chains = []
    
    for i in range(0, len(a)):
        l = [a[i]]
        for j in range(i+1, len(a)):
            s = [] + l
            for k in range(j, len(a)):
                if all(map(lambda x: abs(x - a[k]) <= 1, s)):
                    s.append(a[k])
            #print(s)
            chains.append(len(s))
                
    
    return max(chains)
            
            
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

