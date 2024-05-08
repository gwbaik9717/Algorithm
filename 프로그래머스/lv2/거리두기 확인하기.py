from collections import deque

def solution(places):
    answer = []
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    
    def bfs(sy, sx, graph):
        visited = [[0] * 5 for _ in range(5)]
        q = deque()
        q.append((sy, sx, 0))
        visited[sy][sx] = 1
        
        while q:
            cy, cx, cc = q.popleft()
            
            if cc > 2:
                break 
            
            if cc != 0 and graph[cy][cx] == 'P':
                return False
            
            for ddy, ddx in zip(dy, dx):
                ny = cy + ddy
                nx = cx + ddx
                nc = cc + 1
                
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0 and graph[ny][nx] != 'X':
                    visited[ny][nx] = 1
                    q.append((ny, nx, nc))
        return True
            
    
    for place in places:
        graph = list(map(lambda x: list(x), place))
        temp = 1
        for i in range(5):
            for j in range(5):
                if graph[i][j] == 'P':
                    if(not bfs(i, j, graph)):
                        temp = 0
        answer.append(temp)
                        
        
    return answer