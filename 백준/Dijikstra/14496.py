import sys
import heapq 

INF = sys.maxsize

a, b = map(int, sys.stdin.readline().strip().split())
n, m = map(int, sys.stdin.readline().strip().split())

dist = [INF] * (n + 1)
dist[a] = 0
graph = [[] for _ in range(n + 1)]

for i in range(m):
    start, end = map(int, sys.stdin.readline().strip().split())
    graph[start].append(end)
    graph[end].append(start)

min_heap = []
heapq.heappush(min_heap, (dist[a], a))

while min_heap:
    cc, cn = heapq.heappop(min_heap)
    
    for nn in graph[cn]:
        nc = cc + 1

        if nc < dist[nn]:
            dist[nn] = nc
            heapq.heappush(min_heap, (nc, nn))

if dist[b] == sys.maxsize:
    print(-1)
else:
    print(dist[b])