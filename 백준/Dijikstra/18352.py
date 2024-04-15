import sys
import heapq 

INF = sys.maxsize
n, m, k, x = map(int, sys.stdin.readline().strip().split())
lines = [map(int, sys.stdin.readline().strip().split()) for _ in range(m)]

checked = [0] * (n + 1)
dist = [INF] * (n + 1)
dist[x] = 0

graph = [[] for _ in range(n + 1)]

for (start, end) in lines:
    graph[start].append(end)

min_heap = []
heapq.heappush(min_heap, (dist[x], x))

while min_heap:
    cc, cn = heapq.heappop(min_heap)
    checked[cn] = 1
    nc = cc + 1

    for nn in graph[cn]:
        if checked[nn] == 0 and nc < dist[nn]:
            dist[nn] = nc
            heapq.heappush(min_heap, (nc, nn))

flag = False
for i, v in enumerate(dist):
    if v == k:
        flag = True
        print(i)
if not flag:
    print(-1)