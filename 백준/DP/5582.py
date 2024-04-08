import sys
str1 = list(sys.stdin.readline().strip())
str2 = list(sys.stdin.readline().strip())
n = len(str1)
m = len(str2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

ans = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])

print(ans)