sample = """1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7"""

inputs = sample.split("\n")
sudoku = list(map(lambda x: list(map(int, x.split(" "))), inputs))

def isValid():
    # 행 
    for i in range(9):
        checked = [0 for x in range(10)]
        for j in sudoku[i]:
            checked[j] += 1
            if checked[j] > 1:
                return False
    
    # 열
    for i in range(9):
        checked = [0 for x in range(10)]
        cols = list(map(lambda row : row[i], sudoku))

        for j in cols:
            checked[j] += 1
            if checked[j] > 1:
                return False
            
    # 
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            checked = [0 for x in range(10)]
            
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    cur = sudoku[k][l]
                    checked[cur] += 1
                    if checked[cur] > 1:
                        return False
    
    return True

if isValid():
    print("YES")
else:
    print("NO")
                    