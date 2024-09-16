import sys

n, k = map(int, sys.stdin.readline().strip().split())
steps = [[step, False] for step in list(map(int, sys.stdin.readline().strip().split()))]

def is_end():
    filtered = [step for step in steps if step[0] == 0]
    return len(filtered) >= k

def rotate():
    global steps

    new_steps = []
    new_steps.append(steps[-1])
    new_steps.extend(steps[:-1])
    steps = new_steps
    offboard()

def onboard():
    global steps

    if steps[0][0] == 0 or steps[0][1] == True:
        return
    
    steps[0][0] -= 1
    steps[0][1] = True

def offboard():
    global steps

    if steps[n-1][1] == True:
        steps[n-1][1] = False

def move():
    global steps

    for i in range(n - 2, -1, -1):
        
        if steps[i][1] == False:
            continue

        if steps[i + 1][1] == True or steps[i + 1][0] == 0:
            continue

        steps[i + 1][0] -= 1
        steps[i][1] = False

        if i + 1 == n-1:
            offboard()
        else:
            steps[i + 1][1] = True
    
def experiment():
    rotate()
    move()
    onboard()


ans = 0
while not is_end():
    ans += 1
    experiment()

print(ans)