import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
h, w, sy, sx, fy, fx = map(int, sys.stdin.readline().strip().split())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

q = deque()
q.append((sy - 1, sx - 1, 0))
visited[sy-1][sx-1] = 1
walls = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            walls.append([i, j])

def check(cy, cx):
    for [wy, wx] in walls:
        if cy <= wy < cy + h and cx <= wx < cx + w:
            return False
    return True

while q:
    cy, cx, cc = q.popleft()
    
    if (cy, cx) == (fy - 1, fx - 1):
        print(cc)
        break

    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        nc = cc + 1
        
        if nx >= 0 and nx + w <= m and ny >= 0 and ny + h <= n and check(ny, nx) and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            q.append((ny, nx, nc))
            
else:
    print(-1)