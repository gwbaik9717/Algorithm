sample="""5
172 67
183 65
180 70
170 72
181 60"""

inputs = sample.split("\n")
pps = list(map(lambda x: list(map(int, x.split(" "))), inputs[1:]))

pps.sort(key=lambda x: (x[0], x[1]),  reverse=True)

ans = 0
maxW = None

for pp in pps:
    [h, w] = pp
    if maxW == None:
        maxW = w
        ans += 1
    
    if w > maxW:
        maxW = w
        ans += 1

print(ans)