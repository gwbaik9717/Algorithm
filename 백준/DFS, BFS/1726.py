import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
sy, sx, sd = map(lambda x: int(x) - 1, sys.stdin.readline().split())
ey, ex, ed = map(lambda x: int(x) - 1, sys.stdin.readline().split())
visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
dm = [1, 2, 3]
new_dir = [((3,1), (2,1), (1,2)), ((3, 1), (2, 1), (0, 2)), ((0, 1), (1, 1), (3, 2)), ((0, 1), (1, 1),(2, 2))]

visited[sy][sx][sd] = 1
q = deque()
q.append([sy, sx, sd, 0])

while q:
    [cy, cx, cd, cc] = q.popleft()
    
    if (cy, cx, cd) == (ey, ex, ed):
        print(cc)
        break
    
    # 움직일때
    for i in range(3):
        nx = cx + dx[cd] * dm[i]
        ny = cy + dy[cd] * dm[i]

        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            if graph[ny][nx] == 1:
                break
            elif visited[ny][nx][cd] == 1:
                continue
            else:
                visited[ny][nx][cd] = 1
                q.append([ny, nx, cd, cc + 1])

    # 회전할때
    for nd, dc in new_dir[cd]:
        if visited[cy][cx][nd] == 0:
            visited[cy][cx][nd] = 1
            q.append([cy, cx, nd, cc + dc])
