import sys 

n = int(sys.stdin.readline().strip())
numbers = [0] + [int(sys.stdin.readline().strip()) for _ in range(n)]
checked = [0] * (n+1)


def dfs(current, target, paths):

    if current == target:
        for path in paths:
            checked[path] = 1      
        return
    
    if current not in paths:
        paths.append(current)
        dfs(numbers[current], target, paths)
    
    
for i in range(1, n+1):
    if checked[i] == 0:
        dfs(numbers[i], i, [i])

print(sum(checked))
for i in range(1, n+1):
    if checked[i] == 1:
        print(i)