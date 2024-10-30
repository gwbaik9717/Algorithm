def solution(m, n, puddles):
    answer = 0
    graph = [[0] * m for _ in range(n)]
    
    for px, py in puddles:
        graph[py-1][px-1] = -1
    
    graph[0][0] = 1
    
    dy = [-1, 0]
    dx = [0, -1]
    
    for i in range(n):
        for j in range(m):
            
            if graph[i][j] == -1:
                continue
            
            for zipped in zip(dy, dx):
                zy, zx = zipped
                oy, ox = i + zy, j + zx
                
                if 0 <= oy < n and 0 <= ox < m and graph[oy][ox] != -1:
                    graph[i][j] += (graph[oy][ox] % 1000000007)
    
    answer = graph[-1][-1] % 1000000007
    
    return answer 