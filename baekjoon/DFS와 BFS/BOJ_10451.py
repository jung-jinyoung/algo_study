import sys
from collections import deque

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

T = int(input())

def bfs(node):
    my_queue = deque([node])

    while my_queue :
        node = my_queue.popleft()
        next_node = info[node]
        if visited[next_node] == -1 :
            my_queue.append(next_node)
            visited[next_node] = 1


for _ in range(T):
    N = int(input())
    info = [0] + list(map(int, input().strip().split(" ")))
    cnt = 0
    visited = [-1] * (N+1)
    for node in range(1, N+1):
        if visited[node] == -1 :
            cnt += 1
            bfs(node)

    print(cnt)    



    