n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

info = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        info[i][j] = arr[i][j]
        info[i][j] += info[i-1][j] + info[i][j-1]
        info[i][j] -= info[i-1][j-1]

