"""

시간초과  -> 순서대로 진행 
"""

def solution(n, m, x, y, queries):
    # n*m 배열
    # 목표 도착점 x,y

    count = 0

    for i in range(n):
        for j in range(m):
            px, py = i, j
            for num, dx in queries:
                if num == 0 or num == 1:
                    # 열 이동
                    if num == 0:
                        if 0 <= py - dx < m:
                            py -= dx
                    elif num == 1:
                        if 0 <= py + dx < m:
                            py += dx
                elif num == 2 or num == 3:
                    # 행 이동
                    if num == 2:
                        if 0 <= px - dx < n:
                            px -= dx
                    elif num == 3:
                        if 0 <= px + dx < n:
                            px += dx
            if px == x and py == y:
                count += 1

    return count