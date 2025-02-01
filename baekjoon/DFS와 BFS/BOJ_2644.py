import sys
from collections import deque

sys.stdin = open("input.txt","r")
input = sys.stdin.readline


n = int(input())
p1, p2 = map(int,input().split(" "))
m = int(input()) 

graph = [[] for _ in range(n+1)]
for _ in range(m):
    parent, child = map(int, input().split(" "))
    graph[parent].append(child)
    graph[child].append(parent)

def bfs(start, target): 
    # 현재 노드와 촌수 카운트 초기화
    queue = deque([[start, 0]])
    visited = set()

    while queue : 
        current, count = queue.popleft()
        if current == target :
            return count

        visited.add(current)
        for neightbor in graph[current]:
            if neightbor not in visited:
                queue.append([neightbor, count+1])
    
    return -1

answer = bfs(p1, p2)
print(answer)