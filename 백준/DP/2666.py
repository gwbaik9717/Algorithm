import sys

n = int(sys.stdin.readline().strip())
temp = list(map(int, sys.stdin.readline().strip().split()))
temp.sort()
[sa, sb] = temp
t = int(sys.stdin.readline().strip())
aims = [0] + [int(sys.stdin.readline().strip()) for _ in range(t)]

dp = [[[sys.maxsize] * (n + 1) for _ in range(n + 1)] for _ in range(t + 1)]
dp[0][sa][sb] = 0

for i in range(1, t + 1):
    for j in range(1, n + 1):
        for k in range(j, n + 1):
            current_aim = aims[i]

            if dp[i-1][j][k] != sys.maxsize:
                if current_aim in [j, k]:
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])
                    continue

                # case 1
                new_arr = [current_aim, k]
                new_arr.sort()

                dp[i][new_arr[0]][new_arr[1]] = min(dp[i][new_arr[0]][new_arr[1]], dp[i-1][j][k] + abs(current_aim - j))
                
                # case 2
                new_arr = [j, current_aim]
                new_arr.sort()

                dp[i][new_arr[0]][new_arr[1]] = min(dp[i][new_arr[0]][new_arr[1]], dp[i-1][j][k] + abs(current_aim - k))

print(min(map(lambda row: min(row), dp[t])))