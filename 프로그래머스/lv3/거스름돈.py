def solution(n, money):
    answer = 0
    m = len(money)

    money.sort()

    dp = [[1] + [0] * n for _ in range(m+1)]

    dp[1] = [(0 if i < money[0] or i % money[0] != 0 else 1) for i in range(n+1)]

    for i in range(2, m+1):
        for j in range(1, n+1):

            dp[i][j] = dp[i-1][j] + (0 if j < money[i-1] else dp[i][j-money[i-1]])            

    answer = dp[-1][-1]

    return answer % 1000000007
