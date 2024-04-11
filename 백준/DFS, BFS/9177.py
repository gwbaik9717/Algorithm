import sys

n = int(sys.stdin.readline().strip())
tcs = [sys.stdin.readline().strip().split() for _ in range(n)]

def dfs(cur, cci, tc):
    global ans

    [a, b, target] = tc
    n = len(cur)

    if n > 0 and target[:n] != cur:
        return 
    if target == cur:
        ans = "yes"
        return 
    
    for i, ci in enumerate(cci):
        if ci < len(tc[i]):
            new_cci = cci[:]
            new_cci[i] += 1
            
            dfs(cur + tc[i][ci], new_cci, tc)



for i, tc in enumerate(tcs):
    ans = "no"
    dfs("", [0, 0], tc)
    print(f'Data set {i + 1}: {ans}')