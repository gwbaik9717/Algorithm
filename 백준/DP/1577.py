import sys
n, m = map(int, sys.stdin.readline().strip().split())
k = int(sys.stdin.readline().strip())
roads = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(k)]

dp = [[0] * (n+1) for _ in range(m+1)]
dp[0][0] = 1

def isRoad(start, end):
    for [a, b, c, d] in roads:
        if a < c or b < d:
            road_start = (a, b)
            road_end = (c, d)
        else:
            road_start = (c, d)
            road_end = (a, b)
        
        if  road_start == start and road_end == end:
            return True
        
    return False

for i in range(m+1):
    for j in range(n+1):
        if (i, j) == (0, 0):
            continue
        if i < 1:
            if not isRoad((j-1, i), (j, i)):
                dp[i][j] = dp[i][j-1]
                continue
        
        if j < 1:
            if not isRoad((j, i-1), (j, i)):
                dp[i][j] = dp[i-1][j]
                continue
        
        left = dp[i-1][j]
        right = dp[i][j-1]
        
        if isRoad((j, i-1), (j, i)):
            left = 0
        if isRoad((j-1, i), (j, i)):
            right = 0 
        
        dp[i][j] = left + right

print(dp[-1][-1])