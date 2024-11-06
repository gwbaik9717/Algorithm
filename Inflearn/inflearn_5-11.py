from heapq import heappush, heappop

heap = []

sample="""5
3
6
0
5
0
2
4
0
-1"""

inputs = sample.split("\n")

for x in map(int, inputs):
    if x == 0:
        print(heappop(heap))
    elif x == -1:
        break
    else:
        heappush(heap, x)