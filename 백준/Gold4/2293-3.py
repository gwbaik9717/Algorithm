import sys
n, k = map(int, sys.stdin.readline().strip().split())
coins = [int(sys.stdin.readline().strip()) for _ in range(n)]

coins.sort()

dp = [1] + [0 for _ in range(k)]

for coin in coins:
    for amount in range(coin, k+1):
        dp[amount] += dp[amount - coin]

print(dp[k])