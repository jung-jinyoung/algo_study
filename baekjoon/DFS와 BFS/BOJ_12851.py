import sys
from collections import defaultdict, deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


# 입력 받기
N, K = map(int, input().strip().split())

# 초기화
my_info = defaultdict(int)
my_arr = deque([N])

# 방문 시간 저장
my_info[N] = 0

# 결과 변수
answer = 0
cnt = 0

# BFS 시작
while my_arr:
    now_pos = my_arr.popleft()

    # 동생을 찾은 경우 처리
    if now_pos == K:
        # 첫 번째 발견 시 최단 시간 저장
        if answer == 0:
            answer = my_info[now_pos]
        # 최단 시간에 도달한 경우의 수 카운트
        if my_info[now_pos] == answer:
            cnt += 1

    # 다음 위치 탐색
    for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2):
        if 0 <= next_pos <= 100000:
            # 아직 방문하지 않았거나, 동일 최단 시간으로 방문 가능한 경우
            if next_pos not in my_info or my_info[next_pos] >= my_info[now_pos] + 1:
                my_arr.append(next_pos)
                my_info[next_pos] = my_info[now_pos] + 1

# 결과 출력
print(answer)
print(cnt)
