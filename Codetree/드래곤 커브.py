import sys

n = int(sys.stdin.readline().strip())
curves = [map(int, sys.stdin.readline().strip().split()) for _ in range(n)]

dots = [[0] * 200 for _ in range(200)]

# 오 위 왼 아
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def draw(pos, dir, g):
    sy, sx = pos

    dots[sy][sx] = 1

    ny, nx = sy, sx

    # 이전 세대 커브
    temp = [dir]

    # 새로 더해지는 커브 (이전세대 커브 +1 한 다음 reverse)
    q = [dir]

    # 0세대부터 g세대 까지 만들어야함
    for _ in range(g+1):
        for k in q:
            nx += dx[k]
            ny += dy[k]
            dots[ny][nx]=1
        q= [(i+1)%4 for i in temp]
        q.reverse()
        temp += q

for curve in curves:
    sy, sx, dir, g = curve
    draw((sy, sx), dir, g)

ans = 0

def count_square():
    global ans

    dy = [1, 1, 0]
    dx = [0, 1, 1]

    for i in range(200):
        for j in range(200):
            if dots[i][j] != 1:
                continue

            for zipped in zip(dy, dx):
                ny, nx = i + zipped[0], j + zipped[1]

                if 0 <= nx < 200 and 0 <= ny < 200 and dots[ny][nx] == 1:
                    pass
                else: 
                    break
            else:
                ans += 1

count_square()
print(ans)