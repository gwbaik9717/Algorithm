import sys
from collections import deque

answer = 0

dy = [1, 0, -1, 0, 1, 1, -1, -1]
dx = [0, 1, 0, -1, 1, -1, 1, -1]

while True:
    input = sys.stdin.readline().strip()
    
    if input == "0 0":
        break

    width, height = map(int, input.split())

    board = [sys.stdin.readline().strip().split() for _ in range(height)]
    checked = [[0] * width for _ in range(height)]

    def bfs(sy,sx):
      q = deque()
      q.append((sy, sx))

      checked[sy][sx] = 1

      while q:
         cy, cx = q.popleft()

         for ddy, ddx in zip(dy, dx):
             ny = cy + ddy 
             nx = cx + ddx

             if 0 <= nx < width and 0 <= ny < height and board[ny][nx] == "1" and checked[ny][nx] == 0:
                checked[ny][nx] = 1
                q.append((ny, nx))
    
    for i in range(height):
       for j in range(width):
          if board[i][j] == "1" and checked[i][j] == 0:
             answer += 1
             bfs(i, j)
    
    print(answer)