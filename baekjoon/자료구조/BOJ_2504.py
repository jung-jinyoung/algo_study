from collections import deque

my_strings = deque(input())

X_list = []
x = 0

Y_list = []
y = 0

result = 0
while my_strings:
    temp = my_strings.popleft()

    if temp == "(" or temp == "[":
        if temp == "(":
            X_list.append(temp)
        else:
            Y_list.append(temp)

    if temp == ")":
        try:
            X_list.pop()

            if not X_list:
                if x or y :
                    result += 2 * (2 * x +3 * y)
                    x = 0
                    y = 0
                else :
                    result *= 2
            else:
                x += 1

        except IndexError:
            result = 0
            break

    elif temp == "]":
        try :
            Y_list.pop()

            if not Y_list:
                if x or y :
                    result += 3 * (2 * x+ 3 * y)
                    x = 0
                    y = 0

                else:
                    result *= 3
            else :
                y += 1

        except IndexError:
            result = 0
            break

print(result)
