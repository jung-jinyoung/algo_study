import sys
sys.stdin = open("input.txt","r")

input = sys.stdin.readline

S = input().rstrip()
q = int(input())
n = len(S)

# 26개 알파벳 prefix 배열
prefix = [[0] * (n+1) for _ in range(26)]

# prefix 계산
for i in range(n):
    char_idx = ord(S[i]) - 97
    for c in range(26):
        prefix[c][i+1] = prefix[c][i]
    prefix[char_idx][i+1] += 1

# 쿼리
for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    idx = ord(a) - 97
    # prefix는 1-based, 문자열은 0-based
    print(prefix[idx][r+1] - prefix[idx][l])
