import sys

sys.stdin = open("input.txt","r")

input = sys.stdin.readline

n = int(input())
# R, G ,B 순서대로
houses_info = [list(map(int,input().split(" "))) for _ in range(n)]

dp = [[0,0,0] for _ in range(n)]
dp[0] = houses_info[0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + houses_info[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + houses_info[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + houses_info[i][2]
print(min(dp[n-1]))