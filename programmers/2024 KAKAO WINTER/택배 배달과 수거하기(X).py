"""
시간 초과

"""

def solution(cap, n, deliveries, pickups):
    info = []
    for i in range(n):
        info.append([deliveries[i], pickups[i]])

    answer = 0
    num = n - 1
    while num >= 0:
        # 배달가야 하는 가장 멀리 있는 집의 번호 계산
        while num >= 0 and info[num][0] + info[num][1] == 0:
            num -= 1

        if num < 0:
            break

        stack1 = cap
        # 배달
        for idx in range(num, -1, -1):
            # 모두 배달
            if not stack1:
                break

            if info[idx][0]:
                info[idx][0], stack1 = max(info[idx][0] - stack1, 0), max(stack1 - info[idx][0], 0)

        # 수거
        stack2 = cap
        for idx in range(num, -1, -1):
            # 수거 불가
            if not stack2:
                break

            if info[idx][1]:
                info[idx][1], stack2 = max(info[idx][1] - stack2, 0), max(stack2 - info[idx][1], 0)

        # 거리 저장
        answer += num + 1

    return 2 * answer