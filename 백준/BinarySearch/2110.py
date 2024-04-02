import sys
n, c = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline().strip()) for _ in range(n)]
houses.sort()

left = 1
right = houses[-1] - houses[0]
mid = (left + right) // 2

while left <= right:
    cnt = 1 
    cur = houses[0]
    for i in range(1, len(houses)):
        if houses[i] - cur >= mid:
            cur = houses[i]
            cnt += 1
    
    if cnt >= c:
        left = mid + 1
    else:
        right = mid - 1
    
    mid = (left + right) // 2

print(right)