sample="""3 2"""

[n, m] = map(int, sample.split(" "))
balls = list(range(1, n+1))

def combi(arr, n):
    if n == 1:
        return list(map(lambda x: [x], arr))
    
    rv = []

    for i, x in enumerate(arr):
        filtered = [x for j, x in enumerate(arr) if j != i]

        rv += list(map(lambda y: [x, *y], combi(filtered, n-1)))
    
    return rv

print(combi(balls, m))