def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    to_deliver = 0
    to_pick = 0 

    for i in range(n):
        to_deliver += deliveries[i]
        to_pick += pickups[i]
        
        while to_deliver > 0 or to_pick > 0: 
            to_deliver -= cap
            to_pick -= cap
            
            answer += (n - i) * 2
    
    
    return answer