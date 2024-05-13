import math

def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        temp = 0
        for j in range(1, int(math.sqrt(i)) + 1):
            if j < i and i % j == 0: 
                temp = max(temp, j)
                
                if i / j < min(10000001, i):
                    temp = max(temp, i / j)
        answer.append(temp)
                
    return answer