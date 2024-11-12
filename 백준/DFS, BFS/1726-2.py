import sys
from collections import deque

INF = 1e9
m, n = map(int, sys.stdin.readline().strip().split())
board = [sys.stdin.readline().strip().split() for _ in range(m)]
start = tuple(map(lambda x: int(x) - 1, sys.stdin.readline().strip().split()))
end = tuple(map(lambda x: int(x) - 1, sys.stdin.readline().strip().split()))

visited = [[[INF] * 4 for _ in range(n)] for _ in range(m)]

# 동쪽이 1, 서쪽이 2, 남쪽이 3, 북쪽이 4로
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

q = deque()
q.append((start[0], start[1], start[2], 0))
visited[start[0]][start[1]][start[2]] = 0

answer = INF

while q:
    cy, cx, cd, cc = q.popleft()

    if cc >= answer:
        continue

    if (cy, cx, cd) == (end[0], end[1], end[2]):
        answer = min(answer, cc)
        continue

    # 움직이기
    for i in range(1, 4):
        ny, nx, nc = cy + i * dy[cd], cx + i * dx[cd], cc + 1
        
        if 0 <= ny < m and 0 <= nx < n:
            if board[ny][nx] == '1':
                break

            if nc >= visited[ny][nx][cd]:
                continue

            visited[ny][nx][cd] = 1
            q.append((ny, nx, cd, nc))


    # 회전하기
    for nd, zipped in enumerate(zip(dy, dx)):
        if nd == cd: 
            continue

        zy, zx = zipped

        if abs(zy) == abs(dy[cd]) and abs(zx) == abs(dx[cd]):
            if nc < visited[cy][cx][nd]:
                visited[cy][cx][nd] = nc
                q.append((cy, cx, nd, cc + 2))
        
        else:
            if nc < visited[cy][cx][nd]:
                visited[cy][cx][nd] = nc
                q.append((cy, cx, nd, cc + 1))
    
print(answer)