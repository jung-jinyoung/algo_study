import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# reverse 를 위한 리스트화
S = input().strip()
T = list(input().strip())
# S -> T 로 바꿈

## 1. A 추가
## 2. B 추가 후 모든 문자열 뒤집기


def pop(arr):
    arr.pop()
    return T

def reverse(arr):
    arr.reverse()
    arr.pop()
    return arr


def check(S,T):
    global result

    if result or len(S) > len(T):
        return

    if len(S) == len(T):
        temp = "".join(T)
        if temp == S :
            result = True
        return

    if T[-1] == "B":
        check(S,reverse(T))
    elif T[-1] == "A":
        print(T)
        if T[0] == "B":
            print("check B")
            check(S,reverse(T))

        check(S,pop(T))

result = False
check(S,T)

if result :
    print(1)
else:
    print(0)


