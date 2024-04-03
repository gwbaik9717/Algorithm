import sys
n, pe, pw, ps, pn = map(int, sys.stdin.readline().split())
graph = [[0] * 30 for _ in range(30)]

# 동 서 남 북
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
p = [pe/100, pw/100, ps/100, pn/100]
ans = 0

def dfs(start, cp, cnt):
    rv = 0
    [cy, cx] = start
    
    graph[cy][cx] = 1

    if cnt == n:
        return cp

    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        np = cp * p[i]

        if graph[ny][nx] == 0:
            rv += dfs([ny, nx], np, cnt + 1)
            graph[ny][nx] = 0
    
    return rv

print(dfs([14, 14], 1, 0))