import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(lambda x: list(f'{x:04b}'), map(int, sys.stdin.readline().split()))) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
couples = []

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(sy, sx):
    visited[sy][sx] = island_index
    q = deque()
    q.append([sy, sx])
    island_area = 0

    while q:
        [cy, cx] = q.popleft()
        island_area += 1

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and visited[ny][nx] != 0 and visited[ny][nx] != island_index:
                couples.append([island_index, visited[ny][nx]])

            if graph[cy][cx][i] == '0' and visited[ny][nx] == 0:
                visited[ny][nx] = island_index
                q.append([ny, nx])

    return island_area

island_index = 0
island_areas = []

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            island_index += 1
            island_areas.append(bfs(i, j))



print(island_index)
print(max(island_areas))
print(max(map(lambda x: island_areas[x[0] - 1] + island_areas[x[1] - 1], couples)))