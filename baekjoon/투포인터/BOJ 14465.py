import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 횡당보도 n, 요구되는 연속한 신호등 개수 k, 고장난 신호등 개수 b
n, k, b = map(int, input().split(" "))
broken_list = [int(input())-1 for _ in range(b)]

# 신호등이 고장났으면 1, 고장나지 않았다면 0
arr = [1 if i in broken_list else 0 for i in range(n)]

# 초기 윈도우 고장 개수
current = sum(arr[:k])
ans = current

# 슬라이딩 윈도우
for j in range(k, n) :
    current += arr[j]
    current -= arr[j - k]
    ans = min (ans, current)
    
print(ans)