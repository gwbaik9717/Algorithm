def solution(n):
    answer = 0
    queens = []
    
    def check(i, j):
        for qy, qx in queens:
            
            # 같은 row
            if qy == i:
                return False
            
            # 같은 col
            if qx == j:
                return False
            
            # 대각선
            if abs(qy - i) == abs(qx - j):
                return False
            
        return True
            
    
    def dfs(i):
        nonlocal answer
        
        if i == n:
            answer += 1
            return
        
        for j in range(n):
            if check(i, j):
                queens.append((i, j))
                dfs(i+1)
                queens.remove((i, j))
    
    dfs(0)

    return answer