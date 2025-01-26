import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

# 역순으로 접근하여 고점일 때 팔 수 있도록 하는 함수 생성

def function(stocks: list, n : int):
    
    max_stock = stocks[-1]
    my_profit = 0 

    # 역순 접근 : 가장 고점일 때 팔 수 있도록
    for idx in range(n-1, -1, -1):
        now = stocks[idx]
        if now <= max_stock:
            my_profit += max_stock - now
        else:
            max_stock = now
    
    return my_profit


T = int(input())

for _ in range(T):
    N = int(input())
    stocks = list(map(int, input().split(" ")))
    answer = function(stocks, N)
    print(answer)