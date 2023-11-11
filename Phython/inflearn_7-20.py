from itertools import combinations

sample="""4 4
0 1 2 0
1 0 2 1
0 2 1 2
2 0 1 2"""

inputs = sample.split("\n")

[n, m] = map(int, inputs[0].split(" "))
graph = list(map(lambda x: list(map(int, x.split(" "))), inputs[1:]))

pizzas = []

def getMinDist(candidates):
    dist = 0
    for i, row in enumerate(graph):
        for j, col in enumerate(row):
            if col == 1:
                dist += min(map(lambda c: abs(c[0]-i) + abs(c[1]-j),candidates))
    return dist

    

for i, row in enumerate(graph):
    for j, col in enumerate(row):
        if col == 2:
            pizzas.append([i, j])

combis = combinations(pizzas, m)

ans = 100000

for combi in combis:
    ans = min(ans, getMinDist(combi))

print(ans)