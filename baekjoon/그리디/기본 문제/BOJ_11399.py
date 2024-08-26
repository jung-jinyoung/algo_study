import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
# 사람의 수 
info = list(map(int,input().split()))
info.sort(reverse=  True) # 시간 오름차순 

sum = 0

for i in range(N):
    sum += info[i] * (i+1)

print(sum)
