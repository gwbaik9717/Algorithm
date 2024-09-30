import sys
from collections import deque
from copy import deepcopy

n = 5

k, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)]

wall = deque(map(int, sys.stdin.readline().strip().split()))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# 배열의 특정 부분(정사각형)을 회전시킴
def rotate_90(sy, sx, length, arr):
    
    new_arr = deepcopy(arr)

    # 정사각형을 시계방향으로 90도 회전
    for y in range(sy, sy + length):
        for x in range(sx, sx + length):
            # 1단계 : (0,0)으로 옮겨주는 변환을 진행함
            oy, ox = y - sy, x - sx
            # 2단계 : 90도 회전했을때의 좌표를 구함
            ry, rx = ox, length - oy - 1
            # 3단계 : 다시 (sy,sx)를 더해줌
            new_arr[sy + ry][sx + rx] = arr[y][x]

    # new_arr 값을 현재 board에 옮겨줌
    for y in range(sy, sy + length):
        for x in range(sx, sx + length):
            arr[y][x] = new_arr[y][x]

def get_relics(graph):
    checked = [[0] * n for _ in range(n)]
    relics = [[0] * n for _ in range(n)]
    
    def bfs(start):
        
        q = deque()
        sy, sx = start
        
        checked[sy][sx] = 1
        candidates = []

        q.append(start)
        candidates.append(start)

        while q:
            cy, cx = q.popleft()

            for zipped in zip(dy, dx):
                ny, nx = cy + zipped[0], cx + zipped[1]

                if 0 <= ny < n and 0 <= nx < n and checked[ny][nx] == 0 and graph[ny][nx] == graph[sy][sx]:
                    q.append((ny, nx))
                    candidates.append((ny, nx))
                    checked[ny][nx] = 1
        
        if len(candidates) >= 3: 
            for candidate in candidates:
                relics[candidate[0]][candidate[1]] = 1
        
    for i in range(n):
        for j in range(n):
            if checked[i][j] == 0:
                bfs((i, j))
    
    return relics, sum([sum(row) for row in relics])

def rotate():
    start, deg, ans, relics = None, 0, -1, None

    rotated = [[deepcopy(graph) for _ in range(n-2)] for _ in range(n-2)]

    for k in range(1, 4):
        
        for j in range(n-2): 
            for i in range(n-2):

                rotate_90(i, j, 3, rotated[i][j])
                relics, cnt_relics = get_relics(rotated[i][j])

                if cnt_relics > ans:
                    start, deg, ans, relics = (i, j), k, cnt_relics, relics

    if ans == 0: 
        return ans

    for i in range(deg):
        rotate_90(start[0], start[1], 3, graph)
    
    return ans

ans = []

for _ in range(k):
    cnt = 0

    rv = rotate()

    if rv == 0:
        break

    while True:
        relics, cnt_relics = get_relics(graph=graph)

        cnt += cnt_relics

        if cnt_relics == 0:
            break

        for j in range(n):
            for i in range(n-1, -1, -1):
                if relics[i][j] == 1:
                    graph[i][j] = wall.popleft()
    
    ans.append(cnt)

print(" ".join(map(str, ans)))    