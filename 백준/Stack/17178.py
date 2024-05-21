import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
q = deque()
waiting = []

for _ in range(n):
    q.extend(input().strip().split())

sorted_order = sorted(q, key=lambda x: (x.split("-")[0], int(x.split("-")[1])))


for i in range(5 * n):
    if waiting and waiting[-1] == sorted_order[i]:
        waiting.pop()
        continue 

    while q:
        popped = q.popleft()
        if popped == sorted_order[i]:
            break
        waiting.append(popped)
    else:
        print("BAD")
        exit()

print("GOOD")