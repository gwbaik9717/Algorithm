def solution(n):
    global answer
    answer = 0
    board = [0] * (n + 1)
    
    def dfs(row):
        global answer
        
        if row == n:
            answer += 1
            return
        
        for i in range(1, n + 1):
            if check(row + 1, i):
                board[row + 1] = i
                dfs(row + 1)
    
    def check(row, col):
        for i in range(1, row):
            if board[i] == col:
                return False 
            if abs((board[i] - col) / (i - row)) == 1:
                return False
        return True
    
    dfs(0)
    
    return answer