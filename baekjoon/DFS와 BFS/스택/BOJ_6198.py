import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
towers = [int(input()) for _ in range(N)]

stack = []
result = [0] * N
for idx in range(N):

    while stack and towers[stack[-1]] <= towers[idx] :
        stack.pop()

    if stack :
        result[idx] = len(stack)

    stack.append(idx)

print(sum(result))