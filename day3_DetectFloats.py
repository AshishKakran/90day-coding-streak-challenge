import re

f = re.compile('(\+?|-?)[0-9]*\.[0-9]+$')

t = int(input())

for i in range(t):
    if(f.match(input())):
        print(True)
    else:
        print(False)
