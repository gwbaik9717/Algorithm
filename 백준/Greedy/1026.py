import sys
n = int(sys.stdin.readline().strip())
answer = 0
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))

a.sort()
b.sort(reverse=True)

for i, va in enumerate(a):
    answer += b[i] * va

print(answer)