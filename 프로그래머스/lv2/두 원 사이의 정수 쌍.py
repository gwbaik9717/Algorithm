import math

def solution(r1, r2):
    answer = 0
    
    for i in range(1, r2 + 1):
        if i > r1:
            y1 = 0
        else:
            y1 = math.ceil(math.sqrt(r1 ** 2 - i ** 2))
        y2 = math.floor(math.sqrt(r2 ** 2 - i ** 2))
        
        answer += ((y2 - y1) + 1)
        
    answer *= 4
    
    return answer