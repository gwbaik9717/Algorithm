import sys
from copy import deepcopy

n, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


total_moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
chess_dir = [[] for _ in range(6)]

def combi(arr, n, chess):
    if n == 1:
        return list(map(lambda x: [x], arr))

    rv = []

    for i, fixed in enumerate(arr):
        sliced = arr[i+1:]

        if chess == 2:
            sliced = [s for s in sliced if [s[0], s[-1]] == [(-1) * fixed[0], (-1) * fixed[1]]]
        elif chess == 3:
            sliced = [s for s in sliced if abs(s[0]) + abs(fixed[0]) == 1 and abs(s[1]) + abs(fixed[1]) == 1]

        temp = map(lambda x: [fixed] + x, combi(sliced, n-1, chess))

        rv.extend(temp)
    
    return rv

chess_dir[1] = combi(total_moves, 1, 1)
chess_dir[2] = combi(total_moves, 2, 2)
chess_dir[3] = combi(total_moves, 2, 3)
chess_dir[4] = combi(total_moves, 3, 4)
chess_dir[5] = combi(total_moves, 4, 5)

def count(graph):
    cnt = 0
    for i in range(n):
      for j in range(m):
          if graph[i][j] == 0:
              cnt += 1
    
    return cnt

def color(dirs, position, graph):
    cloned_graph = deepcopy(graph)
    cy, cx = position


    for dir in dirs:
        ny, nx = cy, cx

        while True:
            ny, nx = ny + dir[0], nx + dir[1]

            if ny < 0 or ny >= n or nx < 0 or nx >= m or cloned_graph[ny][nx] == 6:
                break    

            if cloned_graph[ny][nx] == 0:
                cloned_graph[ny][nx] = -1
    
    return cloned_graph


answer = 1e9

my_chess = []

for i in range(n):
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            my_chess.append((graph[i][j], (i, j)))

def dfs(lv, graph):
    global answer

    if lv >= len(my_chess):
        answer = min(answer, count(graph))
        return

    chess_num, chess_cord = my_chess[lv]
    

    for dir in chess_dir[chess_num]:
        colored_graph = color(dir, chess_cord, graph)
        dfs(lv + 1, colored_graph)

dfs(0, graph)

print(answer)