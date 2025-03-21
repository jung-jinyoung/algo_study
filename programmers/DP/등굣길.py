def solution(m, n, puddles):
    mod = 1000000007
    dp = [[0] * m for _ in range(n)]
    # 시작점
    dp[0][0] =1
    for i in range(n):
        for j in range(m):
            if ([j+1, i+1] in puddles):
                # m,n 으로 표시되기 때문에 초기화
                continue
            if i > 0 :
                dp[i][j] += dp[i-1][j]
            if j > 0 :
                dp[i][j] += dp[i][j-1]
            dp[i][j] %= mod
    return (dp[n-1][m-1])