import sys
from collections import deque

temp = [list(sys.stdin.readline()) for _ in range(12)]
ans = 0

# graph 90도 회전
graph = [['.' for _ in range(12)] for _ in range(6)]
for i in range(12):
    for j in range(6):
        graph[j][i] = temp[i][j]

def bfs(start):
    checked = [[0] * 12 for _ in range(6)]
    q = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q.append(start)
    checked[start[0]][start[1]] = 1

    while q:
        [cy, cx] = q.popleft()
      
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx >= 0 and nx < 12 and ny >= 0 and ny < 6 and checked[ny][nx] == 0 and graph[ny][nx] == graph[cy][cx]:
                checked[ny][nx] = 1
                q.append([ny, nx])

    
    totalSum = sum(list(map(lambda x: sum(x), checked)))
    
    if totalSum >= 4:
        for i in range(6):
            for j in range(12):
                if checked[i][j] == 1:
                    graph[i][j] = '.' 
        return 1
    return 0

while True:
    temp = 0
    for i in range(6):
        for j in range(12):
            if graph[i][j] != '.':
                temp = max(temp, bfs([i, j]))

    ans += temp

    if temp == 0:
        break
    
    # rearrange
    for i in range(6):
        filtered = list(filter(lambda x: x != '.', graph[i]))
        filtered = ['.'] * (12 - len(filtered)) + filtered
        graph[i] = filtered

print(ans)