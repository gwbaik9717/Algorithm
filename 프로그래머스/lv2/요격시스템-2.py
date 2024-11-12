from collections import deque

def solution(targets):
    answer = 1
    
    q = deque(sorted(targets))
    popped = q.popleft()
    head = popped
    
    while q:
        cs, ce = q.popleft()
        hs, he = head
        
        if cs < he:
            head = (max(cs, hs), min(ce, he))
        else:
            head =(cs, ce)
            answer += 1
        
    return answer