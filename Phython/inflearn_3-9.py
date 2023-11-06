sample="""5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2"""

inputs = sample.split("\n")
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

n = int(inputs[0])
graph = list(map(lambda x: list(map(int, x.split(" "))), inputs[1:]))

ans = 0

for i in range(n):
    for j in range(n):
        flag = False

        for k in range(4):
            ny = i + dy[k]
            nx = j + dx[k]

            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] >= graph[i][j]:
                    flag = True
                    break
        if not flag:
            ans += 1

print(ans)