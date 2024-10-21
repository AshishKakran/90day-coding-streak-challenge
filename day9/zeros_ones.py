import numpy as np

l = list(map(int, input().split()))

print(np.zeros(tuple(x for x in l), dtype=np.int32))
print(np.ones(tuple(x for x in l), dtype=np.int32))

