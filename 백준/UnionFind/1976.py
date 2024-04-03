import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
plan = list(map(lambda x: int(x) - 1, sys.stdin.readline().strip().split()))

parent = [i for i in range(n)]

def get_parent(i, parent):
    if i != parent[i]:
        parent[i] = get_parent(parent[i], parent)
        return parent[i]
    
    return i

def union(a, b, parent):
    parent_a = get_parent(a, parent)
    parent_b = get_parent(b, parent)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

for i in range(n):
    for j in range(n):
        if i <= j and graph[i][j] == 1:
            union(i, j, parent)

for i in range(n):
    get_parent(i, parent)        

prev = plan[0]
for i in range(1, m):
    curr = plan[i]

    if parent[prev] != parent[curr]:
        print("NO")
        break
    else:
        prev = curr
else:
    print("YES")

    