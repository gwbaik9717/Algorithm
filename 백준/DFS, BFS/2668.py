import sys
from copy import deepcopy

n = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n+1)]
inputs = [int(sys.stdin.readline().strip()) for _ in range(n)]


for i, input in enumerate(inputs):
    graph[input].append(i + 1)


checked = [0] * (n + 1)
ans = []

def dfs(current, breadcrumb):
    checked[current] = 1
    breadcrumb.append(current)

    for j in graph[current]:
        if j not in breadcrumb:
            dfs(j, deepcopy(breadcrumb))
        else:
            ans.extend(breadcrumb)
            return

for i in range(1, n + 1):
    if checked[i] == 0:
        dfs(i, list())

print(len(ans))
ans.sort()
print('\n'.join(list(map(str, ans))))