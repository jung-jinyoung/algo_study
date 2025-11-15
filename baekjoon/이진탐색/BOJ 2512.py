import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(" ")))
m = int(input())
ans = 0

# 예산안 사용 가능 확인
def is_possible(c) :
    total = 0
    for x in arr : 
        total += min(x, c)
    return total <= m

left, right = 0, max(arr)

while left<=right : 
    mid = (left+right) // 2
    if is_possible(mid):
        ans = mid 
        left = mid+1
    else : 
        right = mid-1

print(ans)