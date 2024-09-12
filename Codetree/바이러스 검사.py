import sys
import math

n = int(sys.stdin.readline().strip())
rests = map(int, sys.stdin.readline().strip().split())
work_leader, work_member = map(int, sys.stdin.readline().strip().split())
answer = 0

for rest in rests:
    remainder = max(0, rest - work_leader)
    answer += (1 + math.ceil(remainder / work_member))

print(answer)