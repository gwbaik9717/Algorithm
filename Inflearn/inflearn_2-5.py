sample = "4 6"
n, m = map(int, sample.split(" "))

dic = dict()

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum = i + j
        if(bool(dic.get(sum))):
            dic[sum] += 1
        else:
            dic[sum] = 1
        
sums = list(map(lambda x: [x[0], x[1]], dic.items()))
filtered = list(filter(lambda x : x[1] == max(map(lambda x : x[1], sums)), sums))
candidates = list(map(lambda x: x[0], filtered))

for candidate in candidates:
    print(candidate, end =' ')