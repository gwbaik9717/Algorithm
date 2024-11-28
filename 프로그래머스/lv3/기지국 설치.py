import math

def solution(n, stations, w):
    answer = 0
    start = 1
    cover = 2 * w + 1
    
    for station in stations:
        left, right = station - w, station + w
        
        if left <= start:
            start = right + 1
            continue
        
        answer += math.ceil((left - start) / cover)
        start = right + 1
    
    if start <= n:
        answer += math.ceil((n - start + 1) / cover)

    return answer