def solution(n, m, x, y, queries):
    x1, x2, y1, y2 = x, x, y, y  # 시작점으로 영역 설정

    # 쿼리를 역순으로 처리
    for command, distance in reversed(queries):
        if command == 0:  # 열 감소 -> 열 증가
            y2 += distance
            if y2 >= m:
                y2 = m - 1
            if y1 != 0:
                y1 += distance
            if y1 >= m:
                return 0

        elif command == 1:  # 열 증가 -> 열 감소
            y1 -= distance
            if y1 < 0:
                y1 = 0
            if y2 != m - 1:
                y2 -= distance
            if y2 < 0:
                return 0

        elif command == 2:  # 행 감소 -> 행 증가
            x2 += distance
            if x2 >= n:
                x2 = n - 1
            if x1 != 0:
                x1 += distance
            if x1 >= n:
                return 0

        elif command == 3:  # 행 증가 -> 행 감소
            x1 -= distance
            if x1 < 0:
                x1 = 0
            if x2 != n - 1:
                x2 -= distance
            if x2 < 0:
                return 0

    return (x2 - x1 + 1) * (y2 - y1 + 1)
