import sys

n, m, k = map(int, sys.stdin.readline().strip().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    start, end, c = map(int, sys.stdin.readline().strip().split())
    if start < end:
        graph[start][end] = max(graph[start][end], c)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i, c in enumerate(graph[1]):
    dp[i][2] = c

for i in range(2, n+1):
    for j in range(3, m+1):
        for k in range(1, i):
            if graph[k][i] and dp[k][j-1]:
                dp[i][j] = max(dp[i][j], dp[k][j-1] + graph[k][i])

print(max(dp[-1]))