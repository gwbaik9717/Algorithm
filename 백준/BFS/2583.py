import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())
rects = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

graph = [[0 for _ in range(n)] for _ in range(m)]
areas = 0
answer = []

for rect in rects:
    [lx, ly, rx, ry] = rect
    
    for i in range(ly, ry):
        for j in range(lx, rx):
    
            graph[i][j] = 1

def bfs(start):
        q = deque()
        q.append(start)
        rv = 0
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        while q:
            [cy, cx] = q.popleft()
    
            rv += 1

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if nx>=0 and nx<n and ny>=0 and ny<m and graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    q.append([ny, nx])
        
        return rv
    
for i in range(0, m):
     for j in range(0, n):
          if graph[i][j] == 0:
              areas += 1
              graph[i][j] = 1
              answer.append(bfs([i, j]))

answer.sort()

print(areas)
print(" ".join(list(map(str, answer))))