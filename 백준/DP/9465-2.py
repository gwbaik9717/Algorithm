import sys

t =  int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    stickers = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(2)]

    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][1], dp[1][1] = stickers[0][0], stickers[1][0]

    
    for j in range(2, n + 1):
        for i in range(2):
            dp[i][j] = max(dp[1-i][j-1], dp[1-i][j-2]) + stickers[i][j-1]
    
    print(max(dp[0][-1], dp[1][-1]))