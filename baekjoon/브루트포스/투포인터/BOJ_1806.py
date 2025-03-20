import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
total = 0
end = 0
answer = int(1e9)
for start in range(n):
    while end < n and total < m :
        total += arr[end]
        end +=1
    if total >= m:
        answer = min(answer, end-start)
    total -= arr[start]

if (answer != int(1e9)) :
    print(answer)
else: 
    print(0)