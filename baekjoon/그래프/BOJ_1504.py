import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline
# 정점의 개수 n 와 간선의 개수 e
n, e = map(int, input().split())
nodes = defaultdict(dict)
for _ in range(e) :
    a, b, c = map(int, input().split())
    nodes[a][b] = c
    nodes[b][a] = c

# 반드시 지나야할 정점
v1, v2 = map(int, input().split())

def dikstra(start):
    distance = [float("inf") for _ in range(n+1)]
    distance[start] = 0
    h = []
    heappush(h, (0, start))
    
    while h :
        dist, pos = heappop(h)
        if (dist > distance[pos]):
            continue
        for next_pos in nodes[pos].keys():
            cost = dist + nodes[pos][next_pos] 
            if cost < distance[next_pos]:
                heappush(h, (cost, next_pos))
    return distance
    
start_dist = dikstra(1)
start_v1 = dikstra(v1)
start_v2 = dikstra(v2)

# 1 -> v1 -> v2 -> n
path1 = start_dist[v1] + start_v1[v2] + start_v2[n]
# 1 -> v2 -> v1 -> n
path2 = start_dist[v2] + start_v2[v1] + start_v1[n]

result = min(path1, path2)
if result < float('inf'):
    print(result)
else :
    print(-1)