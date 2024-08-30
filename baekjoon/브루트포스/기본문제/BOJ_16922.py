import sys
from itertools import product, combinations_with_replacement
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

my_dirs = {'I':1,'V':5,'X':10,'L':50}
my_nums = [1,5,10,50]

N = int(input())

result_set = set()

for comb in (combinations_with_replacement(my_nums,N)):
    total = sum(comb)
    result_set.add(total)
print(len(result_set))
