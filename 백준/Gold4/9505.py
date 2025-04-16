from heapq import heappush, heappop
import sys
t = int(sys.stdin.readline().strip())

for _ in range(t):
    
    k, w, h = map(int, sys.stdin.readline().strip().split(" "))

    cost_dict = dict()

    for _ in range(k):
        name, cost = sys.stdin.readline().strip().split(" ")
        cost_dict[name] = int(cost)
    
    graph = []

    for _ in range(h):
        row = list(map(lambda x: cost_dict[x] if x != "E" else "E", list(sys.stdin.readline().strip())))
        graph.append(row)
    
    start = None

    for i in range(h):
        for j in range(w):
            if graph[i][j] == "E":
                start = [i, j]
                graph[i][j] = 1e9
                break
        else:
            continue

        break

    dists = [[1e9 for _ in range(w)] for _ in range(h)]
    dists[start[0]][start[1]] = 0
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    heap = []
    heappush(heap, [0, start[0], start[1]])

    while len(heap) > 0:
        cc, cy, cx = heappop(heap)
        
        # 가장자리에 도착했을 때
        if cy == 0 or cy == h-1 or cx == 0 or cx == w-1:
            print(cc)
            break
        
        for ddy, ddx in zip(dy, dx):
            ny, nx = cy + ddy, cx + ddx
            nc = cc + graph[ny][nx]

            if ny >= 0 and ny < h and nx >= 0 and nx < w and nc < dists[ny][nx]:
                dists[ny][nx] = nc
                heappush(heap, [nc, ny, nx])