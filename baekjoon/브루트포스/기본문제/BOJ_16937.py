import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

H, W = map(int,input().strip().split())
N = int(input().strip())

# H*W 모눈 종이와 스티커 N개
# 스티커 2개를 붙일 때 최대 면적의 값을 구하시오.

arr = []
for _ in range(N):
    R, C = map(int, input().strip().split())
    arr.append([R,C])

def check(r1,c1,r2,c2,H,W):
    if (r1+r2 <= H and max(c1,c2) <= W) or (max(r1,r2)<=H and (c1+c2) <=W):
        return True
    elif (r1+r2 <= W and max(c1,c2) <= H) or (max(r1,r2) <= W and (c1+c2)<=H):
        return True
    
    return False


max_area = 0
for (sticker1, sticker2) in combinations(arr,2):
    
    r1, c1 = sticker1
    r2, c2 = sticker2
    ## 회전시켰을 때의 모든 경우의 수 
    if check(r1,c1,r2,c2,H,W) or check(r1,c1,c2,r2,H,W) or  check(c1,r1,r2,c2,H,W) or check(c1,r1,c2,r2,H,W):

        area = (r1*c1) + (r2*c2)
        max_area = max(area, max_area)

print(max_area)