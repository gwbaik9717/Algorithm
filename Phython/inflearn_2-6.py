sample = """3
125 15232 97"""

nums = sample.split("\n")[1].split(" ")

candidates = list(map(lambda x: [x[0], x[1], sum([int(digit) for digit in x[1]])], enumerate(nums)))
candidates.sort(key=lambda x: (-x[2], x[0]))
print(candidates[0][1])