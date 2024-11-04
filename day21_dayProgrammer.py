#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def depends(year):
    
    if year < 1918:
        return 29 if year % 4 == 0 else 28
    elif year == 1918:
        return 16 if year % 400 == 0 else 15
    else:
        return 29 if  (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else 28

def dayOfProgrammer(year, day = 256):
    # Write your code here
    
    months = [31, depends(year),31,30,
                31,30,31,31,
                30,31,30,31]
                
                
    count = 0
    
    for curr in range(len(months)):
        
        count = months[curr]
            
        if day < count:
            break
        else:
            day = day - count
            
            
    return "{:02}.{:02}.{}".format(day,curr + 1, year)        
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

