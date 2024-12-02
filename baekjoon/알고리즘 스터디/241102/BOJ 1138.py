import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
result = [0] * N

for number in range(1,N+1):
    cnt = arr[number - 1]
    # 앞에서 이동하는 숫자 카운트
    check = 0
    for idx in range(N):
        if result[idx] == 0 :
            if check != cnt :
                check +=1
            else : 
                result[idx] = number
                break


print(*result)