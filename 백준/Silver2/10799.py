import sys
str = sys.stdin.readline().strip()

answer = 0
stack = []

for i, chr in enumerate(str):
    
    if chr == '(':
        stack.append((chr, i))
        continue

    if chr == ')':
        # 레이저일때
        if stack[-1][0] == '(' and stack[-1][1] + 1 == i:
            stack.pop()
            answer += len(stack)
        
        # 막대의 끝일때
        else: 
            stack.pop()
            answer += 1
            

print(answer)    