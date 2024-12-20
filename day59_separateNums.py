#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def generateSplit(s, c):
    
    exp = r'\d' * c
    r = re.compile('(' + ''.join(exp) + ')')
    
    split = list(filter(None, r.split(s))) #split the string and remove ''
    
    if c > 1 and any(map(lambda x: x[0] == '0', split)):
        return None #discard if any item in split begins with 0
        
    split = list(map(int, split))
    
    return split
    
def separateNumbers(s):
    # Write your code here
    
    
    for i in range(1, len(s)//2 + 1):
  
        t = generateSplit(s, i)
        
        if t and all(map(lambda x: (t[x] - t[x-1]) == 1, range(1,len(t)))):
            print("YES", t[0])
            break
        
        e = '9' * i
        if e in s:
            x = s.find(e + str(int(e) + 1)) + i # find 9(10), 99(100) to split
            part1 = generateSplit(s[:x], i) 
            part2 = generateSplit(s[x:], i + 1) 


            if part1 and part2:
                t = part1 + part2 
                
                if all(map(lambda x: (t[x] - t[x-1]) == 1, range(1,len(t)))):
                    print("YES", t[0])
                    break
    else:
        print("NO")

    

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

