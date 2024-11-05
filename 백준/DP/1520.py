import sys
sys.setrecursionlimit(10 ** 8)
m, n = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]

dy = [1, 0, -1, 0]
dx = [0 ,1, 0, -1]


def dfs(cy, cx):
     
     if dp[cy][cx] != -1:
          return dp[cy][cx]

     if (cy, cx) == (m-1, n-1):
          return 1
     
     ans = 0

     for zy, zx in zip(dy, dx):
          ny, nx = cy + zy, cx + zx

          if 0 <= ny < m and 0 <= nx < n and board[ny][nx] < board[cy][cx]:
               ans += dfs(ny, nx)

     dp[cy][cx] = ans

     return ans



print(dfs(0, 0))