import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

num_virus = 0
hospitals = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            hospitals.append([i, j])
        elif graph[i][j] == 0:
            num_virus += 1



def combi(arr, n):

    if n == 1:
        return [[item] for item in arr]
    
    rv = []

    for i, fixed in enumerate(arr):
        sliced = arr[i+1:]
        temp = map(lambda x: [fixed] + x, combi(sliced, n-1))
        rv.extend(temp)
    
    return rv

if num_virus == 0:
    print(0)
    exit()

combis = combi(hospitals, m)
ans = 1e9

for combi in combis:
    checked = [[0] * n for _ in range(n)]
    remaining_virus = num_virus

    q = deque()

    for hospital in combi:
        q.append([*hospital, 1])
        checked[hospital[0]][hospital[1]] = 1
    
    while q:
        if remaining_virus == 0:
            ans = min(ans, max([max(row) for row in checked]) - 1)

        cy, cx, cd = q.popleft()

        for zipped in zip(dy, dx):
            ny = cy + zipped[0]
            nx = cx + zipped[1]
            nd = cd + 1
            
            if 0 <= ny < n and 0 <= nx < n and checked[ny][nx] == 0 and graph[ny][nx] != 1:
                if graph[ny][nx] == 0:
                    remaining_virus -= 1

                checked[ny][nx] = nd
                q.append([ny, nx, nd])
    
if ans == 1e9:
    ans = -1

print(ans)