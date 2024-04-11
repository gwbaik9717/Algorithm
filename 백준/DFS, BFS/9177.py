import sys
from collections import deque

n = int(sys.stdin.readline().strip())
tcs = [sys.stdin.readline().strip().split() for _ in range(n)]


def bfs(tc):
    global ans
  
    q = deque()
    q.append(["", [0, 0]])

    while q:
        [cw, cis] = q.popleft()
        
        if cw == tc[-1]:
            ans = "yes"
            break

        for i, ci in enumerate(cis):
        
          if ci < len(tc[i]):
            ni = ci + 1
            ncis = cis[:]
            ncis[i] = ni
            nw = cw + tc[i][ci]

            if nw == tc[-1][:len(nw)]:
                q.append([nw, ncis])

for i, tc in enumerate(tcs):
    ans = "no"
    bfs(tc)
    print(f'Data set {i + 1}: {ans}')