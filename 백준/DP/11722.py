import sys 

INF = sys.maxsize
n = int(sys.stdin.readline().strip())
items = [INF] + list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    current = items[i]

    for j in range(i):
        item = items[j]
        if item > current:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))