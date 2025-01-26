import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
games = [ int(input()) for _ in range(N)]

answer = 0 

idx = N - 1
next = games[idx]
while idx > 0 :
    before = games[idx - 1]

    if before >=next : 
        request = next - 1
        answer += before - request 
        next = request
    else :
        next = before
    
    idx -= 1
print(answer)