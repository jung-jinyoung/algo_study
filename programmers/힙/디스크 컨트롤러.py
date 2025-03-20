from heapq import heappush, heappop

def solution(jobs):
    # 요청 시간 기준으로 정렬
    jobs.sort()
    
    # 우선순위 큐 (작업 시간이 짧은 순으로 실행)
    h = []
    now, total_time, idx = 0, 0, 0
    job_count = len(jobs)

    while idx < job_count or h:
        # 현재 시간(now)까지 요청된 모든 작업을 큐에 삽입
        while idx < job_count and jobs[idx][0] <= now:
            heappush(h, (jobs[idx][1], jobs[idx][0]))  # 실행 시간 기준 정렬
            idx += 1

        if h:
            # 가장 짧은 작업 실행
            duration, start = heappop(h)
            now += duration
            total_time += now - start  # 요청부터 종료까지의 시간 계산
        else:
            # 대기할 작업이 없다면 다음 작업의 요청 시간으로 이동
            now = jobs[idx][0]

    return total_time // job_count  # 평균값 반환

