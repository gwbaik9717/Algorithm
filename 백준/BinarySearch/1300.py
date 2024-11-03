import sys

n, k = map(int, [sys.stdin.readline().strip() for _ in range(2)])

def is_possible(candidate, k):
    ss = sum([min(n, candidate // i) for i in range(1, n+1)])
    
    if ss >= k:
        return True
    
    return False

left, right = 1, n**2

while left <= right:
    mid = (left + right) // 2
    
    if is_possible(mid, k):
        right = mid - 1
    else:
        left = mid + 1

print(left)