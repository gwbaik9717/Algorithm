import sys
from copy import deepcopy

l, n, q = map(int, sys.stdin.readline().strip().split())
graph = [sys.stdin.readline().strip().split() for _ in range(l)]
knights = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
original_knights = deepcopy(knights)

orders = [map(int, sys.stdin.readline().strip().split()) for _ in range(q)]

# 위쪽, 오른쪽, 아래쪽, 왼쪽 방향
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

walls = []

for i in range(l):
    for j in range(l):
        if graph[i][j] == '2':
            walls.append((i, j))

def damage(exception, moved):
    global knights

    for mv in moved:
        if mv == exception:
            continue

        knight = knights[mv]

       

        r,c,h,w,k = knight

        cnt = 0

        for l in range(r-1, r-1+h):
            for m in range(c-1, c-1+w): 
                if graph[l][m] == "1":
                    cnt += 1
        
        knight[-1] = max(0, k - cnt)

def get_ans():

    ans = 0

    for i, knight in enumerate(knights):
        r,c,h,w,k = knight

        if k == 0:
            continue

        ans += original_knights[i][-1] - k
    
    return ans

def get_intersection(knight_a, b):

    ar,ac,ah,aw = knight_a
    br,bc,bh,bw,bk = knights[b]

    for i in range(br-1, br-1+bh):
        for j in range(bc-1, bc-1+bw):
            if ar <= i < ar+ah and ac <= j < ac+aw:
                return True
    
    return False


def move(i, d, moved):

    knight = knights[i]
    r,c,h,w,k = knight

    nr, nc = r + dy[d] - 1, c + dx[d] - 1

    if 0 <= nr < l and 0 <= nc < l and 0 <= nr+h-1 < l and 0 <= nc+w-1 < l: 
        
        # 벽에 막힐 경우
        for wall in walls:
            wy, wx = wall

            if nr <= wy < nr + h and nc <= wx < nc + w:
                return False


        for j, kn in enumerate(knights):
            if i == j:
                continue

            # 체력이 0 이면 없는 것과 다름 없음
            if kn[-1] == 0:
                continue

            # 겹치는게 있으면 겹치는 것을 먼저 move
            if get_intersection((nr, nc, h, w), j):

                # 만약에 하나라도 움직이지 못한다면 stop
                if not move(j, d, moved):
                    return False
    
    else:
        return False
    
    moved.append(i)

    return True


for order in orders:
    i, d = order

    i -= 1

    if knights[i][-1] == 0:
        continue

    moved = []

    if move(i, d, moved):
       
        for mv in moved:
            knight = knights[mv]
            r,c,h,w,k = knight
            knights[mv] = [r+dy[d], c+dx[d], h, w, k]
       
        damage(i, moved)

print(get_ans())