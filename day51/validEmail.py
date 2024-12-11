# Enter your code here. Read input from STDIN. Print output to STDOUT

import re 
import email.utils as email 

n = int(input())

r = re.compile(r'^[a-z](\w|-|\.)*@[a-z]+\.[a-z]{1,3}$')

for i in range(n):
    name,mail = email.parseaddr(input())
    
    if r.match(mail):
        print(email.formataddr((name,mail)))

