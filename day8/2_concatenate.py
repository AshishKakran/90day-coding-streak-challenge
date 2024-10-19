import numpy

n,m,p = map(int, input().split())

np = [ list(map(int,input().split())) for x in range(n)]
mp = [ list(map(int,input().split())) for x in range(m)]

print(numpy.concatenate((numpy.array(np),numpy.array(mp)), axis = 0))
