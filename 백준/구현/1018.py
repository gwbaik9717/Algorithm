import sys

INF = sys.maxsize
answer = INF

wb = "WB" * 25
bw = "BW" * 25

case1 = [wb, bw] * 25
case2 = [bw, wb] * 25

n, m = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]

def count(to_compare, compared, sy, sx):
    cnt = 0

    for i in range(sy, sy + 8):
        for j in range(sx, sx + 8):
            if to_compare[i][j] != compared[i][j]:
                cnt += 1
    
    return cnt


for i in range(n - 7):
    for j in range(m - 7):

        # case1 
        cnt1 = count(case1, board, i, j)

        # case2
        cnt2 = count(case2, board, i, j)

        answer = min(answer, cnt1, cnt2)

print(answer)