import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n ,m = map(int, input().split(" "))
cards = list(map(int,input().split(" ")))

cards.sort()


for _ in range(m):
    request = cards[0] + cards[1]
    cards[0] = request
    cards[1] = request
    cards.sort()

print(sum(cards))

