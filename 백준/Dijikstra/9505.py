import sys
import heapq 

n = int(sys.stdin.readline().strip())
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for i in range(n):
    k, w, h = map(int, sys.stdin.readline().strip().split())
    class_dict = dict()
    class_dict['E'] = 0

    for j in range(k):
        [class_name, class_cost] = sys.stdin.readline().strip().split()
        class_dict[class_name] = int(class_cost)
    
    graph = [list(sys.stdin.readline().strip()) for _ in range(h)]

    for j in range(h):
        for k in range(w):
            if graph[j][k] == 'E':
                (sy, sx) = (j, k)
                break
        else:
            continue
        break

    # 다익스트라
    dist = [[sys.maxsize] * w for _ in range(h)]
    dist[sy][sx] = 0
    min_heap = []
    heapq.heappush(min_heap, [0, sy, sx])
    
    while min_heap:
        cc, cy, cx = heapq.heappop(min_heap)
        
        if cy in [0, h-1] or cx in [0, w-1]:
            print(cc)
            break

        for y, x in zip(dy, dx):
            ny = cy + y
            nx = cx + x

            if 0 <= nx < w and 0 <= ny < h:
                nc = cc + class_dict[graph[ny][nx]]

                if nc < dist[ny][nx]:
                    dist[ny][nx] = nc
                    heapq.heappush(min_heap, [nc, ny, nx])