import sys
from collections import deque
sys.stdin =  open("input.txt", "r")
input = sys.stdin.readline


N = int(input())
my_towers = deque([*map(int,input().strip().split())])

stack = []
result = [0] * N

for i in range(N):
    # 현재 탑보다 낮은 탑을 스택에서 제거
    while stack and my_towers[stack[-1]] <= my_towers[i]:
        stack.pop()

    if stack :
        result[i] = stack[-1] + 1
    stack.append(i)

print(*result)