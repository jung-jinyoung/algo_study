import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

left = 0
right = n-1
answer = 0

while (left < right):
    now = arr[left] + arr[right]
    if (now > x) :
        right -=1
    elif now == x :
        answer +=1
        left +=1
    else : 
        left +=1
print(answer)