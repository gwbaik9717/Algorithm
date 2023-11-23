import sys
import math

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
coins.sort()

table = [[math.inf] * (k + 1) for _ in range(n + 1)]

for row in table:
    row[0] = 0

for i in range(1, n+1):
    currentcoin = coins[i-1]

    for j in range(1, k+1):
        if j - currentcoin >= 0:
            table[i][j] = min(table[i][j - currentcoin] + 1, table[i-1][j])

        else:
            table[i][j] = table[i-1][j]
          

if table[-1][-1] != math.inf:
    print(table[-1][-1])
else:
    print(-1)