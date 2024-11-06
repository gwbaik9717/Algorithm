from itertools import combinations
sample="""5 3
2 4 5 8 12
6"""

inputs = sample.split("\n")
[n, k] = map(int, inputs[0].split(" "))
nums = map(int, inputs[1].split(" "))

combis = combinations(nums, k)
cnt = 0 
for combi in combis:
    if sum(combi) % 6 == 0:
        cnt += 1
print(cnt)