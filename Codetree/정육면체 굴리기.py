import sys

n, m, y, x, k = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dirs = map(int, sys.stdin.readline().strip().split())
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

dice = [0] * 6

def rotate(dir):
    global dice

    new_dice = []
    rv = [0] * 6

    # [동, 서, 북, 남]
    if dir == 0:
        new_dice = [1, 5, 2, 3, 0, 4]
    elif dir == 1:
        new_dice = [4, 0, 2, 3, 5, 1]
    elif dir == 2:
        new_dice = [3, 1, 0, 5, 4, 2]
    else:
        new_dice = [2, 1, 5, 0, 4, 3]

    for i, nd in enumerate(new_dice):
        rv[nd] = dice[i]
    
    dice = rv

def change(position):
    global dice

    cy, cx = position

    if graph[cy][cx] == 0:
        graph[cy][cx] = dice[5]
    else:
        dice[5] = graph[cy][cx]
        graph[cy][cx] = 0

cy, cx = y, x

for dir in dirs:
    ny, nx = cy + dy[dir - 1], cx + dx[dir - 1]

    if 0 <= ny < n and 0 <= nx < m:
        cy, cx = ny, nx
        rotate(dir - 1)
        change((cy, cx))
        print(dice[0])
 