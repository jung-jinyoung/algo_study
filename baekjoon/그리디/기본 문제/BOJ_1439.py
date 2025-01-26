import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

S = input().strip()
N = len(S)
answer = 0 

now = S[0]
idx = 1
flag = False
while idx < N : 
    check = S[idx]
    if now != check : 
        if flag == False : 
            answer +=1
            flag = True
        else : 
            flag = False
    now = check
    idx +=1

print(answer)