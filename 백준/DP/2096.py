import sys
import copy
n = int(sys.stdin.readline().strip())

dp_max = [[0] * 3 for _ in range(2)]
dp_min = [[0] * 3 for _ in range(2)]

scores = list(map(int, sys.stdin.readline().strip().split()))
dp_max[0] = copy.deepcopy(scores)
dp_min[0] = copy.deepcopy(scores)

for i in range(1, n):
    scores = list(map(int, sys.stdin.readline().strip().split()))

    for j in range(3):
        if j == 0:
            dp_max[1][j] = max(dp_max[0][0], dp_max[0][1]) + scores[j]
            dp_min[1][j] = min(dp_min[0][0], dp_min[0][1]) + scores[j]
        elif j == 1:
            dp_max[1][j] = max(dp_max[0][0], dp_max[0][1], dp_max[0][2]) + scores[j]
            dp_min[1][j] = min(dp_min[0][0], dp_min[0][1], dp_min[0][2]) + scores[j]
        else:
            dp_max[1][j] = max(dp_max[0][1], dp_max[0][2]) + scores[j]
            dp_min[1][j] = min(dp_min[0][1], dp_min[0][2]) + scores[j]

    dp_max[0] = copy.deepcopy(dp_max[1])
    dp_min[0] = copy.deepcopy(dp_min[1])

print(max(dp_max[0]), min(dp_min[0]))