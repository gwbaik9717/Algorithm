import sys
from copy import deepcopy

n, L, R = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

ans = 0

def start_round():

    total, count = 0, 0

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    checked = [[0] * n for _ in range(n)]

    to_change = []

    def dfs(position):
        nonlocal total, count

        count += 1
        
        cy, cx = position
        to_change.append((cy, cx))
        checked[cy][cx] = 1
        total += graph[cy][cx]
        
        for zipped in zip(dy, dx):
            ny, nx = cy + zipped[0], cx + zipped[1]

            if 0 <= ny < n and 0 <= nx < n and checked[ny][nx] == 0 and L <= abs(graph[ny][nx] - graph[cy][cx]) <= R:
                dfs((ny, nx))

    
    for i in range(n):
        for j in range(n):
            if checked[i][j] == 0:
                dfs((i, j))
                for change in to_change:
                    cy, cx = change
                    graph[cy][cx] = total // count

                total, count = 0, 0
                to_change = []

while True:
    prev = deepcopy(graph)
    start_round()
    

    if prev == graph:
        break
    
    ans += 1

print(ans)