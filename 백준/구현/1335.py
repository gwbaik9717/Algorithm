import sys
from collections import deque

input = sys.stdin.readline
answer = 1
n, w, l = map(int, input().strip().split())
trucks = deque(map(int, input().strip().split()))
bridge = deque()

truck = trucks.popleft()
bridge.append([truck, w])

while len(trucks) > 0 or len(bridge) > 0:
    for car in bridge:
        car[1] -= 1
    
    if bridge and bridge[0][1] == 0:
        bridge.popleft()
        
    if trucks and trucks[0] + sum(map(lambda x: x[0], bridge)) <= l:
        truck = trucks.popleft()
        bridge.append([truck, w])    
    
    answer += 1

print(answer)