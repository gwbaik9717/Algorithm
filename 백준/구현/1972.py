import sys

while True:
    input = sys.stdin.readline().strip()
    if input == '*':
        break
    
    for i in range(1, len(input)):
        total = []
        uniques = set()
        for j in range(len(input) - i):
            str = input[j] + input[j + i]
            total.append(str)
            uniques.add(str)
        if len(total) != len(uniques):
            print(f'{input} is NOT surprising.')
            break
    else:
         print(f'{input} is surprising.')
