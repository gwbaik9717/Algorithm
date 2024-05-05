from collections import deque

def solution(board):
    answer = 0
    h = len(board)
    w = len(board[0])
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'R':
                sy, sx = i, j
    
    visited = [[0] * w for _ in range(h)]
    q = deque()
    q.append((sy, sx, 0))
    
    while q:
        cy, cx, cc = q.popleft()
        
        if board[cy][cx] == 'G':
            answer = cc
            break
        
        for i in range(4):
            ny, nx = cy, cx
            nc = cc + 1
            
            while True:
                py, px = ny, nx
                ny, nx = ny + dy[i], nx + dx[i]
                

                if 0 <= nx < w and 0 <= ny < h and board[ny][nx] != 'D':
                    continue
                else:
                    if (cy, cx) != (py, px) and visited[py][px] == 0:
                        visited[py][px] = 1
                        q.append([py, px, nc])
                    break
    else:
        answer = -1
                    
    
    return answer