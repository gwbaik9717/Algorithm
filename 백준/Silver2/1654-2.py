import sys

k, n = map(int, sys.stdin.readline().strip().split())
lines = [int(sys.stdin.readline().strip()) for _ in range(k)]

def is_possible(length, target):
    return sum([line // length for line in lines]) >= target

left, right = 1, max(lines)

while left <= right:
    mid = (left + right) // 2

    if is_possible(mid, n):
        left = mid + 1
    else:
        right = mid - 1

print(right)