import sys

INF = sys.maxsize
n = int(sys.stdin.readline().strip())

dp = [INF] * (n + 1)
dp[-1] = 0

for i in range(n, 1, -1):
    if i % 2 == 0:
        dp[int(i / 2)] = min(dp[int(i / 2)], dp[i] + 1)
    
    if i % 3 == 0:
        dp[int(i / 3)] = min(dp[int(i / 3)], dp[i] + 1)
    
    dp[i - 1] = min(dp[i - 1], dp[i] + 1)
    
print(dp[1])