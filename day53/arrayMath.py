import numpy as np


n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    a += list(map(int, input().split()))
    
for i in range(n):
    b += list(map(int, input().split()))
    
a = np.array(a).reshape(n,m)
b = np.array(b).reshape(n,m)

print(a+b)
print(a-b)
print(a*b)
print(np.floor_divide(a,b))
print(a%b)
print(a**b)
    
