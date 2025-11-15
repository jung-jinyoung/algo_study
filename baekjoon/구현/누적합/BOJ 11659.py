import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))


prefix = [0] * (n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1] + nums[i-1]

for _ in range(m) :
    i, j = map(int, input().split(" "))
    print(prefix[j] - prefix[i-1])