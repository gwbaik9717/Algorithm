import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
ans = 0
temp = 0

# 공기에서 접근하자
def bfs(sy, sx):
    global temp
    melted = False

    checked = [[0] * m for _ in range(n)]
    q = deque()
    q.append([sy, sx])
    to_melt = []
    checked[sy][sx] = 1

    while q: 
        [cy, cx] = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and checked[ny][nx] == 0:
                checked[ny][nx] = 1
                if graph[ny][nx] == 0:
                    q.append([ny, nx])
                else:
                    to_melt.append([ny, nx])

    # 치즈 녹이기
    if len(to_melt) > 0:
        melted = True
        temp = len(to_melt)
        for [my, mx] in to_melt:
            graph[my][mx] = 0
    
    return melted

while bfs(0, 0):
    ans += 1

print(ans)
print(temp)