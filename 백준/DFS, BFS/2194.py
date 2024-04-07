import sys
from collections import deque

n, m, a, b, k = map(int, sys.stdin.readline().strip().split())
blockers = [list(map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())) for _ in range(k)]
sy, sx = map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())
ey, ex = map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 동 서 남 북
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 시작, 끝 표시
for i in range(ey, ey + a):
    for j in range(ex, ex + b):
        graph[i][j] = 2

for i in range(sy, sy + a):
    for j in range(sx, sx + b):
        graph[i][j] = 2

# 장애물 표시
for [by, bx] in blockers:
    graph[by][bx] = 1

def check_move(cy, cx):
    flag = False

    if cy + a > n or cx + b > m:
        return False

    for i in range(cy, cy + a):
        for j in range(cx, cx + b):
            # 장애물이 있을 경우
            if graph[i][j] == 1:
              
                return False
            
            if visited[i][j] == 0:
                flag = True
    
    # 이미 방문한 유닛인 경우
    if not flag:
        return False
    return True
                
def visit(cy, cx):
    for i in range(cy, cy + a):
        for j in range(cx, cx + b):
            visited[i][j] = 1

def is_arrived(cy, cx):
    if (cy, cx) == (sy, sx):
        return False

    for i in range(cy, cy + a):
        for j in range(cx, cx + b):
            if graph[i][j] != 2:
                return False
    return True

q = deque()
q.append([sy, sx, 0])
visit(sy, sx)

while q:
    [cy, cx, cd] = q.popleft()

    if is_arrived(cy, cx):
        print(cd)
        break

    for i in range(len(dx)):
        ny = cy + dy[i]
        nx = cx + dx[i]
        nd = cd + 1

        if nx >= 0 and nx < m and ny >= 0 and ny < n and check_move(ny, nx):
            q.append([ny, nx, nd])
            visit(ny, nx)
else:
    print(-1)