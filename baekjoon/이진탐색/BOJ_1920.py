import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
A = [*map(int, input().split())]
m = int(input())
B = [*map(int, input().split())]

def binary_search(target, start, end, data):
    if start > end :
        print(0) 
        return 
    mid  = (start + end) // 2 

    if data[mid] == target :
        print(1)
        return
    elif data[mid] > target :
        end = mid - 1
    else:
        start = mid + 1
    return binary_search(target, start, end, data)



def solution(target, data):
    start = 0 
    end = n-1
    return binary_search(target, start, end, data)

A.sort()
for i in range(m):
    num = B[i]
    solution(num, A)
