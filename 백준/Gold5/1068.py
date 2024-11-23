import sys

n = int(sys.stdin.readline().strip())
parent = list(map(int, sys.stdin.readline().strip().split()))
degree = [0] * n
tree = [[] for _ in range (n)]
to_delete = int(sys.stdin.readline().strip())

for c, p in enumerate(parent):
    if p == -1:
        degree[c] += 1
        continue

    degree[p] += 1
    degree[c] += 1

    tree[p].append(c)

def remove(node):
    global tree
    
    p = parent[node]

    if p == -1:
       degree[node] -= 1
    else: 
        degree[p] -= 1

    def dfs(node):
        
        for child in tree[node]:
            dfs(child)
        
        degree[node] = 0
    
    dfs(node)

remove(to_delete)

print(len([d for d in degree if d == 1]))