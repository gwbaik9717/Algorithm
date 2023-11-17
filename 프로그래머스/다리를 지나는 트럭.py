from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    i = 1
    bridge = deque()    
    bridge.append([truck_weights[0], bridge_length])
    
    while bridge:
        for b in bridge:
            b[1] = max(0, b[1] - 1)
            
        if bridge[0][1] == 0:
            bridge.popleft()
            
        currentSum = sum(map(lambda x: x[0], bridge))
        
        if i < len(truck_weights) and currentSum + truck_weights[i] <= weight and len(bridge) < bridge_length:
            bridge.append([truck_weights[i], bridge_length])
            i += 1
            
        answer += 1
        
    return answer + 1