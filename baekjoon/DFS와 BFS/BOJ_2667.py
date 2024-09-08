import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
# N*N
my_map = [input().strip() for _ in range(N)]


checked = [ [0] * N for _ in range(N)]
ans = 0
total = []

def bfs(i, j):

    que = deque()
    que.append((i,j))
    checked[i][j] = 1

    count = 1
    while que:
        i, j = que.popleft()
        for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            ni = i + di
            nj = j + dj

            if (0<=ni<N and 0<=nj<N) :
                if my_map[ni][nj] == "1" and not checked[ni][nj]:
                    que.append((ni,nj))
                    checked[ni][nj] =1
                    count +=1

    total.append(count)
    return






for i in range(N):
    for j in range(N):
        if checked[i][j]:
            continue
        if my_map[i][j] == "1":
            bfs(i,j)
            ans+=1

total.sort()
print(ans)
print(*total, sep= '\n')