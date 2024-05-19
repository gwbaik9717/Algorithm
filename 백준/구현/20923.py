import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())
deck_do = deque()
deck_su = deque()
ground_do = deque()
ground_su = deque()

for _ in range(n):
    d, s = map(int, input().strip().split())
    deck_do.append(d)
    deck_su.append(s)

gd, gs = 0, 0

for cnt in range(m):
    if cnt % 2 == 0:
        gd = deck_do.pop()
        ground_do.append(gd)
    else:
        gs = deck_su.pop()
        ground_su.append(gs)

    if not deck_do:
        break

    if not deck_su:
        break

    if gd == 5 or gs == 5:
        deck_do.extendleft(ground_su)
        deck_do.extendleft(ground_do)
        ground_do.clear()
        ground_su.clear()

    elif ground_do and ground_su and ground_do[-1] + ground_su[-1] == 5:
        deck_su.extendleft(ground_do)
        deck_su.extendleft(ground_su)
        ground_do.clear()
        ground_su.clear()
    
    gd, gs = 0, 0


if len(deck_do) > len(deck_su):
    print("do")
elif len(deck_do) < len(deck_su):
    print("su")
else:
    print("dosu")