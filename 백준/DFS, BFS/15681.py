import sys
sys.setrecursionlimit(10**9)

n, r, q = map(int, sys.stdin.readline().strip().split())
lines = [map(int, sys.stdin.readline().strip().split()) for _ in range(n - 1)]
us = [int(sys.stdin.readline().strip()) for _ in range(q)]

tree = [[] for _ in range(n + 1)]

for (start, end) in lines:
    tree[start].append(end)
    tree[end].append(start)

new_tree = [[] for _ in range(n + 1)]
new_tree_cnts = [0] * (n + 1)

def make_tree(current, parent):
    for node in tree[current]:
        if node != parent:
            new_tree[current].append(node)
            make_tree(node, current)

def count_subtree(current):
    cnt = 1

    for node in new_tree[current]:
        cnt += count_subtree(node)

    new_tree_cnts[current] = cnt

    return cnt
        

make_tree(r, -1)
count_subtree(r)
 

for u in us:
    print(new_tree_cnts[u])