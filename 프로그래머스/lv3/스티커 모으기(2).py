def solution(sticker):
    answer = 0
    n = len(sticker)
    
    # 첫번째 스티커를 뽑은 경우
    dp1 = [0] * (n+1)
    
    # 첫번째 스티커를 뽑지 않은 경우
    dp2 = [0] * (n+1)
    
    dp1[1] = sticker[0]
    dp2[1] = 0
    
    for i in range(2, n+1):
        if i == n:
            dp1[i] = dp1[i-1]
            break
            
        dp1[i] = max(dp1[i-2] + sticker[i-1], dp1[i-1])
    
    for i in range(2, n+1):
        dp2[i] = max(dp2[i-2] + sticker[i-1], dp2[i-1])
    
    answer = max(dp1[-1], dp2[-1])
    
    return answer