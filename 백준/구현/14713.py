from collections import deque
import sys
input = sys.stdin.readline

answer = "Possible"
n = int(input().strip())
parrots = [deque(input().strip().split()) for _ in range(n)]
sentence = input().strip().split()

if sum(map(lambda parrot: len(parrot), parrots)) != len(sentence):
    answer = "Impossible"
else:
    for word in sentence:
        for parrot in parrots:
            if parrot:
                if parrot[0] == word:
                    parrot.popleft()
                    break
        else:
            answer = "Impossible"
            break

print(answer)