import sys
n, c = map(int, sys.stdin.readline().strip().split())
houses = [int(sys.stdin.readline().strip()) for _ in range(n)]

houses.sort()

def check(dist):    
    prev = 0 

    for _ in range(c-1):
        for j in range(prev+1, n):
            if houses[j] - houses[prev] >= dist:
                prev = j
                break
        else:
            return False
    
    return True

left, right = 0, 1000000000

while left <= right:
    mid = (left + right) // 2

    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
    
print(right)