import sys
n, m = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n)]
visited = [0] * n
lines = [map(int, sys.stdin.readline().strip().split()) for _ in range(m)]

for (start, end) in lines:
    graph[start].append(end)
    graph[end].append(start)

ans = 0

def dfs(lv, current):
    global ans

    if ans == 1:
        return
    
    if lv == 4:
        ans = 1
        return 
    
    for nn in graph[current]:
        if visited[nn] == 0:
            visited[nn] = 1
            dfs(lv + 1, nn)
            visited[nn] = 0

for i in range(n):
    visited[i] = 1 
    dfs(0, i)
    visited[i] = 0

print(ans)