import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N , M = map(int, input().split())

A = [list(input().strip()) for _ in range(N)]
B = [list(input().strip()) for _ in range(N)]


def convert_matrix(arr,i,j):
    for row in range(i,i+3):
        for col in range(j, j+3):
            if arr[row][col] == "0":
                arr[row][col] = "1"
            else:
                arr[row][col] = "0"

# 3x3 행렬 이하일 경우
if N <3 or M <3 :
    if A == B: # A와 B가 동일하다면 
        print(0)
    else: # 동일하지 않다면 뒤집을 수 없다.
        print(-1)

# 3x3 행렬 이상일 경우 
else: 
    count = 0
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                convert_matrix(A,i,j)
                count+=1

    if A == B :
        print(count)
    else:
        print(-1)

