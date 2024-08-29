import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

request = input().strip()
length = len(request)

result = 1

for i in range(length):
    if request[i] == "c":
        # 이전 문자가 "c" 일 경우 중복 제거 후 25가지 선택
        if i > 0 and request[i-1] == "c":
            result *= 25
        else:
        # 그 외 26 가지 모두 선택 가능
            result *= 26

    else:
        if i > 0 and request[i-1] == "d":
        # 이전 문자가 "d" 일 경우 중복 제거 후 9가지 선택
            result *= 9
        else:
        # 그 외 10가지 모두 선택 가능
            result *= 10

print(result)