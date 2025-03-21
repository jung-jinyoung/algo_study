from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    for fr, to in tickets:
        routes[fr].append(to)
    # 정렬
    for fr in routes:
        routes[fr].sort()
    # 출발지
    path = ["ICN"]
    answer = []
    def dfs(airport):
        # 모든 공항 순회했을 경우
        if len(path) == len(tickets) + 1:
            answer.extend(path)
            return True
        # 출발할 수 있는 공항이 없을 경우
        if airport not in routes:
            return False
        
        for i in range(len(routes[airport])):
            next_airport = routes[airport][i]
            if next_airport == "":
                continue
            # 여행지 추가 후 확인
            path.append(next_airport)
            # 티켓 사용 처리
            routes[airport][i] = ""
            # 성공했으면 return
            if dfs(next_airport) :
                return True
            
            # 복구
            path.pop()
            routes[airport][i] = next_airport
        # 모두 순회했는데 없을 경우
        return False
    
    dfs("ICN")
    return answer