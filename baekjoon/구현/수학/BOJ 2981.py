import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

def find_gcd(a, b):
    while b : 
        a, b = b, a % b
    return a

gcd = arr[1] - arr[0]

for i in range(2, n):
    gcd = find_gcd(gcd, arr[i] - arr[i-1])

answer = set()
answer.add(gcd)
for j in range(2, int(gcd ** 0.5) + 1):
    if gcd % j == 0:
        answer.add(j)
        answer.add(gcd // j)
answer = list(answer)
answer.sort()

print(*answer)