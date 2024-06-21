from collections import deque


def solution(cap, n, deliveries, pickups):
    dv = deque()
    pu = deque()

    answer = 0

    for idx in range(n):
        if deliveries[idx]:
            dv.append([idx, deliveries[idx]])
        if pickups[idx]:
            pu.append([idx, pickups[idx]])

    while dv or pu:

        stack1 = cap
        max_dis = 0
        while dv and stack1:
            num1, d = dv.pop()
            max_dis = max(max_dis, num1)
            if d - stack1 < 0:
                d, stack1 = 0, stack1 - d
            elif d - stack1 == 0:
                d, stack1 = 0, 0
            else:
                d, stack1 = d - stack1, 0

            if d > 0:
                dv.append([num1, d])

        stack2 = cap
        while pu and stack2:
            num2, p = pu.pop()
            max_dis = max(max_dis, num2)
            if p - stack2 < 0:
                p, stack2 = 0, stack2 - p
            elif p - stack2 == 0:
                p, stack2 = 0, 0
            else:
                p, stack2 = p - stack2, 0

            if p > 0:
                pu.append([num2, p])

        answer += 2 * (max_dis + 1)

    return answer