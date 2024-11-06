sample = """5
1 4
2 3
3 5
4 6
5 7"""

inputs = sample.split("\n")

candidates = list(map(lambda x: list(map(int, x.split(' '))),inputs[1:]))


candidates.sort(key=lambda x: (x[1], x[0]))

stack = []

for candidate in candidates:
    [s1, e1] = candidate

    if len(stack) == 0:
        stack.append(candidate)
    else:
        [s2, e2] = stack[-1]
        if s1 >= e2:
            stack.append(candidate)

print(len(stack))