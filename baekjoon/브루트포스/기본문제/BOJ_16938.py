import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, L, R, X = map(int, input().strip().split())
# 문제 N 개 중 두 문제 이상 
# 문제 난이도의 합은 L 이상 R 이하
# 가장 높은 난이도와 낮은 난이도의 차이는 X 이상

tests = list(map(int, input().strip().split()))
cnt = 0
for i in range(N,1,-1):
    for comb in combinations(tests,i):
        arr = [*comb]
        if L <= sum(arr) <= R :
            if max(arr) - min(arr) >= X :
                cnt +=1

print(cnt) 