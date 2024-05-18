from itertools import permutations
from copy import deepcopy
import sys

INF = sys.maxsize
input = sys.stdin.readline
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
answer = INF

n, m, k = map(int, input().strip().split())

graph = [list(map(int, input().strip().split())) for _ in range(n)]
orders = [list(map(int, input().strip().split())) for _ in range(k)]

permus = permutations(orders, k)

def count(cloned_graph):
    total = INF
    for row in cloned_graph:
        total = min(total, sum(row))
    return total
        

for permu in permus:
    cloned_graph = deepcopy(graph)
    temp_graph = deepcopy(graph)

    for order in permu:  
        r, c, s = order
        cs = (r-s-1, c-s-1)

        for i in range(s):
            cs = (cs[0] + i, cs[1] + i)
       
            for ddy, ddx in zip(dy, dx):
                 for j in range(2 * (s - i)):
                    ns = (cs[0] + ddy, cs[1] + ddx)
                    cloned_graph[ns[0]][ns[1]] = temp_graph[cs[0]][cs[1]]
                    cs = ns
            
        temp_graph = deepcopy(cloned_graph)
    answer = min(answer, count(cloned_graph))
    

print(answer)