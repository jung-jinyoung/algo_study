import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n, m = map(int, input().split(" "))
my_map = [list(map(int, input().split(" ")) )for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[0][0] = my_map[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0 :
            continue
        if i > 0 :
            dp[i][j] = max(dp[i][j], dp[i-1][j]+my_map[i][j])
        if j > 0 :
            dp[i][j] = max(dp[i][j], dp[i][j-1]+my_map[i][j])
        if i>0 and j>0 :
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+my_map[i][j])

print(dp[n-1][m-1])