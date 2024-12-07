#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def ordered(b):
    
    prev = b[0]
    count = 1
    
    for i in b[1:]:
        if i != prev and count <2:
            return False
        elif i != prev:
            prev = i
            count = 1
        else:
            count +=1 
        
    if count == 1:
        return False
    return True
    
    

def happyLadybugs(b):
    # Write your code here
    bugs = b
    bugs = list(bugs.replace('_', ''))
    
            
    if b.count('_') == 0 and ordered(bugs):
        return "YES"
    
    if b.count('_') == 0:
        return "NO"
    
    
    colors = set(bugs)
    for c in colors:
        if bugs.count(c) == 1:
            return "NO"
            
    return "YES"
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

