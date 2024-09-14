from itertools import combinations, permutations
import sys

n = int(sys.stdin.readline().strip())
table = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
works = [i for i in range(n)]
answer = 1e9

combis = combinations(works, n // 2)

for combi in combis:
    morning_works = combi
    evening_works = [work for work in works if not work in combi]

    morning_stress = sum([table[permu[0]][permu[1]] for permu in permutations(morning_works, 2)])
    evening_stress = sum([table[permu[0]][permu[1]] for permu in permutations(evening_works, 2)])

    answer = min(answer, abs(morning_stress - evening_stress))


print(answer)