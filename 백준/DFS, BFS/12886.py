import sys
from itertools import combinations
from collections import deque

a, b, c = map(int, sys.stdin.readline().strip().split())
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
        
        # leave last one
        candidates = [ca, cb, cc]
        for x in listed:
            candidates.remove(x)

        [x, y] = listed

        # add last one 
        if x < y: 
            nx = x * 2
            ny = y - x
            nz = candidates[-1]

            nc = [nx, ny, nz]
            nc.sort()

            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append(nc)
else:
    print(0)
