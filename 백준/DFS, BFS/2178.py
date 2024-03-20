import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[int(str) for str in list(sys.stdin.readline().strip())] for _ in range(n)]

dx = [0, 1, 0, - 1]
dy = [1, 0, -1, 0]


q = deque()
q.append([0, 0, 1])
graph[0][0] = 0

while q:
    [cy, cx, cd] = q.popleft()
    if cy == n-1 and cx == m-1:
        print(cd)
        break

    for i in range(len(dx)):
        ny = cy + dy[i]
        nx = cx + dx[i]
        
        if nx >= 0 and nx < m and ny >= 0 and ny < n and graph[ny][nx] == 1:
            graph[ny][nx] = 0
            q.append([ny, nx, cd+1])