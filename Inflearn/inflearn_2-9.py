import math

sample = """3
3 3 6
2 2 2
6 2 5"""

results = list(map(lambda x: list(map(int, x.split(" "))), sample.split("\n")[1:]))
answer = 0

for result in results:
    ns = [0] * 7

    for r in result:
        ns[r]+=1

    n = len(list(filter(lambda x : x != 0, ns)))

    if n == 1:
        ans = ns.index(3)
        answer = max(answer, 10000 + ans * 1000)
    elif n == 2:
        ans = ns.index(2)
        answer = max(answer, 1000 + ans * 100)
    else:
        ans = 6 - ns[::-1].index(1)
        answer = max(answer, ans * 100)

print(answer)

