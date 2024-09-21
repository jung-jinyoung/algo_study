import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
A = [*map(int, input().split())]
m = int(input())
B = [*map(int, input().split())]

A.sort()
cards = {}

for card in A :
    if card in cards:
        cards[card] +=1
    else:
        cards[card] = 1

def binary_search(target, start, end, data):
    if start > end :
        print(0, end = " ")
        return 
    mid = (start + end) // 2

    if data[mid] == target :
        print(cards[target], end=" ")
        return 
    elif data[mid] > target : 
        end = mid - 1
    else:
        start = mid + 1
    return binary_search(target, start, end, data)
    



def solution(target, data):
    start = 0
    end = n - 1
    return binary_search(target, start, end, data)

for card in B:
    solution(card, A)


