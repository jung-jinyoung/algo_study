import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
current_sum = 0 

end = 0
for start in range(n):
    while end < n and current_sum < m:
        current_sum +=arr[end]
        end +=1
    if (current_sum == m) :
        answer +=1
    current_sum -= arr[start]
print(answer)