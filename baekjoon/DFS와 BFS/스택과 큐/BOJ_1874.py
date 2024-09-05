import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())


# 완성해야 하는 수열 
my_nums = [int(input()) for _ in range(n)]

# 저장할 스택 초기화 
stack = []

result = []


idx = 0
for num in range(1, n+1):
    stack.append(num)
    result.append("+")

    
    

    
