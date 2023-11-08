sample="""3*(5+2)-9"""
stack=[]
ans = ""

i = 0

for x in sample:
    if x.isdigit():
        ans += x
    elif x == '(':
        stack.append(x)
    elif x == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
    elif x in ['+', '-']:
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(x)
    elif x in ['*', '/']:
        while stack and stack[-1] in ['*', '/']:
            ans += stack.pop()
        stack.append(x)
        

while stack:
    ans += stack.pop()
           

print(ans)