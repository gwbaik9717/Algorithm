def solution(targets):
    answer = 1
    sorted_targets = sorted(targets, key=lambda x: x[1])
    
    last_end = sorted_targets[0][1]
    
    for i in range(1, len(sorted_targets)):
        [start, end] = sorted_targets[i]
        
        if start >= last_end:
            answer += 1
            last_end = end
    
    return answer