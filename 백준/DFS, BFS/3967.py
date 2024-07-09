import sys

candidates = [chr(i) for i in range(ord('A'), ord('L') + 1)]
checked = [0 for _ in range(12)]
star = []
target = ord('A') * 4 + 22

n = 5

for _ in range(n):
    row = [v for v in list(sys.stdin.readline().strip()) if v != '.']

    for r in row:
        if r != 'x':
            checked[ord(r) - ord('A')] = 1

    star += row

def check():
    lines = [(1,2,3,4), (1,5,8,11), (4,6,9,11), (0,2,5,7), (7,8,9,10), (0,3,6,10)]

    for line in lines:
        sum = 0

        for index in line:
            value = star[index]

            if value == 'x': 
                continue

            sum += ord(value)
        
        if sum > target:
            return False

        if sum != target:
            return False
    
    return True

def draw():
    points = [(0, 4), (1, 1), (1, 3), (1, 5), (1, 7), (2, 2), (2, 6), (3, 1), (3, 3), (3, 5), (3, 7), (4, 4)]

    idx = 0
    for i in range(5):
        row = ['.'] * 9

        for point in points:
            if point[0] == i:
                row[point[1]] = star[idx]
                idx += 1
        
        print("".join(row))
        


def dfs(): 
    if check():
        draw()
        exit(0)
    
    if 'x' not in star:
        return
    
    index = star.index('x')

    for i, c in enumerate(checked):
        if c == 0:
            checked[i] = 1
            star[index] = candidates[i]
            dfs()
            checked[i] = 0
            star[index] = 'x'
    
dfs()