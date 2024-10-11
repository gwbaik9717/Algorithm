import sys
from heapq import heappush, heappop

n, e = map(int, sys.stdin.readline().strip().split())

graph = [{} for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().strip().split())

    graph[a][b] = c 
    graph[b][a] = c

v1, v2 = map(int, sys.stdin.readline().strip().split())

INF = 1e9

def get_dist(start, target, dist):
    dist[start] = 0
    heap = []
    heappush(heap, (start, dist[start]))

    while heap:
        s, d = heappop(heap)

        if d > dist[s]:
            continue

        for end, dd in graph[s].items():
            nd = d + dd

            if nd < dist[end]:
                dist[end] = nd
                heappush(heap, (end, nd))
    
    return dist[target]

cases = [[1, v1, v2, n], [1, v2, v1, n]]

ans = INF

for case in cases:
    total = 0

    for i in range(len(case) - 1):
        dists = [INF] * (n + 1)
        dist = get_dist(case[i], case[i+1], dists)
        total += dist

        if dist == INF:
            break
    else:
        ans = min(ans, total)
        continue

    break

if ans == INF:
    print(-1)
else:
    print(ans)