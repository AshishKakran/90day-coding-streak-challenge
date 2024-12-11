# Enter your code here. Read input from STDIN. Print output to STDOUT


import re 
n = int(input())

r = re.compile(r'(?<!^)(#(?:[\da-fA-F]{3}){1,2})')
for i in range(n):
    for m in r.findall(input()):
        print(m)
