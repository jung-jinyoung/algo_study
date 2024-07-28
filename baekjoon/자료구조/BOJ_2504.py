from collections import deque

my_strings = deque(input())

# 스택을 이용해 괄호열의 값을 계산
stack = []
result = 0
temp_value = 1

is_not_correct = False

prev_char = ""

while my_strings:
    my_char = my_strings.popleft()

    if my_char == "(":
        stack.append(my_char)
        temp_value *= 2
    elif my_char == "[":
        stack.append(my_char)
        temp_value *= 3
    elif my_char == ")":
        if not stack or stack[-1] != "(":
            is_not_correct = True
            break
        if prev_char == "(":
            result += temp_value
        stack.pop()
        temp_value //= 2
    elif my_char == "]":
        if not stack or stack[-1] != "[":
            is_not_correct = True
            break
        if prev_char == "[":
            result += temp_value
        stack.pop()
        temp_value //= 3

    prev_char = my_char

# 모든 괄호가 짝을 이루었는지 확인
if stack:
    is_not_correct = True

if is_not_correct:
    print(0)
else:
    print(result)
