import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    test = int(sys.stdin.readline().strip())
    dp = [0] * (test + 1)
    dp[0] = 1

    for i in range(1, test + 1):
        for j in range(1, 4):
            if i - j >= 0:
                dp[i] += dp[i - j]
            else:
                break
    
    print(dp[-1])