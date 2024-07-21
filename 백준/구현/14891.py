import sys
from collections import deque

gears = [sys.stdin.readline().strip() for _ in range(4)]
n = int(sys.stdin.readline().strip())
orders = [map(int, sys.stdin.readline().strip().split()) for _ in range(n)]

dx = [1, -1]


for order in orders:
    no, dir = order
    no -= 1

    q = deque()
    q.append((no, dir))
    
    list = []

    checked = [0] * 4
    checked[no] = 1

    while q:
        cn, cd = q.popleft()

        list.append((cn, cd))

        for ddx in dx:
            nn = cn + ddx

            if 0 <= nn < 4 and checked[nn] == 0:
                checked[nn] = 1
                # 오른쪽
                if ddx == 1:
                    if gears[cn][2] != gears[nn][6]:
                        q.append((nn, (-1) * cd))
                # 왼쪽
                if ddx == -1:
                    if gears[cn][6] != gears[nn][2]:
                        q.append((nn, (-1) * cd))
    
    
    for l in list:
        cg, cd = l
        # 시계 방향
        if cd == 1:
            gears[cg] = gears[cg][-1] + gears[cg][:-1]
        # 시계 반대 방향 
        else:
            gears[cg] = gears[cg][1:] + gears[cg][0]

answer = 0
for i, gear in enumerate(gears):
    answer += 2 ** i * int(gear[0])

print(answer)