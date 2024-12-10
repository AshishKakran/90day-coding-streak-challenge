# Enter your code here. Read input from STDIN. Print output to STDOUT

import re 


def and_or(m):
    sym  = m.group(0)
    
    if sym == '&&':
        return "and"
    elif sym == '||':
        return "or"
        
r = re.compile(r'(?<=\s)&&(?=\s)|(?<=\s)\|\|(?=\s)')

n = int(input())

for i in range(n):
    txt = input()
    print(r.sub(and_or, txt))

