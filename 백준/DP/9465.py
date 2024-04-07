import sys

t = int(sys.stdin.readline().strip())

ans = []
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    stickers = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(2)]
    dp = [[0 for _ in range(n + 1)] for _ in range(2)]

    dp[0][1] = stickers[0][0]
    dp[1][1] = stickers[1][0]



    for j in range(2, n + 1):
         for i in range(2):
            if i == 0:
                dp[i][j] = max(
                    dp[i + 1][j - 1] + stickers[i][j - 1],
                    dp[i + 1][j - 2] + stickers[i][j - 1]
                )


            else:
                dp[i][j] = max(
                    dp[i - 1][j - 1] + stickers[i][j - 1],
                    dp[i - 1][j - 2] + stickers[i][j - 1]
                )   
    
    ans.append(str(max(dp[0][n], dp[1][n])))
    
print('\n'.join(ans))