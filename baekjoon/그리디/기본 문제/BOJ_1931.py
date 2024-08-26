import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input().strip())
# 총 회의의 수 

info = []
for _ in range(N):
    s, e = map(int, input().strip().split())
    info.append([s,e])

info.sort(key=lambda x: (x[1],x[0])) # 빨리 끝나는 회의 순서대로 정렬

count = 1
now_end = info[0][1]

for i in range(1,N):
    start, end = info[i]
    if now_end <= start:
        count +=1
        now_end = end

print(count)
