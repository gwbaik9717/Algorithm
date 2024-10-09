import sys
sys.setrecursionlimit(1000000)
n, m = map(int, sys.stdin.readline().strip().split())
parent = [i for i in range(n + 1)]
commands = [map(int, sys.stdin.readline().strip().split()) for _ in range(m)]

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


for command in commands:

    t, a, b = command

    # union
    if t == 0:
        union(a, b, parent)
    
    elif t == 1:
        if get_parent(a, parent) == get_parent(b, parent):
            print("YES")
        else:
            print("NO")