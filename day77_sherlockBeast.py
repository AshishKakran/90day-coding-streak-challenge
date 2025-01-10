#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # Write your code here
    
    t = n - n % 3
    found = False
    
    while t >= 0 and not found:
        if (n - t) % 5 == 0:
            found = True
        else:
            t = t - 3

    print("5" * t + "3" * (n-t)) if found else print(-1)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)

