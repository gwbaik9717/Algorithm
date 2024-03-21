import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

graph = [[] for _ in range(n + 1)]
checked = [0 for _ in range(n + 1)]

for [start, end] in lines:
    graph[start].append(end)
    graph[end].append(start)

q = deque()
q.append(1)
checked[1] = 1

while q:
    curr = q.popleft()

    for next in graph[curr]:
        if checked[next] == 0:
            q.append(next)
            checked[next] = 1

print(sum(checked) - 1)