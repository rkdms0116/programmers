import heapq

def solution(n, works):
        
    answer = 0
    # 일을 다 해낼 수 있다면
    if sum(works) <= n:
        return answer
    
    heap = [-work for work in works]
    heapq.heapify(heap)
    
    for _ in range(n):
        w = heapq.heappop(heap)
        w += 1
        heapq.heappush(heap, w)
    
    for work in heap:
        answer += work ** 2
    
    return answer