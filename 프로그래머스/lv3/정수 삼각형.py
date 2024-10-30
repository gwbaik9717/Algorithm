from copy import deepcopy

def solution(triangle):
    answer = 0
    h = len(triangle)
    dp = deepcopy(triangle)
    
    for i in range(1, h):
        for j in range(i+1):
            candidates = [(i-1, j), (i-1, j-1)]
            
            max_candidate = -1
            for cy, cx in candidates:
                if 0 <= cx <= cy:
                    max_candidate = max(max_candidate, dp[cy][cx])
            
            dp[i][j] += max_candidate
    
    answer = max(dp[-1])
    
    return answer