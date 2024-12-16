#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
       
    s = list(s)
    
    change = True
    
    while change:
        l = len(s)
        if l <= 1:
            break
        for i in range(0,l-1):
            if s[i] == s[i+1]:
                s[i] = s[i+1] =''
        s = list(''.join(s))
        
        if len(s) == l:
            change = False        
                
    return "Empty String" if len(s) == 0 else ''.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

