sample="""AbaAeCF
baeeCCA"""

[a, b] = sample.split("\n")

dicA = dict()
dicB = dict()

for char in a:
    dicA[char] = dicA.get(char, 0) + 1

for char in b:
    dicB[char] = dicB.get(char, 0) + 1

for keyA, itemA in dicA.items():
    if dicB.get(keyA) and dicB[keyA] != itemA:
        print("NO")
        break
else:
    print("YES")