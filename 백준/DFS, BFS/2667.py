import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]

houses = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(start):
    q = deque()
    q.append(start)
    [sy, sx] = start
    graph[sy][sx] = 0
    cnt = 0

    while q:
        [cy, cx] = q.popleft()
        cnt += 1

        for i in range(len(dx)):
            ny = cy + dy[i]
            nx = cx + dx[i]
            
            if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[ny][nx] == 1:
                q.append([ny, nx])
                graph[ny][nx] = 0
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append(bfs([i, j]))

houses.sort()

print(len(houses))
print('\n'.join(str(house) for house in houses))