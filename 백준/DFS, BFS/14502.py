import sys
from itertools import combinations
from copy import deepcopy
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


empty_spaces = []
viruses = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty_spaces.append((i, j))
        elif graph[i][j] == 2:
            viruses.append((i, j))

combis = combinations(empty_spaces, 3)

def spread_virus(start, cloned):
    q = deque()
    q.append(start)

    while q:
        (cy, cx) = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= nx < m and 0 <= ny < n and cloned[ny][nx] == 0:
                cloned[ny][nx] = 2
                q.append((ny, nx))

def get_safe_area(cloned):
    area = 0

    for i in range(n):
        for j in range(m):
            if cloned[i][j] == 0:
                area += 1
    
    return area

ans = 0

for combi in combis:
    cloned = deepcopy(graph)

    for (wi, wj) in combi:
        cloned[wi][wj] = 1
    
    for virus in viruses:
        spread_virus(virus, cloned)
    
    ans = max(ans, get_safe_area(cloned))

print(ans)