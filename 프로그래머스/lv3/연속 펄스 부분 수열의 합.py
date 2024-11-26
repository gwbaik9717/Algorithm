def solution(sequence):
    answer = -1e9
    n = len(sequence)
    
    for i in range(2):
        cloned_sequence = sequence[:]
        
        if i == 0:
            cloned_sequence = [-s if i%2 == 0 else s for i, s in enumerate(sequence)]
        else:
            cloned_sequence = [s if i%2 == 0 else -s for i, s in enumerate(sequence)]
        
        dp = [0] * n
        dp[0] = cloned_sequence[0]
        answer = max(answer, dp[0])
        
        for i in range(1, n):
            dp[i] = max(cloned_sequence[i] + dp[i-1], cloned_sequence[i])
            if dp[i] > answer: 
                answer = dp[i]
        
    return answer