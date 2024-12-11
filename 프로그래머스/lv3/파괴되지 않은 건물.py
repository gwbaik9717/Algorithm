def solution(board, skills):
    answer = 0
    n = len(board)
    m = len(board[0])
    
    aggregated_sum = [[0] * (m + 1) for _ in range(n + 1)]
    
    for skill in skills:
        t, sy, sx, ey, ex, amount = skill
        
        if t == 1: 
            amount = -amount
        
        aggregated_sum[sy][sx] += amount
        aggregated_sum[ey+1][ex+1] += amount
        
        aggregated_sum[ey+1][sx] += -amount
        aggregated_sum[sy][ex+1] += -amount
        
    
    # calculate aggregated
    for i in range(n+1): 
        for j in range(1, m+1):
            # L -> R
            aggregated_sum[i][j] += aggregated_sum[i][j-1]
    
    for j in range(m+1): 
        for i in range(1, n+1):
            # U -> D
            aggregated_sum[i][j] += aggregated_sum[i-1][j]
    
    for i in range(n):
        for j in range(m):
            board[i][j] += aggregated_sum[i][j]
            
            if board[i][j] > 0:
                answer += 1
   
    return answer