sample="""11"""
ans = ""
def dfs(n):
    global ans

    if n == 1:
        ans += str(1)
    else:
        dfs(n // 2)
        ans += str(n % 2)
    
dfs(int(sample))
print(ans)