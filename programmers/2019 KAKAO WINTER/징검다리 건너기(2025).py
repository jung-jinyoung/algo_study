from heapq import heappush, heappop

def solution(stones, k):
    h = []
    result = float("inf")
    
    for i in range(len(stones)):
        heappush(h, (-stones[i], i))  # 최대 힙 유지 (값을 음수로 변환)
        
        if i >= k - 1:
            while (h[0][1] < i - k +1 ) :
                result = min(result, -h[0][0])  # 현재 힙의 최대값을 결과로 갱신
                heappop(h)
            result = min(result, h[0][0])

    return result
