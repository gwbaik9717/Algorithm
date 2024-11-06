from heapq import heappush, heappop

def solution(n, works):
    answer = 0
    
    heap = []
    
    for work in works:
        heappush(heap, -work)
    
    for _ in range(n):
        popped = heappop(heap)
        heappush(heap, min(0, popped + 1))
    
    answer = sum([h**2 for h in heap])
    
    return answer