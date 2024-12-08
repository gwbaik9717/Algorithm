from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    INF = 1e9
    dists = [[INF] * (n+1)  for _ in range(n+1)]
    graph = [dict() for _ in range(n+1)]
    
    
    for start, end, cost in fares:
        graph[start][end] = cost
        graph[end][start] = cost
    
    
    for i in range(1, n+1):
        # i부터 거리계산
        current_dist = dists[i]
        current_dist[i] = 0 
        
        heap = []
        heappush(heap, (current_dist[i], i))
        
        while heap:
            popped_dist, popped_node = heappop(heap)
            
            for key, value in graph[popped_node].items():
                new_dist = popped_dist + value
                if new_dist < current_dist[key]:                
                    current_dist[key] = new_dist
                    heappush(heap, (new_dist, key))
    
    answer = INF
    
    for i in range(1, n+1):
        cost = 0
        
        # i 지점까지 A,B 동승
        cost += dists[s][i]
        
        # i 지점부터 A
        cost += dists[i][a]
        
        # i 지점부터 B
        cost += dists[i][b]
        
        answer = min(answer, cost)
    
    return answer