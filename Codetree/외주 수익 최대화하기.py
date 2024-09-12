import sys

n = int(sys.stdin.readline().strip())
works = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

answer = 0

def dfs(index, end_time, price):
    global answer

    answer = max(answer, price)

    if index >= n or end_time >= n:    
        return
    
    for i in range(index + 1, n):
        cd, cp = works[i]

        new_end_time = i + cd

        if i >= end_time and new_end_time <= n:
            dfs(i, new_end_time, price + cp)

dfs(-1, -1, 0)    

print(answer)