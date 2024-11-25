import sys

t = int(sys.stdin.readline().strip())

for tt in range(t):
    n = int(sys.stdin.readline().strip())
    combis = []

    def dfs(lv, operators):

        if lv == n-1:
            combis.append(operators)
            return

        for operator in ['+', '-', '']:
            new_operators = operators[:] + [operator]
            dfs(lv+1, new_operators)
    
    dfs(0, [])

    answer = []

    for combi in combis:
        
        numbers = [i+1 for i in range(n)]
        expression = "1"
        raw_expression = ['1']
        for operator, number in zip(combi, numbers[1:]):
            expression += operator + str(number)
            raw_expression += [operator if operator != "" else " ", str(number)]
        
        if eval(expression) == 0:
            answer.append("".join(raw_expression))
    
    answer.sort()
    print("\n".join(answer))

    if tt != t-1:
        print()

        


