def solution(diffs, times, limit):
    answer = 0
    
    left, right = 1, max(diffs)
    
    def check(lv):
        
        total = 0
        
        for i, diff in enumerate(diffs):
            if lv >= diff:
                total += times[i]
            else:
                total += (times[i-1] + times[i]) * (diff - lv) + times[i]
        

        return total <= limit
        
    
    while left <= right:
        
        mid = (left + right) // 2
       
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
        

    return left