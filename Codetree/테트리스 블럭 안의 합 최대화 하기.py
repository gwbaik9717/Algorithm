import sys

n, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
ans = -1e9

def place(position):
    sy, sx = position

    def dfs(lv, blocks, total):
        global ans

        if lv >= 3:
            ans = max(ans, total)
            return

        for block in blocks:
            by, bx = block

            for zipped in zip(dy, dx):
                ny, nx = by + zipped[0], bx + zipped[1]

                if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in blocks:
                    blocks.append((ny, nx))
                    dfs(lv + 1, blocks, total + graph[ny][nx])
                    blocks.pop()
    
    dfs(0, [(sy, sx)], graph[sy][sx])
    

for i in range(n):
    for j in range(m):
        place((i, j))

print(ans)