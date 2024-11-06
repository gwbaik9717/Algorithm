from collections import deque

sample="""6 0
60 60 90 60 60 60"""

inputs = sample.split("\n")
[n, m] = map(int, inputs[0].split(" "))
patients = list(map(int, inputs[1].split(" ")))

og = deque(map(lambda x: [x[1], x[0]], enumerate(patients)))
patients.sort(reverse=True)

# print(patients)

i=0
while True:
    popped = og.popleft()
    print(popped)

    if popped[0] == patients[i]:
        i += 1
        if popped[1] == m:
            print(i)
            break
    else:
        og.append(popped)