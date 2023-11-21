import math
import sys

n,m = map(int, sys.stdin.readline().split())
rels = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

dists = [[math.inf for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dists[i][i] = 0

for [start, end] in rels:
    dists[start][end] = 1
    dists[end][start] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            nd = dists[j][i] + dists[i][k]
            dists[j][k] = min(nd, dists[j][k])

minimum, person = math.inf, 0


for i in range(1, n + 1):
    ns = sum(dists[i][1:])
    if ns < minimum:
        minimum, person = ns, i

print(person)