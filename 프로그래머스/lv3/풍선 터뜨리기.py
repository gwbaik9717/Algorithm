def solution(a):
    n = len(a)

    INF = 1e9
    dp = [[INF] * n for _ in range(2)]
    dp[0][0] = a[0]
    dp[1][-1] = a[-1]
    
    # -> 방향으로 최솟값 계산
    for i in range(1, n): 
        dp[0][i] = min(a[i], dp[0][i-1])
    
    # <- 방향으로 최솟값 계산
    for i in range(n-2, -1, -1): 
        dp[1][i] = min(a[i], dp[1][i+1])
    
    if n <= 2:
        return n
    
    answer = 2
    
    for i in range(1, n-1): 
        # 양쪽 모두 클 경우
        if dp[0][i-1] > a[i] and dp[1][i+1] > a[i]:
            answer += 1
            continue
        
        # 왼쪽 또는 오른쪽 한쪽만 클 경우
        if dp[0][i-1] > a[i] or dp[1][i+1] > a[i]:
            answer += 1
            continue  
    
    return answer