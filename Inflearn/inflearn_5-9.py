sample="""5
big
good
sky
blue
mouse
sky
good
mouse
big"""

inputs = sample.split("\n")
n = int(inputs[0])
pres = inputs[1:1+n]
words = inputs[1+n:]
dict = dict()

set = set()

for pre in pres:
    set.add(pre)

for word in words:
    set.remove(word)

print(set.pop())