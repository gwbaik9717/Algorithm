sample = """(((()(()()))(())()))(()())"""

stack = []
ans = 0

for char in sample:
    if char == '(':
        stack.append(1)
    elif char == ')':
        # 레이저일 경우
        if stack[-1] == 1:
            stack = list(map(lambda x: x + 1, stack))
            stack.pop()
        else:
            ans += stack.pop()

print(ans)