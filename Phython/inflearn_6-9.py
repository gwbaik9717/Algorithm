import copy

sample="""4 16"""
[n, f] = map(int, sample.split(" "))
nums = list(range(1, n + 1))

def permu(arr, n):
    if n == 1:
        return list(map(lambda x: [x], arr))
    
    rv = []

    for i, x in enumerate(arr):
        filtered = [y for j, y in enumerate(arr) if j != i]
        rv += list(map(lambda u: [x, *u] , permu(filtered, n-1)))

    return rv

def isTarget(arr, target):
    stack = arr

    while len(stack) > 1:
        temp = []
        for i in range(len(stack) - 1):
            temp .append(stack[i] + stack[i+1])
        stack = copy.deepcopy(temp)
    
    if stack[0] == target:
        return True
    return False

perms = permu(nums, n)


for perm in perms:
    if isTarget(perm, f):
        print(perm)
        break