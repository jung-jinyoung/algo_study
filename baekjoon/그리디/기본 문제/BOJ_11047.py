import sys

# sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N, K = map(int, input().split()) 
# 동전 N개, 원하는 값 K

coins = [int(input()) for _ in range(N)]

count = 0 

for i in range(N-1,-1,-1):
    
    # K 값보다 크다면 넘어가기 
    if coins[i] > K:
        continue

    c = K // coins[i]

    K -= coins[i] * c
    count += c
    
    if K == 0 :
        break
print(count)




