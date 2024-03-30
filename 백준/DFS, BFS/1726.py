import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
sy, sx, sd = map(lambda x: int(x) - 1, sys.stdin.readline().split())
ey, ex, ed = map(lambda x: int(x) - 1, sys.stdin.readline().split())
visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
dm = [1, 2, 3]

visited[sy][sx][sd] = 1
q = deque()
q.append([sy, sx, sd, 0])

while q:
    [cy, cx, cd, cc] = q.popleft()

    if (cy, cx) == (ey, ex):
        if cd == ed:
            print(cc)
            break
        else:
            if cd // 2 == ed // 2:
                print(cc + 2)
                break
            else:
                print(cc + 1)
                break

    for i in range(4):
        for j in range(3):
            ny = cy + dy[i] * dm[j]
            nx = cx + dx[i] * dm[j]

            if nx >= 0 and nx < m and ny >= 0 and ny < n and graph[ny][nx] == 0:
                # 같은 방향을 바라보고 있을때
                if i == cd:
                     if visited[ny][nx][cd] == 0:
                       visited[ny][nx][cd] = 1
                       q.append([ny, nx, cd, cc + 1])
                # 다른 방향을 바라보고 있을때
                else:
                    nd = i
                    if visited[ny][nx][nd] == 0:
                        visited[ny][nx][nd] = 1

                        # 2 만큼 회전
                        if i // 2 == cd // 2:
                            q.append([ny, nx, nd, cc + 3])
                        else:
                            q.append([ny, nx, nd, cc + 2])
            else:
                break