import sys
from collections import deque

sys.stdin = open("input.txt","r")
input = sys.stdin.readline


f, s, g, u, d= map(int, input().split(" "))

my_queue = deque([(s, 0)])
visited = set()
visited.add(s)
answer = "use the stairs"

while my_queue:
    now, cnt = my_queue.popleft()
    
    if now == g : 
        answer = cnt
        break

    up = now + u
    down = now - d

    if up <= f and up not in visited:
        my_queue.append((up, cnt+1))
        visited.add(up)

    if down >= 1 and down not in visited:
        my_queue.append((down, cnt+1))
        visited.add(down)
        
print(answer)