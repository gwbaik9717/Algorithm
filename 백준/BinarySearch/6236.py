import sys
n, m = map(int, sys.stdin.readline().split())
outs = [int(sys.stdin.readline().strip()) for _ in range(n)]

left = max(outs)
right = sum(outs)
mid = (left + right) // 2

while left <= right:
    cnt = 0
    remainder = 0
    for i, out in enumerate(outs):
        if remainder < out:
            remainder = mid - out
            cnt += 1
        else:
            remainder -= out
    
    if cnt <= m:
        right = mid - 1
    else:
        left = mid + 1         
    
    mid = (left + right) // 2

print(left)