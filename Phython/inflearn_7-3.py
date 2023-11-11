sample="""7
8
9
11
12
23
15
17"""

inputs = sample.split("\n")
k = int(inputs[0])
coins = list(map(int, inputs[1:]))
abc = [0] * 3
ans = 100000

def dfs(L):
    global ans

    if L == k:
        if len(set(abc)) == len(abc):
            ans = min(ans, max(abc) - min(abc))
    
    else:
        for i in range(3):
            abc[i] += coins[L]
            dfs(L+1)
            abc[i] -= coins[L]
        
dfs(0)
print(ans)