import sys
import heapq

INF = sys.maxsize
n, d = map(int, sys.stdin.readline().strip().split())
graph = [[(i + 1, 1)] for i in range(d)] + [[]]
dist = [INF] * (d + 1)

dist[0] = 0

for _ in range(n):
    ss, se, sc = map(int, sys.stdin.readline().strip().split())
    
    if se > d:
        continue

    graph[ss].append((se, sc))


min_heap = []
heapq.heappush(min_heap, (dist[0], 0))

while min_heap:
    cc, cn = heapq.heappop(min_heap)

    for (nn, dc) in graph[cn]:
        nc = cc + dc
        if nc < dist[nn]:
            dist[nn] = nc
            heapq.heappush(min_heap, (nc, nn))

print(dist[-1])