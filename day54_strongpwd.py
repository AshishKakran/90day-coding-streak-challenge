#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    
    count = 0
    numbers = re.compile(r'[0-9]')
    lower = re.compile(r'[a-z]')
    upper = re.compile(r'[A-Z]')
    special = re.compile(r'[!@#$%^&*()\-+]')
    
    if not numbers.search(password):
        count += 1

    if not lower.search(password):
        count += 1

    if not upper.search(password):
        count += 1

    if not special.search(password):
        count += 1
    return max(count, 6-n)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

