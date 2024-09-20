import sys 
from itertools import combinations
from copy import deepcopy
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

walls = []
fires = []
candidates = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            candidates.append((i, j))
        elif graph[i][j] == 2:
            fires.append((i, j))
        else:
            walls.append((i, j))


combis = combinations(candidates, 3)

def get_safe_area(new_walls):

    new_graph = deepcopy(graph)

    for new_wall in new_walls:
        ny, nx = new_wall
        new_graph[ny][nx] = 1
    
  
    q = deque()
    q.extend(fires)

    while q:
        cy, cx = q.popleft()

        for zipped in zip(dy, dx):
            ny, nx = cy + zipped[0], cx + zipped[1]

            if 0 <= ny < n and 0 <= nx < m and new_graph[ny][nx] == 0:
                new_graph[ny][nx] = 2
                q.append((ny, nx))
    
    cnt = 0

    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 0:
                cnt += 1

    return cnt

answer = -1e9

for combi in combis:
    answer = max(answer, get_safe_area(combi))

print(answer)