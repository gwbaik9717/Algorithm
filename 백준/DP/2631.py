import sys

n = int(sys.stdin.readline().strip())
order = [int(sys.stdin.readline().strip()) for _ in range(n)]

# i 번째에 끝나는 가장 긴 부분증가수열
dp = [1] * n

for i in range(n):
    for j in range(i):
        if order[i] > order[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))