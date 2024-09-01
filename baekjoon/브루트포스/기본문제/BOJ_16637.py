import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [*map(lambda x : int(x) if x.isdigit() else x, input())]
# 연산자 위치는 홀수

def calc(a,op,b):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    return

def dfs(now, end, total):
    global max_result
    
    if now >= end:
        max_result = max(max_result, total)
        return 

    if now + 3 < N:
        # 괄호로 묶을 수 있는 경우
        dfs(now+4,end,calc(total,arr[now], calc(arr[now+1],arr[now+2],arr[now+3]))) 
    # 괄호로 묶지 않을 경우
    dfs(now+2,end,calc(total,arr[now],arr[now+1]))


max_result = float('-inf')

if N == 1:
    print(arr[0])
else: 
    # 첫번째를 괄호로 묶었을 경우
    dfs(1,N,arr[0])
    print(max_result)