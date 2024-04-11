import sys
from collections import deque

n = int(sys.stdin.readline().strip())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs_normal(sy, sx):
    q = deque()
    q.append([sy, sx])
    visited_normal[sy][sx] = 1
    
    while q:
        [cy, cx] = q.popleft()
        cc = graph[cy][cx]

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 같은 색상일 때
            if 0 <= nx < n and 0 <= ny < n and visited_normal[ny][nx] == 0 and graph[ny][nx] == cc:
                visited_normal[ny][nx] = 1
                q.append([ny, nx])

def bfs_color(sy, sx):
    q = deque()
    q.append([sy, sx])
    visited_color[sy][sx] = 1
    
    while q:
        [cy, cx] = q.popleft()
        cc = graph[cy][cx]

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 비슷한 색상일 때
            if 0 <= nx < n and 0 <= ny < n and visited_color[ny][nx] == 0:
                if (cc in ['R', 'G'] and graph[ny][nx] in ['R', 'G']) or graph[ny][nx] == cc:
                    visited_color[ny][nx] = 1
                    q.append([ny, nx])
                

visited_normal = [[0] * n for _ in range(n)]
visited_color = [[0] * n for _ in range(n)]
ans_normal = 0
ans_color = 0

for i in range(n):
    for j in range(n):
        if visited_normal[i][j] == 0:
            bfs_normal(i, j)
            ans_normal += 1
        
        if visited_color[i][j] == 0:
            bfs_color(i, j)
            ans_color += 1

print(ans_normal, ans_color)
