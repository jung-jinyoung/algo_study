def solution(triangle):
    n = len(triangle)
    dp = [ [0] * (i+1) for i in range(n)]
    dp[0] =triangle[0]
    for i in range(1, n):
        for j in range(len(dp[i])):
            left, right = 0, 0
            if (0 <= j-1):
                left = dp[i-1][j-1]
            if (j < len(dp[i-1])):
                right = dp[i-1][j]
            dp[i][j] = max(left, right) + triangle[i][j]
            
    return (max(dp[-1]))