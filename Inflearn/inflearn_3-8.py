import math
sample = """5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3
2 0 3
5 1 2
3 1 4"""

inputs = sample.split("\n")
n = int(inputs[0])
graph = list(map(lambda x : list(map(int, x.split(" "))), inputs[1: 1+n]))
orders = map(lambda x : list(map(int, x.split(" "))), inputs[2+n:])


for order in orders:
    [row, dir, dist] = order
    nr = [0 for x in range(n)]
  
    for i, item in enumerate(graph[row - 1]):
        if dir == 0:
            # 왼쪽
            nr[(i - dist) % n] = item
        else:
            # 오른쪽
            nr[(i + dist) % n] = item
    graph[row - 1] = nr

ans = 0

for i in range(n // 2 + 1):
    row = graph[i]

    if i == n // 2:
        ans += row[n // 2]
    else:
        ans += sum(row[i: n-i])
        ans += sum(graph[n-1-i][i: n-i])

print(ans)