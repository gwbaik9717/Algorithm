import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def dfs(start):
    global ans

    [cy, cx, cd] = start

    if graph[cy][cx] == 0:
        graph[cy][cx] = 2
        ans += 1
    
    nd = cd
    for _ in range(4):
        nd = (nd + 3) % 4
        nx, ny = cx + dx[nd], cy + dy[nd]

        if  graph[ny][nx] == 0:
            dfs([ny, nx, nd])
            return
    
    nx, ny = cx - dx[cd], cy - dy[cd]

    if graph[ny][nx] != 1:
        dfs([ny, nx, cd])

dfs([r, c, d])
print(ans)
