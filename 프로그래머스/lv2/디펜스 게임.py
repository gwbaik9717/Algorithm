from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0
    heap = []
    temp_sum = 0
    
    for e in enemy:
        heappush(heap, -e)
        temp_sum += e
        
        while k > 0 and heap and temp_sum > n:
            popped = heappop(heap)
            temp_sum += popped
            k -= 1
        
        if temp_sum <= n:
            answer += 1
        else:
            break
            
    return answer