import sys
import math

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))



max_height = max(trees)
left = 0
right = max_height
mid = math.floor((left + right) / 2)

while left <= right:
    cnt = sum(map(lambda tree: max(0, tree - mid), trees))
   
    if cnt < m:
        right = mid - 1
    else:
        left = mid + 1
    
    mid = math.floor((left + right) / 2)

print(mid)