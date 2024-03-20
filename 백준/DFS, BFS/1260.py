import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = [list() for _ in range(n + 1)]
for line in lines:
    [start, end] = line
    graph[start].append(end)
    graph[end].append(start)

for arr in graph:
    arr.sort()

checked = [False for _ in range(n + 1)]
dfsPath = []
bfsPath = []

def dfs(start):
    checked[start] = True
    dfsPath.append(start)

    for next in graph[start]:
        if not checked[next]:
            dfs(next)

def bfs(start):
    q = deque()
    q.append(start)
    checked = [False for _ in range(n + 1)]
    checked[start] = True

    while q:
        curr = q.popleft()
        bfsPath.append(curr)

        for next in graph[curr]:
            if not checked[next]:
                checked[next] = True
                q.append(next)
            
        
    
dfs(v)
bfs(v)

print(' '.join(str(num) for num in dfsPath))
print(' '.join(str(num) for num in bfsPath))
