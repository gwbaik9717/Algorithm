import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

n, m = len(str1), len(str2)

dp = [[''] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
  

        if str1[i-1] == str2[j-1]:
            new_str = dp[i-1][j-1] + str1[i-1]
            dp[i][j] = new_str
            continue
        
        if len(dp[i-1][j]) > len(dp[i][j-1]):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]))
print(dp[-1][-1])