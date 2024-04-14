import sys
n = int(sys.stdin.readline().strip())

dp = [0 for _ in range(n + 1)]

dp[0] = 1
dp[1] = 1

i = 0
while pow(2, i) <= n:
    for j in range(2, n + 1):
        if j  >= pow(2, i):
            dp[j] += dp[j - pow(2, i)]
    i += 1

print(dp[-1] % 1000000000)