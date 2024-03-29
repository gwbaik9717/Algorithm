import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
island_index = 0

edges = []
visited = [[0] * n for _ in range(n)]
def bfs(start):
    global island_index
    island_index += 1

    q = deque()
    q.append(start)

    [sy, sx] = start
    visited[sy][sx] = 1
    graph[sy][sx] = island_index
    edge = []

    while q:
        [cy, cx] = q.popleft()
        
        for i in range(len(dx)):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and visited[ny][nx] == 0:
                visited[ny][nx] = 1
 
                if graph[ny][nx] != 0:
                    graph[ny][nx] = island_index
                    q.append([ny, nx])
                else:
                    edge.append([ny, nx, 1])
    edges.append(edge)

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and visited[i][j] == 0:
            bfs([i, j])

def get_distance(start, curr_island):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append(start)
    [sy, sx, sd] = start
    visited[sy][sx] = 1

    while q:
        [cy, cx, cd] = q.popleft()

        for i in range(len(dx)):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and visited[ny][nx] == 0 and cd < ans:
                visited[ny][nx] = 1
                if graph[ny][nx] != 0 and graph[ny][nx] != curr_island: 
                    return cd
                q.append([ny, nx, cd + 1])
    
    return None

ans = 10000
for i, edge in enumerate(edges):
    for e in edge:
         dist = get_distance(e, i + 1)

         if dist != None:
             ans = min(ans, dist)

print(ans)