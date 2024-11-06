import statistics, math

sample = """10
45 73 66 87 92 67 75 79 75 80
"""


scores = [[x, i+1] for i,x in enumerate(list(map(int, sample.split("\n")[1].split(" "))))]

mean = round(statistics.mean(map(lambda x: x[0], scores)))

scores.sort(key=lambda x: (abs(mean - x[0]), -x[0], x[1]))
print(scores[0][1])