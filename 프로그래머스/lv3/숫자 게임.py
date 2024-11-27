def solution(A, B):
    answer = 0
    
    sorted_a = sorted(A, reverse=True)
    sorted_b = sorted(B, reverse=True)
    
    n = len(A)
    
    i, j = 0, 0
    
    while i < n and j < n: 
        
        if sorted_b[j] > sorted_a[i]:
            answer += 1
            j += 1
        
        i += 1
    
    return answer