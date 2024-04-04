import sys
import math
from collections import deque

n, r, d, ex, ey = map(int, sys.stdin.readline().strip().split())
towers = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def dist(sx, sy, ex, ey):
    return math.sqrt((sx - ex)**2 + (sy - ey)**2)

# def dfs(index, cnt):
#     global rv
#     cx, cy = towers[index]
#     visited[index] = 1

#     if dist(cx, cy, ex, ey) <= r:
#         rv = max(cnt, rv)
#         return
    
#     for i in range(n):
#         nx, ny = towers[i]
        

#         if i != index:
#             if dist(cx, cy, nx, ny) <= r and visited[i] == 0:
#                 dfs(i, cnt / 2)
#                 visited[i] = 0


def bfs(start):
    q = deque()
    q.append(start)
    visited = [0 for _ in range(n)]

    while q:
        (cx, cy, cc) = q.popleft()

        if dist(cx, cy, ex, ey) <= r:
            return cc
        
        for i in range(n):
            nx, ny = towers[i]

            if (cx, cy) != (nx, ny) and dist(cx, cy, nx, ny) <= r and visited[i] == 0:
                visited[i] = 1
                q.append((nx, ny, cc / 2))
    
    return 0


ans = 0

for i in range(n):
    [sx, sy] = towers[i]
    ans += bfs((sx, sy, d))

print(float(ans))