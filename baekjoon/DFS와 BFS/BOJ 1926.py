import sys
from collections import deque, defaultdict
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
# 색칠된 종이 번호 : 개수
info = defaultdict(int)
# 종이 번호 초기화
num = 1

checked = [[False] * m for _ in range(n)]
dirs = [[-1,0], [0,1], [1,0], [0,-1]]

def bfs (i,j,num) : 
    q = deque() 
    q.append((i,j))
    while q : 
        x, y = q.popleft()
        for dx, dy in dirs : 
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m and paper[nx][ny] == 1:
                if not checked[nx][ny]:
                    checked[nx][ny] = True
                    info[num] += 1
                    q.append((nx,ny))
    
    return 

for i in range(n):
    for j in range(m):
        # 색칠되었고 확인하지 않았다면 
        if paper[i][j] == 1 and not checked[i][j] : 
            checked[i][j] = True
            info[num] =1 
            bfs(i,j,num)
            num +=1 

if info : 
    print(len(info))
    print(max(info.values()))
else : 
    print(0)
    print(0)
