import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
operator_cnts = list(map(int, sys.stdin.readline().strip().split()))
operator_kinds = ['+', '-', '*']
operators = []

max_ans = -1e9
min_ans = 1e9

for zipped in zip(operator_kinds, operator_cnts):
    operator, operator_cnt = zipped
    operators.extend([operator] * operator_cnt)

for permu in set(permutations(operators)):
    expression = f'{numbers[0]}'
    for i, number in enumerate(numbers[1:]):
        expression += f'{permu[i]}{number}'
        result = eval(expression)
        expression = str(result)

    result = eval(expression)

    max_ans = max(max_ans, result)
    min_ans = min(min_ans, result)

print(int(min_ans), int(max_ans))