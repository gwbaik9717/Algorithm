import sys 

INF = sys.maxsize
n = int(sys.stdin.readline().strip())

for _ in range(n):
    m = int(sys.stdin.readline().strip())
    chapters = list(map(int, sys.stdin.readline().strip().split()))

    sum = [0] * (m + 1)

    for i in range(m):
        sum[i + 1] = sum[i] + chapters[i]

    dp = [[0] * (m+1) for _ in range(m+1)]

    for i in range(1, m):
        k = 1 # y 좌표
        j = i + 1 # x 좌표

        for l in range(m - i):
            dp[k][j] = INF
            
            for p in range(k, j):          
                dp[k][j] = min(dp[k][j], dp[k][p] + dp[p + 1][j] + sum[j] - sum[k - 1])

            j += 1
            k += 1
    
    print(dp[1][m])