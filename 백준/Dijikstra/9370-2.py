import sys
from heapq import heappush, heappop

tc= int(sys.stdin.readline().strip())
INF = 1e9

def get_dists(n, s, graph):
    dists = [INF for _ in range(n + 1)]
    dists[s] = 0

    heap = []
    heappush(heap, (dists[s], s))

    while heap:
        nc, nn = heappop(heap)

        if nc > dists[nn]:
            continue

        for key, value in graph[nn].items():        
            
            nn = value + nc

            if nn < dists[key]:
                dists[key] = nn
                heappush(heap, (nn, key))
    
    return dists

for _ in range(tc):
    n, m, t = map(int, sys.stdin.readline().strip().split())
    s, g, h = map(int, sys.stdin.readline().strip().split())

    roads = [map(int, sys.stdin.readline().strip().split()) for _ in range(m)]
    candidates = [int(sys.stdin.readline().strip()) for _ in range(t)]

    graph = [{} for _ in range(n + 1)]

    for road in roads:
        a, b, d = road

        graph[a][b] = d
        graph[b][a] = d

    dists_s = get_dists(n, s, graph)
    dists_g = get_dists(n, g, graph)
    dists_h = get_dists(n, h, graph)
    

    min_dists = []

    for candidate in candidates:      
        total_min_dist = dists_s[candidate]
          
        min_dists.append(min(dists_s[g] + graph[g][h] + dists_h[candidate], dists_s[h] + graph[h][g] + dists_g[candidate]))
    
    min_dist = min(min_dists)
    ans = []


    for candidate, dist in zip(candidates, min_dists):
        total_dist = dists_s[candidate]

        if dist != total_dist:
            continue
        
        ans.append(candidate)
    
    ans = sorted(ans)
    ans = map(str, ans)
    
    print(" ".join(ans))