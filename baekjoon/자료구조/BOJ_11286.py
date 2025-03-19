import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N = int(input())
h = []

for _ in range(N):
    test = int(input());
    if (test == 0):
        if (len(h) > 0) :
            print(heappop(h)[1])
        else :
            print(0)
        continue
        
    heappush(h, (abs(test), test))
    