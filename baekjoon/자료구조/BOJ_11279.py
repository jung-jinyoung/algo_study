import sys
from heapq import heappush, heappop
input = sys.stdin.readline
h = []
N = int(input())
for _ in range(N):
    test = int(input())
    # 0 일 경우 최댓값 출력
    if (test == 0) :
        if (len(h) > 0):
            print(heappop(h)[1])
        else: 
            print(0)
        continue
        
    heappush(h, (-test, test))