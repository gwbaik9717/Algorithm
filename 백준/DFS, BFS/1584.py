import sys
from collections import deque
n = int(sys.stdin.readline().strip())
danger_area = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
m = int(sys.stdin.readline().strip())
death_area = [list(map(int, sys.stdin.readline().strip().split()))for _ in range(m)]
graph = [[0] * 501 for _ in range(501)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for d in danger_area:
    [x1, y1, x2, y2] = d

    for i in range(min(y1, y2), max(y1, y2) + 1):
        for j in range(min(x1, x2), max(x1, x2) + 1):
            graph[i][j] = 1

for d in death_area:
    [x1, y1, x2, y2] = d

    for i in range(min(y1, y2), max(y1, y2) + 1):
        for j in range(min(x1, x2), max(x1, x2) + 1):
            graph[i][j] = 2

q = deque()
q.append([0, 0, 0])
graph[0][0] = 2 

while q:
    [cy, cx, cd] = q.popleft()

    if (cy, cx) == (500, 500):
        print(cd)
        break

    for i in range(len(dx)):
        nx = cx + dx[i]
        ny = cy + dy[i]
        
        if nx >= 0 and nx <= 500 and ny >= 0 and ny <= 500 and graph[ny][nx] != 2 :
            nd = cd + graph[ny][nx]
        
            if graph[ny][nx] == 0:
                q.appendleft([ny, nx, nd])
            else:
                q.append([ny, nx, nd])
            
            graph[ny][nx] = 2
else:
    print(-1)