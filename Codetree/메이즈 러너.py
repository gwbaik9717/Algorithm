import sys
from copy import deepcopy

n, m, k = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
players = [list(map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())) for _ in range(m)]
ey, ex = map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())

ans = 0

# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 출구 표시
graph[ey][ex] = -1

def find_exit():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == -1:
                return (i, j)

def rotate_90(start, size):
    global graph

    sy, sx = start
    cloned_graph = deepcopy(graph)

    for i in range(sy,  sy+size):
        for j in range(sx, sx+size):
            # (0, 0) 을 기준으로 이동
            oy, ox = i - sy, j - sx 

            # 시계방향으로 90도 회전
            ry, rx = ox, size - 1 - oy

            # 원상 복귀
            ny, nx = ry + sy, rx + sx

            if graph[i][j] > 0:
                # 벽 내구도 감소
                cloned_graph[ny][nx] = graph[i][j] - 1
            else:
                cloned_graph[ny][nx] = graph[i][j]
    
    # players 중 만약 해당 범위에 있는 player 가 있다면 회전
    for i, player in enumerate(players):
        py, px = player

        if sy <= py < sy + size and sx <= px < sx + size:
            oy, ox = py - sy, px - sx 

            # 시계방향으로 90도 회전
            ry, rx = ox, size - 1 - oy

            # 원상 복귀
            ny, nx = ry + sy, rx + sx

            players[i] = [ny, nx]

    graph = cloned_graph

def get_exit_dist(a):
    ay, ax = a
    ey, ex = find_exit()

    return abs(ay - ey) + abs(ax - ex)

def move_players():

    global ans

    to_remove = []

    for i, player in enumerate(players):
        py, px = player
        pd = get_exit_dist(player)

    
        for zipped in zip(dy, dx):
            ny, nx = py + zipped[0], px + zipped[1]

            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] < 1:
                nd = get_exit_dist((ny, nx))

                # 출구까지 최단거리가 더 가까울 때만 움직임
                if nd < pd:
                    ans += 1

                    # 출구일때는 바로 삭제
                    if graph[ny][nx] == -1:
                        to_remove.append(player)
                        break

                    players[i] = [ny, nx]
                    break

    for r in to_remove:
        players.remove(r)

def find_square():

    ey, ex = find_exit()
    
    for k in range(2, n + 1):
        for r in range(n-k+1):
            for c in range(n-k+1):

                # exit 좌표가 범위에 있는지 확인
                if r <= ey < r + k and c <= ex < c + k:
                    
                    # player 좌표가 범위에 있는지 확인
                    for player in players:
                        py, px = player

                        if r <= py < r + k and c <= px < c + k:
                            return (r, c, k)
    
    return False

for _ in range(k):

    move_players()
    square = find_square()

    if len(players) == 0:
        break

    r, c, size = square
    rotate_90((r, c), size)

print(ans)
print(" ".join(map(lambda x: str(x + 1), find_exit())))
