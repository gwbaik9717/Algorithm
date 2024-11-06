sample="""7
4 20
2 10
3 15
3 20
2 30
2 20
1 10"""

inputs = sample.split("\n")
n = int(inputs[0])
tables = list(map(lambda x: list(map(int, x.split(" "))), inputs[1:]))
ans = 0


def dfs(today, cp):
    global ans

    for i, table in enumerate(tables[today:]):
        [t, p] = table
        
        if today + i + t <= n:
            ans = max(ans, cp + p) 
            dfs(today + i + t, cp + p)
        

dfs(0, 0)
print(ans)