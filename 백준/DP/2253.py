import sys
INF = sys.maxsize
n, m = map(int, sys.stdin.readline().strip().split())
skips = [int(sys.stdin.readline().strip()) for _ in range(m)]

dp = [[INF] * 150 for _ in range(n + 1)]
dp[1][0] = 0

for i in range(2, n + 1):
    speed = 1

    if i in skips:
        continue

    while 1 + speed * (speed + 1) / 2 <= i:
        dp[i][speed] = min(dp[i - speed][speed - 1], dp[i - speed][speed], dp[i - speed][speed + 1]) + 1
        speed += 1 

ans = min(dp[-1])

if ans == INF:
    print(-1)
else:
    print(ans)