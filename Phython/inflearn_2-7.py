import math
sample=20

arr=[0] * (sample + 1)

for i in range(2, math.floor(math.sqrt(sample)) + 1):
    if arr[i] != 0:
        continue

    j = 2
    while i * j <= sample:
        arr[i*j] = 1
        j+=1 


print(len(list(filter(lambda x: x == 0, arr[2:]))))