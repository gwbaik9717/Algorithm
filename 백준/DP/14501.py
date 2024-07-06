import sys
n = int(sys.stdin.readline().strip())
answer = 0
dp = [0] * (n + 1)
schedule = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

for i in range(n):
    for j in range(i + schedule[i][0], n + 1):
        dp[j] = max(dp[j], dp[i] + schedule[i][1])

print(dp[-1])