import sys
from collections import deque

t = int(sys.stdin.readline())
ans = []

def get_dist(start, end):
    [sy, sx] = nodes[start]
    [ey, ex] = nodes[end]

    return abs(sy - ey) + abs(sx - ex)

for _ in range(t):
    n = int(sys.stdin.readline())
    nodes = [list(map(int, sys.stdin.readline().split())) for _ in range(n + 2)]
    visited = [0 for _ in range(n + 2)]

    q = deque()
    q.append(0)
    visited[0] = 1

    while q:
        cp = q.popleft()
        [cy, cx] = nodes[cp]

        if cp == len(nodes) - 1:
            ans.append("happy")
            break

        for i, node in enumerate(nodes):
            if visited[i] == 0 and get_dist(cp, i) <= 1000:
                visited[i] = 1
                q.append(i)
    else:
        ans.append("sad")

print("\n".join(ans))