import sys

n, m, k = map(int, sys.stdin.readline().strip().split())
atoms = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
graph = [[[] for _ in range(n)] for _ in range(n)]

#  ↑, ↗, →, ↘, ↓, ↙, ←, ↖
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for atom in atoms :
    y, x, m, s, d  = atom
    graph[y-1][x-1].append((y-1, x-1, m, s, d))

def get_mass():
    total = 0
    for i in range(n):
        for j in range(n):
            total += sum(map(lambda x: x[2], graph[i][j]))
    
    return total

def move():
    global graph

    to_move = []
    for i in range(n):
        for j in range(n):
            for atom in graph[i][j]:
                cy, cx, cm, cs, cd = atom
                ny, nx = (cy + dy[cd] * cs) % n, (cx + dx[cd] * cs) % n
                to_move.append((ny, nx, cm, cs, cd))
    
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    
    for atom in to_move:
        cy, cx = atom[0], atom[1]
        new_graph[cy][cx].append(atom)
    
    graph = new_graph


def merge_and_split():
    global graph 

    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) < 2:
                continue
            
            cy, cx, cm, cs, cd = graph[i][j][0]

            sum_m = sum(map(lambda x: x[2], graph[i][j]))
            sum_s = sum(map(lambda x: x[3], graph[i][j]))
            
            nm = sum_m // 5
            ns = sum_s // len(graph[i][j])

            if nm == 0:
                graph[i][j] = []
                continue

            # 모두 짝수 Or 홀수
            if all(map(lambda x: x[-1] % 2 == 0, graph[i][j])) or all(map(lambda x: x[-1] % 2 == 1, graph[i][j])):
                graph[i][j] = [(cy, cx, nm, ns, 0), (cy, cx, nm, ns, 2), (cy, cx, nm, ns, 4), (cy, cx, nm, ns, 6)]
            else:
                graph[i][j] = [(cy, cx, nm, ns, 1), (cy, cx, nm, ns, 3), (cy, cx, nm, ns, 5), (cy, cx, nm, ns, 7)]

def round():
    move()
    merge_and_split()
    
for i in range(k):
    round()

print(get_mass())