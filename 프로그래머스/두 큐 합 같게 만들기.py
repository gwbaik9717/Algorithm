def solution(queue1, queue2):
    answer = 0
    max = len(queue1) * 2 
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    i, j = 0, 0
    
    while sum1 != sum2 and answer < max * 2:
        if sum1 > sum2:
            sum1 -= queue1[i]
            sum2 += queue1[i]
            
            queue2.append(queue1[i])
            i += 1
        else:
            sum2 -= queue2[j]
            sum1 += queue2[j]
            
            queue1.append(queue2[j])
            j += 1
            
        answer += 1
            
    if sum1 != sum2:
        answer = -1
        
    return answer