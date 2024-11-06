sample = """8 3
1 2 1 3 1 1 1 2"""

n, m = map(int, sample.split("\n")[0].split(" "))
arr = list(map(int, sample.split("\n")[1].split(" ")))

i=0
j=0
s=arr[0]
answer = 0


while i < n and j < n:
    if(s == m):
        answer += 1
    if(s >= m):
        s -= arr[i]
        i+=1
    else:
        j+=1
        if j==n:
            break
        s += arr[j]
    
print(answer)    