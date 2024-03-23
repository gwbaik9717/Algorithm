import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def count(start):
    cnt = 0
    [cy, cx] = start
    for i in range(len(dx)):
        ny = cy + dy[i]
        nx = cx + dx[i]
        
        if graph[ny][nx] == 0:
            cnt += 1
    return cnt

def bfs(start):
    [sy, sx] = start
    q = deque()
    visited[sy][sx] = True

    q.append(start)
    
    while q:
        [cy, cx] = q.popleft()
        to_melt[cy][cx] = count([cy, cx])
        
        for i in range(len(dx)):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if nx >= 0 and nx < m and ny >= 0 and ny < n and not visited[ny][nx] and graph[ny][nx] != 0:
                q.append([ny, nx])
                visited[ny][nx] = True

    return 1
  

ans = 0
flag = False
while True:
    visited = [[False] * m for _ in range(n)]
    to_melt = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    
    for i in range(n):
        for j in range(m): 
            if graph[i][j] != 0 and not visited[i][j]:
                cnt += bfs([i, j])

                if cnt > 1:
                    break
        else:
            continue
        break
    
    else:
        if cnt == 0:
            flag = True
            break
        for i in range(n):
            for j in range(m):
                graph[i][j] = max(0, graph[i][j] - to_melt[i][j])
        ans += 1
        continue
    break

if flag:
    print(0)
else:
    print(ans)