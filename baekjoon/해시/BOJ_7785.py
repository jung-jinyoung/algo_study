import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input()) # 로그 수

table = {}

for _ in range(N):
    name , info = input().strip().split()
    if info == "enter":
        table[name] = True
    elif info == "leave":
        del table[name]

result = list(table.keys())
result.sort(reverse=True)
print(*result, sep= '\n')