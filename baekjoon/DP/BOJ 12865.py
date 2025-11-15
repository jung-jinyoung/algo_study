import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n, k = map(int, input().split(" "))
items = [list(map(int, input().split(" "))) for _ in range(n)]

# 물건까지 고려했을 때 무게 w에서 얻을 수 있는 최대 가치
dp = [0] * (k+1)

for weight, value in items : 
    for w in range(k,weight-1,-1):
        dp[w] = max(dp[w], dp[w-weight] + value)

print(dp[k])