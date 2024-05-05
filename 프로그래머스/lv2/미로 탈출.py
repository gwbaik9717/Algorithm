from collections import deque

def solution(maps):
    answer = 0
    h = len(maps)
    w = len(maps[0])
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'S':
                sy, sx = i, j
                break
        else: 
            continue
        break
    
    
    def bfs(sy, sx, target):
        visited = [[0] * w for _ in range(h)]
        q = deque()
        q.append((sy, sx, 0))
        visited[sy][sx] = 1
        ry, rx, rc = 0, 0, -1
        
        while q:
            cy, cx, cc = q.popleft()
            
            if maps[cy][cx] == target:
                ry, rx, rc = cy, cx, cc
                break
            
            for ddy, ddx in zip(dy, dx):
                ny = cy + ddy
                nx = cx + ddx 
                nc = cc + 1
                
                if 0 <= nx < w and 0 <= ny < h and maps[ny][nx] != 'X' and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny, nx, nc))
        return (ry, rx, rc)
    
    ly, lx, lc = bfs(sy, sx, 'L')
    
    if lc == -1:
        return -1
    else:
        ey, ex, ec = bfs(ly, lx, 'E')
        
        if ec == -1:
            return -1
        else:
            answer = lc + ec
    
    return answer