import sys

n = int(sys.stdin.readline().strip())
matrixes = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for cnt in range(n-1):
    for i in range(n-1-cnt):

        j = i + cnt + 1
        dp[i][j] = 2 ** 31

        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrixes[i][0]*matrixes[k][1]*matrixes[j][1])

print(dp[0][-1])