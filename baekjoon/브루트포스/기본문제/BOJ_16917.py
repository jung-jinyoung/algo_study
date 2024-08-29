import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

A, B, C, X, Y = map(int , input().strip().split())

# 해당 개수 만큼 바로 구매 하는 경우
cost1 = A*X + B*Y

# 일부만 반반 치킨으로 구매할 경우 

cost2 = 2*C*min(X, Y) + A * max(0,X-Y) + B * max(0, Y-X)

# 모두 반반 치킨으로 구매할 경우 
cost3 = 2*C*max(X,Y)

result = min(cost1, cost2, cost3)
print(result)