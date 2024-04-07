import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline()) for _ in range(n)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(sy, sx):
    checked = [[0] * k for _ in range(n)]
    q = deque()
    q.append([sy, sx, 0])
    checked[sy][sx] = 1
    rv = 0 


    while q:
        [cy, cx, cd] = q.popleft()

        rv = max(rv, cd)

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            nd = cd + 1

            if nx >= 0 and nx < k and ny >= 0 and ny < n and checked[ny][nx] == 0 and graph[ny][nx] == 'L':
                checked[ny][nx] = 1
                q.append([ny, nx, nd])
    
    return rv

ans = 0

for i in range(n):
    for j in range(k):
        if graph[i][j] == 'L':
            ans = max(ans, bfs(i, j))

print(ans)