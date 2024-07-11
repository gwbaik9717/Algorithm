import sys

answer = 0

m, n = map(int, sys.stdin.readline().strip().split())
board = [sys.stdin.readline().strip().split() for _ in range(m)]

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if board[i-1][j-1] == "0":
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

answer = max(map(lambda row: max(row), dp))

print(answer)