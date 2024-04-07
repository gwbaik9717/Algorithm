import sys
n, k = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for _ in range(n)]
coins.sort()

# 메모리 제한으로 1차원 배열로 변경
dp = [0] * (k + 1)
dp[0] = 1

for c in coins:
    for i in range(c, k + 1):
        dp[i] += dp[i - c]

print(dp[k])