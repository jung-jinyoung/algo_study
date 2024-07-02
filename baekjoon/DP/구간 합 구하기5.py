import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] + list(map(int, input().split())) for _ in range(N)]
arr = [0] + arr
my_sum = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        my_sum[i][j] = my_sum[i-1][j] + my_sum[i][j-1] - my_sum[i-1][j-1] + arr[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = my_sum[x2][y2] - my_sum[x1-1][y2] - my_sum[x2][y1-1] + my_sum[x1-1][y1-1]
    print(ans)
