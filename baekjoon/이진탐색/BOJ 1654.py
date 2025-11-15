import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

k, n = map(int, input().split(" "))
items = [int(input()) for _ in range(k)]

ans = 0
left, right = 1, max(items)

def cutting(m):
    total = 0
    for l in items : 
        total += l // m
    return total >= n

while left <= right : 
    mid = (left+right) // 2
    if cutting(mid):
        ans = mid
        left = mid+1
    else : 
        right = mid-1

print(ans)
        
    
    
    