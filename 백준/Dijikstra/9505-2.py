import sys
from heapq import heappush, heappop

t = int(sys.stdin.readline().strip())
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for _ in range(t):
    k, w, h = map(int, sys.stdin.readline().strip().split())

    class_dict = dict()

    for _ in range(k):
        class_name, cost = sys.stdin.readline().strip().split()
        class_dict[class_name] = int(cost)
    
    board = [list(sys.stdin.readline().strip()) for _ in range(h)]
    dists = [[1e9] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == 'E':
                start = (i, j)
                break
        else:
            continue

        break

    sy, sx = start
    dists[sy][sx] = 0

    q = []
    heappush(q, (0, sy, sx))
    answer = 1e9

    while q:
        cc, cy, cx = heappop(q)
        
        if cc >= answer:
            continue

        if cy in [0, h-1] or cx in [0, w-1]:
            answer = min(answer, cc)
            continue

        for zy, zx in zip(dy, dx):
            ny, nx = cy + zy, cx + zx
            
            if 0 <= ny < h and 0 <= nx < w:
                if board[ny][nx] == 'E':
                    continue

                nc = cc + class_dict[board[ny][nx]]

                if nc < dists[ny][nx]:
                    heappush(q, (nc, ny, nx))
                    dists[ny][nx] = nc
    
    print(answer)