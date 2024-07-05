import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 이동 
dx = [1, 0, 1]
dy = [0, 1, 1]

dp = [ [ 0 for _ in range()] for _ in range(N)]
dp[0][0] = arr[0][0]

for j in range(1, M):
    dp[0][j] = dp[0][j-1] + arr[0][j]

for i in range(1, N):
    for j in range(M):
        print(max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]))
        dp[i][j] = max (dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + arr[i][j]
print(*dp, sep='\n')