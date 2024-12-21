import sys
n, m = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline().strip()) for _ in range(n)]

left = 1
right = max(lines)
mid = (left + right) // 2

while left <= right:
    cnt = sum(list(map(lambda line: line // mid, lines)))
    if cnt >= m:
        left = mid + 1
    else:
        right = mid - 1
    
    mid = (left + right) // 2

print(right)