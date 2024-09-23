import sys
from collections import deque

n, m, t = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

storms = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == -1:
            storms.append((i, j))           

def expand():
    diffs = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):

            if graph[i][j] == -1:
                continue

            for zipped in zip(dy, dx):
                ny, nx = i + zipped[0], j + zipped[1]

                if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in storms:
                    diff = graph[i][j] // 5
                    diffs[i][j] -= diff
                    diffs[ny][nx] += diff
    
    for i in range(n):
        for j in range(m):
            graph[i][j] += diffs[i][j]

    
def rotate(sy, dir, h):
    q = deque()

    q.extend(graph[sy])
    q.extend([row[-1] for row in graph[sy+1:sy+h]])
    q.extend(graph[sy+h-1][:-1][::-1])
    q.extend([row[0] for row in graph[sy+1:sy+h-1]][::-1])
    
    q.rotate(dir)
    
    for j in range(m):                 # 상
        graph[sy][j] = q.popleft()
    for j in range(sy+1, sy+h):             # 우
        graph[j][-1] = q.popleft()
    for j in range(m-2, -1, -1):         # 하
        graph[sy+h-1][j] = q.popleft()  
    for j in range(sy+h-2, sy, -1):           # 좌
        graph[j][0] = q.popleft()    


def init_storm():
    for storm in storms:
        graph[storm[0]][storm[1]] = 0

for i in range(t):
    expand()
    
    # 반시계
    init_storm()
    rotate(0, -1, storms[0][0] + 1)

    # 시계
    init_storm()
    rotate(storms[1][0], 1, n-storms[1][0])
    
    init_storm()

print(sum([sum(row) for row in graph]))