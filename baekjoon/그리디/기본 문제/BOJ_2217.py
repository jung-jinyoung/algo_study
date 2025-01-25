import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())

# 각 줄이 견딜 수 있는 무게 입력 후 정렬
ropes = [int(input()) for _ in range(N)]
ropes.sort()

# 정답 초기화
answer = 0 
for idx in range(N):
    now = ropes[idx] * ( N - idx)
    answer = max(answer, now)

print(answer)
