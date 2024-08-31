import sys
from itertools import permutations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

A, B = input().strip().split()
# A의 숫자들로 새로운 숫자 C를 만든다.
# 가능한 C 들 중 B 보다 작으면서 가장 큰 값
# 단 C는, 0으로 시작할 수 없다.

N, M = len(A), len(B)
A = list(map(int,A))
B = int(B)
result = -1

for comb in permutations(A):
    if comb[0] == 0:
        continue
    temp = sum([comb[i] * (10 ** (N-1-i)) for i in range(N)]) 
    if  temp < B :
        result = max(result, temp)

print(result)