import sys
from collections import deque

n = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n + 1)]
scores = [0] * (n + 1)

while True:
    f1, f2  = map(int, sys.stdin.readline().strip().split())
    if (f1, f2) == (-1, -1):
        break
    else:
        graph[f1].append(f2)
        graph[f2].append(f1)


def bfs(si):
    q = deque()
    q.append([si, 0])
    checked = [0] * (n + 1)
    checked[si] = 1
    score = 0

    while q:
        [ci, cd] = q.popleft()
        score = max(score, cd)

        for ni in graph[ci]:
            if checked[ni] == 0:
                q.append([ni, cd + 1])
                checked[ni] = 1
    
    return score

for i in range(1, n + 1):
    scores[i] = bfs(i)

candidate_score = min(scores[1:])
candidates = list(filter(lambda score: score[1] == candidate_score, enumerate(scores)))

print(candidate_score, len(candidates))
print(' '.join(list(map(lambda x: str(x[0]), candidates))))