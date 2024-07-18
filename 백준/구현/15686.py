import sys
from itertools import combinations

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().strip().split())
board = [sys.stdin.readline().strip().split() for _ in range(n)]
answer = INF

chickens = []
houses = []

def get_dist(candidate):
    rv = 0

    for house in houses:
        temp = INF

        for chicken in candidate:
            hy, hx = house 
            chy, chx = chicken

            temp = min(temp, abs(hy - chy) + abs(hx - chx))
            
        rv += temp
    
    return rv


for i in range(n):
    for j in range(n):
        if board[i][j] == '2':
            chickens.append((i, j))
        elif board[i][j] == '1':
            houses.append((i, j))

combis = combinations(chickens, m)

for combi in combis:
    answer = min(answer, get_dist(combi))
        
print(answer)