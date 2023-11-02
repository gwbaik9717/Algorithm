sample = """5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19"""

n = int(sample.split("\n")[0])
g = sample.split("\n")[1:]


graph = list(map(lambda x: list(map(int, x.split(" "))), g))

cnt = 1
ans = 0

for i in range(n):
    num = i * 2 + 1
    if num > n:
        num = num % (n-1)
    start = int((n - num)/2)
    print(start, num)
    ans += sum(graph[i][start : start + num])

print(ans)

    