import sys

NUM_CIRCLES = 4
circles = [sys.stdin.readline().strip() for _ in range(NUM_CIRCLES)]
n = int(sys.stdin.readline().strip())

orders = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

def rotate(cur, dir):
    if dir == 1:
        # 시계방향
        return cur[-1] + cur[:-1]
    else:
        # 반시계
        return cur[1:] + cur[0]
        
for order in orders:
    checked = [0] * NUM_CIRCLES
    circle_index, dir = order
    circle_index -= 1

    def get_candidates(index, dir):
        filtered = []
        for dx in [-1, 1]:
            cx = index
            nx = index + dx
            if 0 <= nx < NUM_CIRCLES:
                if dx == -1:
                    filtered.append((nx, circles[nx][2] == circles[cx][6]))
                else:
                    filtered.append((nx, circles[nx][6] == circles[cx][2]))

        filtered = [(candidate[0], dir * (-1)) for candidate in filtered if checked[candidate[0]] == 0 and not candidate[1]]
        
        checked[index] = 1

        for f in filtered:
            filtered += get_candidates(f[0], f[1])
        
        return filtered
    
    candidates = [(circle_index, dir)]
    candidates += get_candidates(circle_index, dir)

    for candidate in candidates:
        candidate_index, dir = candidate
        circles[candidate_index] = rotate(circles[candidate_index], dir)

print(int(circles[0][0]) + 2 * int(circles[1][0]) +  4 * int(circles[2][0]) + 8 * int(circles[3][0]))