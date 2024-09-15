from itertools import combinations
import sys 

answer = 1e9
n, m = map(int, sys.stdin.readline().strip().split())
graph = [sys.stdin.readline().strip().split() for _ in range(n)]
hospitals = []
people = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '2':
            hospitals.append((i, j))
        elif graph[i][j] == '1':
            people.append((i, j))

combis = combinations(hospitals, m)

def get_dist(h_coord, p_coord):
    hy, hx = h_coord
    py, px = p_coord

    return abs(hx - px) + abs(hy - py)

def get_total_dist(combi):
    sum = 0
    for person in people:
        min_dist = 1e9

        for hospital in combi:
            min_dist = min(min_dist, get_dist(hospital, person))

        sum += min_dist
    
    return sum    

for combi in combis:
    answer = min(answer, get_total_dist(combi))

print(answer)