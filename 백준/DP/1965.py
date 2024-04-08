import sys
n = int(sys.stdin.readline().strip())
boxes = list(map(int, sys.stdin.readline().strip().split()))
dp = [1] * n

for i in range(1, n):
    box = boxes[i]
    candidate = 0
    for j in range(i):
        if boxes[j] < box:
            candidate = max(candidate, dp[j])
    
    dp[i] = candidate + 1

print(max(dp))