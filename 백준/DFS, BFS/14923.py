import sys
from collections import deque


n, m = map(int, sys.stdin.readline().strip().split())
hy, hx = map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())
ey, ex = map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

board = [sys.stdin.readline().strip().split() for _ in range(n)]
checked = [[[False] * 2 for _ in range(m)] for _ in range(n)]

answer = 1e9

def bfs():
    global answer

    q = deque()
    q.append((hy, hx, 0, 1))

    checked[hy][hx][1] = True

    while q:
        cy, cx, cc, used = q.popleft()
        
        if (cy, cx) == (ey, ex):
            answer = min(answer, cc)
        
        if cc >= answer:
            break

        for i in zip(dy, dx):
            ddy, ddx = i

            ny = cy + ddy
            nx = cx + ddx
            nc = cc + 1

            if 0 <= nx < m and 0 <= ny < n:
                
                if board[ny][nx] == "1":
                    # 사용하지 않았을 때 사용 처리
                    if used == 1 and not checked[ny][nx][0]:
                        checked[ny][nx][0] = True
                        q.append((ny, nx, nc, 0))
                elif board[ny][nx] == "0" and not checked[ny][nx][used]:
                    checked[ny][nx][used] = True
                    q.append((ny, nx, nc, used))

bfs()

if answer == 1e9:
    print(-1)
else:
    print(answer)