import copy
sample="""5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19"""



graph = list(map(lambda x: list(map(int, x.split(" "))), sample.split("\n")[1:]))
psum = copy.deepcopy(graph)

for i in range(len(graph)):
    for j in range(1, len(graph[0])):
        psum[i][j] += psum[i][j-1]

for j in range(len(graph[0])):
    for i in range(1, len(graph)):
        psum[i][j] += psum[i-1][j]


candidates = []

candidates.append(psum[-1][0])
for i in range(1, len(graph[0])):
    candidates.append(psum[-1][i] - psum[-1][i-1])


candidates.append(psum[0][-1])
for i in range(1, len(graph[0])):
    candidates.append(psum[i][-1] - psum[i-1][-1])

sum1 = 0
sum2 = 0
for i in range(len(graph[0])):
    for j in range(len(graph[0])):
        if i == j:
            sum1 += graph[i][j]
        elif i + j == len(graph[0]) - 1:
            sum2 += graph[i][j]

candidates += [sum1, sum2]        
candidates.sort(reverse=True)

print(candidates[0])