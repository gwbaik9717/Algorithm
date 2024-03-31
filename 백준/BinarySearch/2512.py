import sys
import math

n = int(sys.stdin.readline())
requests = list(map(int, sys.stdin.readline().split()))
total = int(sys.stdin.readline())

left = 1
right = max(requests)
mid = (left + right) // 2

while left <= right:
    cnt = sum(map(lambda request: min(request, mid), requests))

    if cnt <= total:
        left = mid + 1 
    else:
        right = mid - 1
    
    mid = (left + right) // 2

print(mid)