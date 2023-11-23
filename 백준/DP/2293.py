import sys

n, k = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for _ in range(n)]
coins.sort()

table = [0] * ((k + 1) * (n + 1))

for i in range(n + 1):
    table[i * (k + 1)] = 1
    
for i in range(1, n+1):
    currentcoin = coins[i-1]

    for j in range(0, k+1):
        if j - currentcoin < 0:
            table[i * (k + 1) + j] = table[(i - 1) * (k + 1) + j]
        else:
            table[i * (k + 1) + j] = table[(i - 1) * (k + 1) + j] + table[i * (k + 1) + j - currentcoin]

print(table[-1])