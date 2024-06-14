"""
테스트 케이스
24 번에서 시간 초과 발생

=> 분석 : 모든 DP 값 저장 후 마지막에 dp[n] % 10007
        : 숫자가 클 수록 연산 시간이 오래 걸리기 때문에 시간 초과 발생

=> 해결 : dp 저장하기 전 10007 나눔눔
"""


def solution(n, tops):
    mod = 10007
    dp = [[0, 0] for _ in range(n + 1)]

    dp[1][0] = 1
    if tops[0] == 0:
        dp[1][1] = 2
    else:
        dp[1][1] = 3

    # 인덱스를 위한 더미 생성
    tops = [0] + tops
    for idx in range(2, n + 1):

        # 오른쪽 모서리 마름모 채울 경우의 수
        dp[idx][0] = sum(dp[idx - 1]) % mod  # 모든 경우의 수 더하기

        # 채우지 않을 경우의 수
        if tops[idx] == 0:
            dp[idx][1] = (dp[idx - 1][0] + 2 * dp[idx - 1][1]) % mod
        elif tops[idx] == 1:
            dp[idx][1] = (2 * dp[idx - 1][0] + 3 * dp[idx - 1][1]) % mod

    answer = sum(dp[n]) % 10007
    return answer