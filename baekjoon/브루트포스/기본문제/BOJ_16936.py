import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().strip().split()))

def dfs(num, cnt, arr, result):
    num2 = num * 2
    num3 = num // 3
    r = num % 3

    if cnt == N:
        print(*result)


    if num2 in arr :
        result.append(num2)
        dfs(num2, cnt+1, arr, result)
        result.pop()

    if r == 0 and num3 in arr:
        result.append(num3)
        dfs(num3, cnt+1, arr, result)
        result.pop()

    return

for num in arr:
    result = [num]
    dfs(num, 1, arr, result)