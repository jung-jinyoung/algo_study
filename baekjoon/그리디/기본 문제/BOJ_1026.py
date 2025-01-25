import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

list_A.sort()
list_B.sort(reverse=True)

answer = 0 

for idx in range(N):
    answer += list_A[idx] * list_B[idx]

print(answer)