import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
# 도감 수 N, 문제 수 M

info_name = {}
info_num = {}
for num in range(1,N+1):
    name = input().strip()
    info_name[name] = num
    info_num[num] = name

# 문제 
for _ in range(M):
    quiz = input().strip()
    
    # 도감 번호이면
    if quiz.isdigit():
       print(info_num[int(quiz)])
    # 포켓몬 이름이면
    else:
        print(info_name[quiz])


