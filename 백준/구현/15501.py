import sys
input = sys.stdin.readline

answer = "bad puzzle"
n = int(input().strip())
asis = input().strip().split()
tobe = input().strip().split()

idx = asis.index(tobe[0])
list1 = asis[idx:] + asis[:idx]

asis = asis[::-1]
idx = asis.index(tobe[0])
list2 = asis[idx:] + asis[:idx]

if tobe == list1 or tobe == list2:
     answer = "good puzzle"

print(answer)