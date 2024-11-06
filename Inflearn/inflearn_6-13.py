sample="""5 9
1 2
1 3
1 4
2 1
2 3
2 5
3 4
4 2
4 5"""

inputs = sample.split("\n")

[n, m] = map(int, inputs[0].split(" "))

lines = map(lambda x: list(map(int, x.split(" "))), inputs[1:])
graph = [[] for _ in range(n+1)]
checked = [0] * (n+1)

for line in lines:
    [start, end] = line
    graph[start].append(end)

ans = 0 

checked[1] = 1

def dfs(current, paths):
    global ans

    if current == n:
        ans += 1
    else:
        for next in graph[current]:
            if checked[next] == 0:
                checked[next] = 1
                dfs(next, [*paths, next])
                checked[next] = 0

dfs(1, [])
print(ans)