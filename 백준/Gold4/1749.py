import sys

sample = """3 5
2 3 -21 -22 -23
5 6 -22 -23 -25
-22 -23 4 10 2"""

lines = sys.stdin.read().splitlines()


n, m = map(int, lines[0].split())
lines = [list(map(int, lines[i+1].split())) for i in range(n)]

arr = [[0 for _ in range(m+1)] for _ in range(n+1)]

# 각 열마다 누적합 구하기
for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i][j] = arr[i-1][j] + lines[i-1][j-1]


answer = -float('inf')

# 두 행을 선택하고 두 행 사이 각 열의 누적합 구하기
for i in range(1, n):
    for j in range(i, n+1):
        temp = [0 for _ in range(m+1)]

        for k in range(1, m+1):
            temp[k] = arr[j][k] - arr[i-1][k]
        
        # 카데인 알고리즘
        sums = [0 for _ in range(m+1)]

        for k in range(1, m+1):
            sums[k] = max(sums[k-1] + temp[k], temp[k])
            answer = max(answer, sums[k])

print(answer)