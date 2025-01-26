import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

my_input = input().strip()
splited_arr = my_input.split("-")

answer = sum(list(map(int, splited_arr[0].split("+"))))
for idx in range(1, len(splited_arr)):
    numbers = list(map(int, splited_arr[idx].split("+")))
    answer -= sum(numbers)

print(answer)