import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0]
sum_total = 0
for i in range(N):
    sum_total += arr[i]
    dp.append(sum_total)

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])