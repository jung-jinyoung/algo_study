import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline


A, B, C, X, Y = map(int,input().strip().split())
# 양념 A, 후라이드 B, 반반 C
# 최소 양념 X 마리 , 후라이드 Y 마리를 구매

def count_C_cost(a,b,c,x,y):
    if 2*c <= (a+b):
        if x >= y:
            return (2*c*x)
        else:
            return (2*c*y)
    else:
        return(a*X+b*Y)

result = count_C_cost(A,B,C,X,Y)
print(result)