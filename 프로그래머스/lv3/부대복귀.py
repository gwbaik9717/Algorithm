from heapq import heappop, heappush

def solution(n, roads, sources, destination):
    answer = []
    board = [[] for _ in range(n+1)]
    
    for start, end in roads:
        board[start].append(end)
        board[end].append(start)
    
    INF = 1e9
    
    dist = [INF] * (n+1)
    dist[destination] = 0
    
    heap = []
    heappush(heap, (dist[destination], destination))
    
    while heap:
        
        current_dist, current_node = heappop(heap)
        
        for cn in board[current_node]:
            nd = current_dist + 1
            if nd < dist[cn]:
                dist[cn] = nd
                heappush(heap, (nd, cn))
                
    answer = [(dist[source] if dist[source] != INF else -1) for source in sources]
        

    return answer