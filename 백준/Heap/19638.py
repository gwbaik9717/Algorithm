import sys, math
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

answer = []
n, h, t = map(int, input().strip().split())
giants = [(-1) * int(input().strip()) for _ in range(n)]
heapify(giants)

for i in range(t):
    if giants:
        popped = heappop(giants) * (-1)
        if popped < h:
            answer = ["YES", i]
            break
        
        heappush(giants, min(-1, math.floor(popped / 2) * (-1)))
else:
    if giants:
        popped = heappop(giants) * (-1)
        if popped < h:
            answer = ["YES", t]
        else:
            answer = ["NO", popped]

print(answer[0])
print(answer[1])