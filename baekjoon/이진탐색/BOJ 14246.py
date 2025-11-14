import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(" ")))
k = int(input())

left = 0
current_sum = 0
cnt = 0

for right in range(n):
    current_sum += arr[right]
    while current_sum > k :
        cnt += n-right
        current_sum -= arr[left]
        left +=1 

print(cnt)
        