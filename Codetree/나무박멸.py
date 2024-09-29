import sys

n, m, k, c = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

def grow():
    global graph
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                cnt = 0
            
                for zipped in zip(dy, dx):
                    ny, nx = i + zipped[0], j + zipped[1]

                    if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] > 0:
                        cnt += 1
                
                graph[i][j] += cnt

def reproduce():
    global graph

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    diff_graph = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                candidates = []
            
                for zipped in zip(dy, dx):
                    ny, nx = i + zipped[0], j + zipped[1]

                    if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 0:
                        candidates.append((ny, nx))
                
                for candidate in candidates:
                    y, x = candidate

                    diff_graph[y][x] += graph[i][j] // len(candidates)
            
    
    for i in range(n):
        for j in range(n):
            graph[i][j] += diff_graph[i][j]

def kill():
    dy = [1, 1, -1, -1]
    dx = [1, -1, 1, -1]

    target, cnt = None, 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] <= 0:
                if 0 > cnt:
                    target, cnt = (i, j), 0
                continue

            else:
                total = graph[i][j]
                for zipped in zip(dy, dx):
                    for t in range(1, k + 1):
                        ny, nx = i + zipped[0] * t, j + zipped[1] * t
                        
                        if 0 <= ny < n and 0 <= nx < n:
                            if graph[ny][nx] >= 0:
                                total += graph[ny][nx]

                            if graph[ny][nx] <= 0:
                                break 
                    
                if total > cnt:
                    target, cnt = (i, j), total

    if target == None:
        print("e")           
                    
    recover()

    ty, tx = target

    if graph[ty][tx] == -1:
        return cnt
    
    graph[ty][tx] = -2 + (-1)*(c-1)

    if graph[ty][tx] == 0:    
        return cnt

    for zipped in zip(dy, dx):
        for t in range(1, k + 1):
            ny, nx = ty + zipped[0] * t, tx + zipped[1] * t

            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] >= 0:
                    graph[ny][nx] = -2 + (-1)*(c-1)

                if graph[ny][nx] <= 0:
                    break 
                
              
    return cnt   
    
def recover():
    global graph

    for i in range(n):
        for j in range(n):
            if graph[i][j] == -2:
                graph[i][j] = 0
            elif graph[i][j] < -1:
                graph[i][j] += 1

ans = 0
for _ in range(m):
    grow()
    reproduce()
    ans += kill()

print(ans)