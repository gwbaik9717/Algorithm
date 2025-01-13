import sys
n = int(sys.stdin.readline().strip())

dp = [i for i in range(3)]
dp[0] = 3
dp[1] = 7

for i in range(2, n):
    if i % 3 == 2:
        dp[2] = 2 * dp[1] + dp[0]
    
    if i % 3 == 1:
        dp[1] = 2 * dp[0] + dp[2]
    
    else:
        dp[0] = 2 * dp[2] + dp[1]

print(dp[(n-1)%3] % 9901)