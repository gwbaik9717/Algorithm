import sys
from heapq import heappush, heappop

vv, e = map(int, sys.stdin.readline().strip().split())
k = int(sys.stdin.readline().strip())

INF = int(1e9)

# Graph representation as adjacency lists (dictionary of dictionaries)
graph = [{} for _ in range(vv + 1)]

# Read in the edges
for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w

# Distance array initialized to infinity
dists = [INF] * (vv + 1)
dists[k] = 0  # Starting node distance to itself is 0

# Priority queue (min-heap), storing (distance, node)
heap = []
heappush(heap, (0, k))  # Start with the source node (distance 0, node k)

# Dijkstra's algorithm
while heap:
    current_dist, start = heappop(heap)

    # If the current distance is greater than the already found distance, skip it
    if current_dist > dists[start]:
        continue

    # Traverse all adjacent nodes
    for end, weight in graph[start].items():
        new_dist = current_dist + weight

        # If a shorter path is found
        if new_dist < dists[end]:
            dists[end] = new_dist
            heappush(heap, (new_dist, end))

# Output the result
for i in range(1, vv + 1):
    print(dists[i] if dists[i] != INF else "INF")
