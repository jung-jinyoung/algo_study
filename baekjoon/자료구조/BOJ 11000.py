import sys
from heapq import heappush, heappop
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(n)]

# 시작 시간 순서로 정렬
arr.sort()
# 최소힙 (끝나는 시간)
pq = []
heappush(pq, arr[0][1])

for i in range(1,n):
    s, e = arr[i]
    
    # 가장 빨리 끝나는 강의실 확인
    if s >=  pq[0] :
        # 기존 강의실 재사용
        heappop(pq)
    # 강의실 정보 추가
    heappush(pq, e)
    
print(len(pq))

