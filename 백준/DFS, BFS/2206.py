import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
visited = [[[0] * 2 for _ in range(m)]  for _ in range(n)]

    
q = deque()
q.append([0, 0, 0, 1])

while q:
    [cy, cx, cc, cd] = q.popleft()

    if cy == n-1 and cx == m-1:
        print(cd)
        exit()

    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]

        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            # 벽일 경우 벽 부수기
            if graph[ny][nx] == 1 and visited[ny][nx][cc] == 0 and cc == 0:
                visited[ny][nx][cc] = 1
                q.append([ny, nx, 1, cd + 1])
            
            # 벽이 아닐 경우
            if graph[ny][nx] == 0 and visited[ny][nx][cc] == 0:
                visited[ny][nx][cc] = 1
                q.append([ny, nx, cc, cd + 1])

print(-1)