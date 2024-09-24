import sys
from collections import Counter

r, c, k = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(3)]

new_graph = [[0] * 100 for _ in range(100)]

for i in range(3):
    for j in range(3):
        new_graph[i][j] = graph[i][j]

def sort_row(i, row, temp_graph):
    counter = Counter([item for item in row if item != 0])
    sorted_row = sorted(counter.items(), key=lambda item: (item[1], item[0]))

    rv = []
    for item in sorted_row:
        rv.extend(item)
    
    for j, val in enumerate(rv):
        if j >= 100:
            break

        temp_graph[i][j] = val

def sort_column(i, col, temp_graph):
    counter = Counter([item for item in col if item != 0])
    sorted_col = sorted(counter.items(), key=lambda item: (item[1], item[0]))

    rv = []
    for item in sorted_col:
        rv.extend(item)
    
    for j, val in enumerate(rv):
        if j >= 100:
            break

        temp_graph[j][i] = val
    
def round(height, width):

    global new_graph

    temp_graph = [[0] * 100 for _ in range(100)]

    # 행 >= 열
    if height >= width:
        for i in range(height):
            sort_row(i, new_graph[i], temp_graph)

    # 행 < 열
    else:
        for j in range(width):
            sort_column(j, [new_graph[i][j] for i in range(height)], temp_graph)
    
    new_graph = temp_graph

ans = 0

while True:
    if new_graph[r-1][c-1] == k:
        break

    if ans > 100:
        ans = -1
        break
    
    max_width = max(sum(1 for col in row if col != 0) for row in new_graph)
    max_height = max(sum(1 for row in new_graph if row[col] != 0) for col in range(len(new_graph[0])))

    round(max_height, max_width)

    ans += 1


print(ans)
