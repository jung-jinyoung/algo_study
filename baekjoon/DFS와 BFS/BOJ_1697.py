import sys
from collections import defaultdict, deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().strip().split())


max_result = abs(N-K)
my_info = defaultdict(int)
my_arr = deque()

my_arr.append(N)

while my_arr :
    now_pos = my_arr.popleft()
    if now_pos == K :
        print(my_info[now_pos])
        break

    if 0 <= now_pos <= 100000:
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            if my_info[next_pos] == 0 :
                my_arr.append(next_pos)
                my_info[next_pos] = my_info[now_pos] + 1
    
