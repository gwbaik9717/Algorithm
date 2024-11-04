def is_possible(n, stones, limit):
    stack = 0
    
    for stone in stones:
        if stone - n <= 0:
            stack += 1
            if stack >= limit:
                return False
        else:
            stack = 0  # Reset stack only when we encounter a non-zero stone
    
    return True

def solution(stones, k):
    left, right = 1, max(stones)  # Set right bound to max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        
        if is_possible(mid, stones, k):
            left = mid + 1
        else:
            right = mid - 1
    
    return left
