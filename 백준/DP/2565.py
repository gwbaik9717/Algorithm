import sys

n = int(sys.stdin.readline().strip())
lines = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

lines.sort(key= lambda x: x[0])

dp = [1] * n

for i in range(n):
    for j in range(i):
        if lines[i][0] > lines[j][0] and lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))