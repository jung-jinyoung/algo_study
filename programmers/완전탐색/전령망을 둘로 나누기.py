from collections import deque


def bfs(start, nodes, n):
    visited = [False for _ in range(n + 1)]
    # 출발 노드 정보 저장
    myque = deque([start])
    visited[start] = True
    cnt = 1
    while (myque):
        node = myque.popleft()
        for next in nodes[node]:
            if not visited[next]:
                visited[next] = True
                myque.append(next)
                cnt += 1
    return cnt


def solution(n, wires):
    answer = int(1e9)

    ## 완전 탐색
    for i in range(len(wires)):
        nodes = [[] for _ in range(n + 1)]
        for (j, (v1, v2)) in enumerate(wires):
            # i번째 간선 제거
            if i == j:
                continue
            nodes[v1].append(v2)
            nodes[v2].append(v1)

        for j in range(n + 1):
            if len(nodes[j]) > 0:
                group = bfs(j, nodes, n)
                break
        diff = abs((n - group) - group)
        answer = min(diff, answer)

    return answer