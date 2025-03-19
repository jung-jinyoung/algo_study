from itertools import permutations


def solution(k, dungeons):
    answer = -1

    l = len(dungeons)
    arr = permutations([i for i in range(l)])
    for combi in arr:
        temp = k
        cnt = 0
        for i in combi:
            req, use = dungeons[i]
            if (temp < req): continue
            if (temp - use >= 0):
                temp -= use
                cnt += 1
            else:
                break
        answer = max(answer, cnt)

    return answer