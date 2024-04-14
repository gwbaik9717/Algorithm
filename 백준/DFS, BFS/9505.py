import sys
from collections import deque

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
    
    q = deque()
    visited = [[sys.maxsize] * w for _ in range(h)]

    for j in range(h):
        for k in range(w):
            if graph[j][k] == 'E':
                q.append([j, k, 0])
                visited[j][k] = 0
                break
        else:
            continue
        break

    ans = sys.maxsize

    while q:
        [cy, cx, cd] = q.popleft()

        if cd >= ans:
            continue

        if cy in [0, h - 1] or cx in [0, w - 1]:
            ans = min(ans, cd)
            continue

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            nd = cd + class_dict[graph[ny][nx]]

            if 0 <= nx < w and 0 <= ny < h and nd < visited[ny][nx]:
                visited[ny][nx] = nd
                q.append([ny, nx, nd])
    
    print(ans)