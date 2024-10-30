def solution(n, info):
    diff = 0
    answer = [-1]
    reversed_info = info[::-1]
    
    def get_diff(record):
        score_a, score_b = 0, 0
        
        
        for i, zipped in enumerate(zip(reversed_info, record)):
            a, b = zipped
            
            if a == b == 0:
                continue
            
            if a < b:
                score_b += i
            
            else:
                score_a += i
        
        return score_b - score_a
    
    
    def dfs(lv, total, record):
        nonlocal diff
        nonlocal answer
        
        if lv == len(info):
            current_diff = get_diff(record)
            
            if current_diff > diff:
                diff = current_diff
                answer = record
                
                if total < n:
                    answer[0] = n-total
            return
        
        for cost in [reversed_info[lv] + 1, 0]:
            
            new_cost = total + cost
            
            if new_cost <= n:
                new_record = record[:]
                new_record.append(cost)
                dfs(lv+1, new_cost, new_record)
    
    dfs(0, 0, [])
    
    answer = answer[::-1]
    
    return answer