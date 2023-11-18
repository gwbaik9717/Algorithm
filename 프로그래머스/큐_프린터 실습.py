from collections import deque

def solution(priorities, location):
    answer = 0
    i = 0
    
    np = deque(enumerate(priorities))
    
    std = sorted(priorities, key=lambda x: -x)
    
    while i < len(priorities):
        if std[i] == np[0][1]:
            if location == np[0][0]:
                return i + 1
            
            i += 1
            
        np.append(np.popleft())
    
    return answer