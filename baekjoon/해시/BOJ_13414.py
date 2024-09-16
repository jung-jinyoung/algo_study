import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

K, L = map(int, input().split())

info = {}

for num in range(1, L+1):
    student = input().strip()
    info[student] = num

cnt = 0
for key in sorted(info, key = info.__getitem__):
    if cnt == K :
        break
    print(key)
    cnt +=1