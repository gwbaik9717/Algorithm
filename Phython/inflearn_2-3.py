from itertools import combinations

sample = """100 30
50 53 20 23 42 54 44 18 53 27 44 23 43 20 48 22 50 45 44 52 37 49 15 23 53 21 29 47 53 51 54 22 50 25 49 33 34 49 53 47 20 42 41 41 25 15 25 51 33 38 44 35 49 35 53 47 19 22 31 27 47 18 44 51 25 16 47 46 43 20 49 44 20 29 33 25 25 19 23 50 35 20 35 47 33 32 13 26 39 22 16 32 39 38 35 29 24 16 48 29"""

inputs = list(map(lambda x: list(map(int, x.split(" "))), sample.split("\n")))
n,k = inputs[0]
cards = inputs[1]

sums = list(map(lambda x: sum(x), combinations(cards, 3)))
sums.sort(reverse=True)


print(sorted(set(sums), reverse=True)[k-1])