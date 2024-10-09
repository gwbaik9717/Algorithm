import sys

n = int(sys.stdin.readline().strip())
m = sys.stdin.readline()
roads = [map(int, sys.stdin.readline().strip().split()) for _ in range(n)]

plan = map(int, sys.stdin.readline().strip().split())
parent = [i for i in range(n+1)]

def get_parent(a, parent):
    if a == parent[a]:
        return a
    
    parent[a] = get_parent(parent[a], parent)

    return parent[a]


def union(a, b, parent):
    parent_a = get_parent(a, parent)
    parent_b = get_parent(b, parent)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

for i, road in enumerate(roads):
    for j, item in enumerate(road):
        if item == 1:
            union(i+1, j+1, parent)

for p in parent[1:]:
    get_parent(p, parent)
cp = [parent[p] for p in plan]

if all([c == cp[0] for c in cp]):
    print("YES")
else:
    print("NO")