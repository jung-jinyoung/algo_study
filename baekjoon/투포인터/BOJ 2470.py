import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(" ")))

arr.sort()

left = 0
right = n-1

res = float('inf')
ans_left = 0
ans_right = n-1

while left < right and left < n and right >= 0: 
    sum = arr[left]+arr[right]

    if abs(sum) < abs(res) :
        res = sum
        ans_left, ans_right = left, right
    
    # 이동
    if sum > 0 :
        right -= 1
    elif sum < 0 :
        left += 1
    else :
        break

print(arr[ans_left], arr[ans_right])