import sys
from collections import deque

dy = [1, 0, -1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
    l, r, c = map(int, sys.stdin.readline().strip().split())
    
    if (l, r, c) == (0, 0, 0):
        break
    
    graph = [[list(sys.stdin.readline().strip()) for _ in range(r + 1)][:-1] for _ in range(l)]
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    q = deque()
    
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    q.append([i, j, k, 0])
                    visited[i][j][k] = 1
                    break
            else:
                continue
            break
        else:
            continue
        break


    while q:
        [cz, cy, cx, cd] = q.popleft()

        if graph[cz][cy][cx] == 'E':
            print(f"Escaped in {cd} minute(s).")
            break

        for i in range(6):
            nz = cz + dz[i]
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c and graph[nz][ny][nx] != '#' and visited[nz][ny][nx] == 0:
                visited[nz][ny][nx] = 1
                q.append([nz, ny, nx, cd + 1])
    else:
        print("Trapped!")