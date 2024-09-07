import sys
from collections import deque


sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

arr = deque()
for _ in range(N):
    my_input = input().strip()
    if "push" in my_input:
        arr.append(int(my_input[5:]))
    elif "pop" == my_input:
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif "size" == my_input:
        print(len(arr))
    elif "empty" == my_input:
        if not arr:
            print(1)
        else:
            print(0)
    elif "front" == my_input:
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif "back" == my_input:
        if arr:
            print(arr[-1])
        else:
            print(-1)