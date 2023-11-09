sample="""3 2"""

[n, m] = map(int, sample.split(" "))

def permu(arr, r):
    if r == 1:
        return list(map(lambda x: [x], arr))
    
    rv = []

    for i in range(len(arr)):
        rv += list(map(lambda x: [arr[i] , *x], permu(arr, r-1)))

    return rv

print(permu(list(range(1, n+1)), m))