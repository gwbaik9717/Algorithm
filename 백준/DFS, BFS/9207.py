import sys 

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

t = int(sys.stdin.readline().strip())

n = 5
m = 9


for i in range(t):

    answer = [1e9, 1e9]

    board = [list(sys.stdin.readline().strip()) for _ in range(n)]

    def dfs(count):
        global answer

        pins = []

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'o':
                    pins.append((i, j))
        
        if len(pins) < answer[0]:
            answer[0] = min(answer[0], len(pins))
            answer[1] = count
        elif len(pins) == answer[0]:
            answer[1] = min(answer[1], count)
        
        for pin in pins:
            cy, cx = pin

            for zipped in zip(dy, dx):
                ddy, ddx = zipped

                ny = cy + ddy
                nx = cx + ddx

                ny2 = ny + ddy 
                nx2 = nx + ddx

                if 0 <= nx2 < m and 0 <= ny2 < n and board[ny][nx] =='o' and board[ny2][nx2] == '.':
                    board[ny][nx] = '.'
                    board[ny2][nx2], board[cy][cx] = board[cy][cx], board[ny2][nx2]

                    dfs(count + 1)

                    board[ny][nx] = 'o'
                    board[ny2][nx2], board[cy][cx] = board[cy][cx], board[ny2][nx2]

    dfs(0)

    print(answer[0], answer[1])

    if i != t-1:
     sys.stdin.readline()