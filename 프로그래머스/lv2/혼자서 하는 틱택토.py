def solution(board):
    global wo, wx
    
    # 조건 1  0 <= no - nx <= 1
    nx, no = 0, 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                no += 1
            elif board[i][j] == 'X':
                nx += 1
    
    if no - nx < 0 or no - nx > 1:
        return 0
    
    # 조건 2 
    dy = [1, 0, -1, 0, 1, -1, 1, -1]
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    
    wx, wo = 0, 0
    visited = [[0] * 3 for _ in range(3)]
    
    def cnt(sy, sx):
        global wo, wx
        
        cv = board[sy][sx]
        visited[sy][sx] = 1
        
        for ddy, ddx in zip(dy, dx):
            ny, nx = sy, sx
            for i in range(2):
                ny += ddy
                nx += ddx
                
                if 0 <= nx < 3 and 0 <= ny < 3 and board[ny][nx] == cv and visited[ny][nx] == 0:
                    continue
                else:
                    break
            else:
                if board[ny][nx] == 'O':
                    wo += 1
                elif board[ny][nx] == 'X':
                    wx += 1
                    
    for i in range(3):
        for j in range(3):
            cnt(i, j)
  
    if wo == 1 and nx == no:
        return 0
    if wx == 1 and no > nx:
        return 0
    return 1