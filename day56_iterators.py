# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

n = int(input())

x = input().split()
k = int(input())

indices = [i for i in range(n) if x[i] == 'a']

total = list(combinations(range(n), k))

count = 0
for x in total:
    for y in indices:
        if y in x:
            count += 1
            break

print(count/len(total))



