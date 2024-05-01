from collections import deque

def solution(land):
    answer = 0
    h = len(land)
    w = len(land[0])
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    groups = [0]
    group_id = 1
    visited = [[0] * w for _ in range(h)]
    
    def bfs(start):
        q = deque()
        q.append(start)
        visited[start[0]][start[1]] = 1
        land[start[0]][start[1]] = group_id
        cnt = 0
        
        while q:
            cy, cx = q.popleft()
            cnt += 1
            
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                
                if 0 <= ny < h and 0 <= nx < w and land[ny][nx] != 0 and visited[ny][nx] == 0:
                    q.append((ny, nx))
                    land[ny][nx] = group_id
                    visited[ny][nx] = 1
        
        groups.append(cnt)
    
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and land[i][j] != 0:
                bfs((i, j))
                group_id += 1
    
    for j in range(w):
        nset = set()
        for i in range(h):
            nset.add(land[i][j])
        
        answer = max(answer, sum(map(lambda x: groups[x], nset)))

    
    return answer