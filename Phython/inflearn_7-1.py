
sample = """5 20
10 5
25 12
15 8
6 3
7 4"""

inputs = sample.split("\n")

[n, m]= map(int, inputs[0].split(" "))
infos = list(map(lambda x: list(map(int, x.split(" "))), inputs[1:]))
checked = [0] * n

ans = 0 

def dfs(start, cs, ct):
    global ans
    
    for i, info in enumerate(infos, start=start):
        [s, d] = info
        
        if ct + d <= m:
            dfs(start + 1, cs + s, ct + d)
        else:
            ans = max(ans, cs)


dfs(0 ,0, 0)
print(ans)