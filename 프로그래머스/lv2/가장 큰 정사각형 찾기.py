def solution(board):
    h = len(board)
    w = len(board[0])

    dp = [[0] * w for _ in range(h)]

    # fill first row
    dp[0] = board[0]

    # fill first col
    for i, row in enumerate(board):
        dp[i][0] = row[0]

    for i in range (1, h):
        for j in range(1, w): 
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1


    answer = max(map(max, dp)) ** 2

    return answer