import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
ans = 0

dz = [0, 0, 0, 0, 1, -1]
dy = [1, 0, -1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append([i, j, k, 0])


while q:
    [cz, cy, cx, cd] = q.popleft()
    ans = cd
    
    for i in range(len(dz)):
        nz = cz + dz[i]
        ny = cy + dy[i]
        nx = cx + dx[i]
        
        if nz >= 0 and nz < h and ny >= 0 and ny < n and nx >= 0 and nx < m and graph[nz][ny][nx] == 0:
            q.append([nz, ny, nx, cd + 1])
            graph[nz][ny][nx] = 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                ans = -1
                break
        else:
            continue
        break
    
    else:
        continue
    break

print(ans)