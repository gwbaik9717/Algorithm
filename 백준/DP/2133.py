import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)

dp[2] = 3

for i in range(4, n+1):
    if i % 2 == 0:
        # 정상인 경우
        dp[i] += dp[i-2] * dp[2]

        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2 # dp[j]에 특수한 모양 2개의 조합

        dp[i] += 2

print(dp[-1])