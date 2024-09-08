import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().strip().split())
grid = [input().strip() for _ in range(N)]

N, M = N-1, M-1

# (0,0) => (N,M) 이동 했을 때 최단 경로
visited = [[0] * (M+1) for _ in range(N+1)]


def bfs():

    que = deque()
    que.append((0,0))

    visited[0][0] =1
    while que :
        x, y = que.popleft()
        if (x, y) == (N, M) :
            print(visited[x][y])
            return
        for dx, dy in [(1,0), (0,1),(-1,0),(0,-1)] :

            nx = x + dx
            ny = y + dy

            if 0<=nx<N+1 and 0<=ny<M+1:
                if not visited[nx][ny] and grid[nx][ny] == "1":
                    que.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1


bfs()