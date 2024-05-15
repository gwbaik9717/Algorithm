import sys


n = int(sys.stdin.readline().strip())
datas = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
answer = 0
stack = []

for i, data in enumerate(datas):
    if data == [0]:
        if stack:
            score, duration = stack.pop()
            duration -= 1
        
            if duration > 0:
                stack.append((score, duration))
            else:
                answer += score
        
        continue
    
    a, t = data[1:]

    if t == 1:
        answer += a
    else:
        stack.append((a, t - 1))

print(answer)