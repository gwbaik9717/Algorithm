import sys
sys.setrecursionlimit(1000000)
n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]
commands = [map(int, sys.stdin.readline().split()) for _ in range(m)]

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

for command in commands:
    cc, a, b = command

    if cc == 0:
        union(a, b, parent)
    else:
        comparison = get_parent(a, parent) == get_parent(b, parent)
        if comparison == True:
            print("yes")
        else:
            print("no")