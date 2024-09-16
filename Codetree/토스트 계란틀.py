import sys
from collections import deque

n, L, R = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

ans = 0

def start_round():

    total, count = 0, 0

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    checked = [[0] * n for _ in range(n)]

    to_change = []

    def bfs(position):
        nonlocal total, count
        count += 1
        q = deque()
        q.append(position)

        cy, cx = position
        to_change.append((cy, cx))
        checked[cy][cx] = 1
        total += graph[cy][cx]

        while q:
            cy, cx = q.popleft()

            for zipped in zip(dy, dx):
                ny, nx = cy + zipped[0], cx + zipped[1]

                if 0 <= ny < n and 0 <= nx < n and checked[ny][nx] == 0 and L <= abs(graph[ny][nx] - graph[cy][cx]) <= R:
                    checked[ny][nx] = 1
                    count += 1
                    q.append((ny, nx))
                    to_change.append((ny, nx))
                    total += graph[ny][nx]

    found = False
                    
    for i in range(n):
        for j in range(n):
            if checked[i][j] == 0:
                bfs((i, j))

                if len(to_change) > 1:
                    found = True

                for change in to_change:
                    cy, cx = change
                    graph[cy][cx] = total // count

                total, count = 0, 0
                to_change = []
    
    return found

while True:
    restart = start_round()

    if restart:
        ans += 1
    else:
        break 

print(ans)