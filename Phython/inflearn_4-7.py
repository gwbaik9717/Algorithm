sample="""10
69 42 68 76 40 87 14 65 76 81
50"""

inputs = sample.split("\n")
n = int(inputs[0])
boxes = list(map(int, inputs[1].split(" ")))
m = int(inputs[2])

for i in range(m):
    boxes.sort()
    boxes[0] += 1
    boxes[-1] -= 1

boxes.sort()

print(boxes[-1] - boxes[0])