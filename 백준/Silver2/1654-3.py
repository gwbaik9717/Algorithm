import sys

k, n = map(int, sys.stdin.readline().strip().split())
lines = [int(sys.stdin.readline().strip()) for _ in range(k)]

left, right = 1, max(lines)

def is_valid(length):
    return sum(map(lambda line : line // length, lines)) >= n

while left <= right:

    mid = (left + right) // 2
    
    if is_valid(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)
