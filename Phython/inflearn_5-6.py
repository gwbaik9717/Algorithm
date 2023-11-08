from collections import deque
sample = """8 3"""


[n, k] = map(int, sample.split(" "))


queue = deque([x for x in range(1, n+1)])
cnt = 0
while len(queue) > 1:
    popped = queue.popleft()
    if cnt == k-1:
        cnt = 0
    else: 
        queue.append(popped)
        cnt += 1

print(queue[0])


# i = 0
# cnt = 0
# while len(q) > 1:
#     if cnt == k-1:
#         q.pop(i)
#         cnt = 0
#     else:
#         cnt += 1
#         i = (i+1) % len(q)

# print(q[0])