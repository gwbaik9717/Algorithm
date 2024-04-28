import sys
n = sys.stdin.readline().strip()
length = len(n)

dp = [0] * (length + 1)
dp[0] = 1
dp[1] = 1



for i in range(2, length + 1):
    if 10 <= int(n[i-2:i]) <= 26:    
        if int(n[i-1: i]) == 0:
            dp[i] = dp[i-2]
        else:
            dp[i] = dp[i-2] + dp[i-1]
        continue

    if int(n[i-2:i]) == 0:
        continue

    if int(n[i-2:i]) < 10:
        if i > 2:
            dp[i] = dp[i-1]
    
    if int(n[i-2:i]) > 26:
        if int(n[i-1]) == 0:
            continue
        dp[i] = dp[i-1]


if int(n[0]) == 0:
    print(0)
else:
    print(dp[-1] % 1000000)