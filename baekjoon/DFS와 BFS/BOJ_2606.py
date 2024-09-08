import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
M = int(input())

related = [[] for _ in range(N+1)]
visited =  [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    related[a].append(b)
    related[b].append(a)

realted = [] + related

def bfs() :
    # 현재 위치 idx 에서 확인
    global  ans

    visited[1] = True
    que = deque(related[1])

    while que :
        computer = que.popleft()

        visited[computer] = True
        ans+=1
        for next_computer in related[computer]:
            if not visited[next_computer]  and next_computer not in que:
                que.append(next_computer)



ans = 0
bfs()

print(ans)
