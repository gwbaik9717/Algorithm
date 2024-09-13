import sys

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dir = [i for i in range(4)] # 북동남서

n, m = map(int, sys.stdin.readline().strip().split())
sy, sx, sd = map(int, sys.stdin.readline().strip().split())
cx, cy, cd = sx, sy, sd

graph = [sys.stdin.readline().strip().split() for _ in range(n)]
checked = [[0] * m for _ in range(n)]

checked[sy][sx] = 1

while True:
    for i in range(4):
        cd = (cd - 1) % 4 
        ny, nx = cy + dy[cd], cx + dx[cd]

        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == "0" and checked[ny][nx] == 0:
                cy, cx = ny, nx
                checked[ny][nx] = 1
                break
        
    else:
        # 한 칸 후진
        ny, nx = cy + (-1) * dy[cd], cx + (-1) * dx[cd]

        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == "0":
            cy, cx = ny, nx
            checked[ny][nx] = 1
            continue
        else:
            break

print(sum([sum(row) for row in checked]))








        



        
    
