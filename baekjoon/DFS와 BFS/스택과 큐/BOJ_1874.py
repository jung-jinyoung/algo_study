import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())


# 완성해야 하는 수열 
my_nums = [int(input()) for _ in range(n)]

# 저장할 스택 초기화 
stack = []

idx = 0 
result = []
for num in range(1,n+2):
    while stack and stack[-1] == my_nums[idx]:
        stack.pop()
        result.append("-")
        idx +=1
    if num <= n:
        stack.append(num)
        result.append("+")


if stack :
    print("NO")
else:
    print(*result, sep="\n")

    
    

    
