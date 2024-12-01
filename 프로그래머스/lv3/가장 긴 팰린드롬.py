def solution(s):
    answer = 0
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # i-i 초기화
    for i in range(n):
        dp[i][i] = 1

    # i-i+1 초기화
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2


    for k in range(2, n):
        for i in range(n):
            j = i + k

            if j >= n:
                continue

            if s[i] == s[j] and dp[i+1][j-1] > 0:
                dp[i][j] = dp[i+1][j-1] + 2

    answer = max(map(lambda row: max(row), dp))

    return answer