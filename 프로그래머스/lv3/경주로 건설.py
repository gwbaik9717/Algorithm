from collections import deque

def solution(board):
    ans = 1e9
    n = len(board)
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    checked = [[[1e9] * 4 for _ in range(n)] for _ in range(n)]
    
    checked[0][0] = [-1] * 4
    q = deque()    
    q.append((0, 0, 0, None))
      
    while q:
        cy, cx, cc, cd = q.popleft()
        
        if cc >= ans:
            continue
        
        if (cy, cx) == (n-1, n-1):
            ans = min(ans, cc)
            continue
        
        for i, zipped in enumerate(zip(dy, dx)):
            zy, zx = zipped
            ny, nx, nc = cy + zy, cx + zx, cc
            
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                
                if cd == None:
                    nc += 100
                elif i != cd:
                    nc += 600
                else:
                    nc += 100
                    
                if nc >= checked[ny][nx][i]:
                    continue
                
                checked[ny][nx][i] = nc
                q.append((ny, nx, nc, i))
    
    return ans