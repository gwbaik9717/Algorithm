sample="""4321 2"""

[num, m] = sample.split(" ")
i=0
cnt = 0
stack =[]

for i in range(len(num)):
    while cnt < int(m) and stack and stack[-1] < int(num[i]):
        stack.pop()
        cnt += 1
        
    stack.append(int(num[i]))

while cnt < int(m):
    stack.pop()
    cnt+=1

print("".join(list(map(str, stack))))