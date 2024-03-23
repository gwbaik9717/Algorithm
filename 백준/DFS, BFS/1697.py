import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

q = deque()
q.append([n, 0])
checked = [False] * 100001
checked[n] = True

while q:
    [cx, cd] = q.popleft()
    if cx == k:
        print(cd)
        break

    for nx in (cx - 1, cx + 1, cx * 2):
        if nx >= 0 and nx <= 100000 and not checked[nx]:
            checked[nx] = True
            q.append([nx, cd + 1])