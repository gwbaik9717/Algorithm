import sys
from itertools import combinations
from collections import deque

a, b, c = map(int, sys.stdin.readline().strip().split())
sum = a + b + c
visited = [[0] * 2000 for _ in range(2000)]

q = deque()

nc = [a, b, c]
nc.sort()
visited[nc[0]][nc[1]] = 1

q.append(nc)

while q:
    ca, cb, cc = q.popleft()

    if ca == cb == cc:
        print(1)
        break

    combis = combinations([ca, cb, cc], 2)
    
    for combi in combis:
        listed = list(combi)
        listed.sort()

        [x, y] = listed

        if x < y: 
            nx = x * 2
            ny = y - x
            nz = sum - (nx + ny)

            nc = [nx, ny, nz]
            nc.sort()

            if visited[nc[0]][nc[1]] == 0:
                visited[nc[0]][nc[1]] = 1
                q.append(nc)
else:
    print(0)
