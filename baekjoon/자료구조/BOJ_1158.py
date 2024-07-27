from collections import deque

N, M = map(int, input().split())

my_nums = deque(range(1, N + 1))
result= "<"
while my_nums:
    my_nums.rotate(-(M-1)) # M-1번 만큼 왼쪽으로 회전
    result += f"{my_nums.popleft()}"
    if my_nums:
        result += ", "

result += ">"
print(result)