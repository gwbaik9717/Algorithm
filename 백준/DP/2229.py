import sys
n = int(sys.stdin.readline().strip())
students = list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * (n + 1)

for i in range(2, n + 1):
    for j in range(i):
        new_group = students[j:i]
        dp[i] = max(dp[i], dp[j] + max(new_group) - min(new_group))

print(dp[-1])