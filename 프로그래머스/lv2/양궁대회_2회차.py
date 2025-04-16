def solution(n, info):
    answer = []
    arr = list(map(lambda x: x+1, info))
    
    def get_diff(info, status):
        score_a = 0
        score_r = 0
        
        for i in range(11):
            if info[i] == 0 and status[i] == 0:
                continue
            
            if info[i] >= status[i]:
                score_a += (10-i)
            else:
                score_r += (10-i)
                
        return score_r - score_a
    
    def compare(a, b):
        for i in range(10, -1, -1):  # 낮은 점수부터 오른쪽에서 왼쪽으로 비교
            if a[i] > b[i]:
                return True
            elif a[i] < b[i]:
                return False
            
        return False
            

    candidate = None 
    max_diff = -1
    
    def dfs(i, status, cnt, score):
        nonlocal max_diff, candidate
        
        if cnt > n:
            return
        
        if i == 10:
            diff = get_diff(info, status)
       
            if diff > 0:
                if diff > max_diff: 
                    max_diff = diff
                    candidate = status[:]
                    return
                
                if diff == max_diff and compare(status, candidate):
                    candidate = status[:]
                
            return

        
        status[i] = arr[i]
        dfs(i+1, status, cnt + arr[i], 10 - i + score)
        
        status[i] = 0
        dfs(i+1, status, cnt, score)
    
    dfs(0, [0 for _ in range(11)], 0, 0)
    
    
    if candidate == None:
        return [-1]
    
    sum_candidate = sum(candidate)
    if sum_candidate < n:
        candidate[-1] += n - sum_candidate 
    
    return candidate