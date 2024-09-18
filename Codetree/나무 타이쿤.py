import sys

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [1, 1, 0, -1, -1, -1, 0, 1]

n, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
moves = [map(int, sys.stdin.readline().strip().split()) for _ in range(m)]

vitamins = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]

def move_vitamin(d, p):
    
    for i, vitamin in enumerate(vitamins):
        vy, vx = vitamin

        ny, nx = (vy + dy[d] * p) % n, (vx + dx[d] * p) % n

        vitamins[i] = [ny, nx]

def grow():

    for vitamin in vitamins:
        vy, vx = vitamin

        graph[vy][vx] += 1

    gy = [1, 1, -1, -1]
    gx = [-1, 1, 1, -1]
    
    for vitamin in vitamins:

        vy, vx = vitamin
        cnt = 0

        for zipped in zip(gy, gx):
            ny, nx = vy + zipped[0], vx + zipped[1]

            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] >= 1:
                cnt += 1
        
        graph[vy][vx] += cnt
        
def buy_vitamin():
    global vitamins

    new_vitamins = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and [i, j] not in vitamins:
                graph[i][j] -= 2
                new_vitamins.append([i, j])
    
    vitamins = new_vitamins

def get_total():
    return sum([sum(graph[i]) for i in range(n)])

for move in moves:
    d, p = move

    move_vitamin(d-1, p)
    grow()
    buy_vitamin()
    
print(get_total())