import sys
from heapq import heappush, heappop

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
hq = []

# 가장 작은 수 = 우선순위
for _ in range(n) :
    heappush(hq, int(input()))
    
total = 0 

while len(hq) > 1 :
    a = heappop(hq)
    b = heappop(hq)
    cost = a + b
    total += cost 
    heappush(hq, cost)

print(total)