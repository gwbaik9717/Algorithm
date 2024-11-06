from collections import deque

sample="""0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 0
1 0 0 0 1 0 0
1 0 1 0 0 0 0"""

inputs = sample.split("\n")
graph = list(map(lambda x: list(map(int, x.split(" "))), inputs))
checked = [[0]*7 for _ in range(7)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque([[0, 0, 0]])
checked[0][0] = 1
ans = -1

while q:
    [cy, cx, cnt] = q.popleft()
    
    if cy == 6 and cx == 6:
        ans = cnt
        break

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        
        if 0 <= nx < 7 and 0 <= ny < 7 and checked[ny][nx] == 0 and graph[ny][nx] == 0:
            checked[ny][nx] = 1 
            q.append([ny, nx, cnt + 1])

print(ans)