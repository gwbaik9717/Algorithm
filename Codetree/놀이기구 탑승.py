import sys

n = int(sys.stdin.readline().strip())
friends = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n**2)]
seats = [[0] * n for _ in range(n)]
scores = [0] + [10**(i-1) for i in range(1, 4)]

dict_friends = dict()

dy = [1, 0, -1, 0]
dx = [0, 1, 0 , -1]

def count(index, cur):
    cy, cx = cur
    
    cnt_empty = 0
    cnt_friends = 0

    for zipped in zip(dy, dx):
        ny = cy + zipped[0]
        nx = cx + zipped[1]

        if 0 <= nx < n and 0 <= ny < n:
            if seats[ny][nx] == 0:
                cnt_empty += 1
            
            else:
                if seats[ny][nx] in friends[index][1:]:
                    cnt_friends += 1 

    return (cnt_friends, cnt_empty)


def ride(index):
    friend = friends[index][0]
    
    # (친구수, 비어있는칸수, 행, 열)
    rv = [0, 0, -1, -1]

    for i in range(n):
        for j in range(n):
            if seats[i][j] == 0:
                cnt_friends, cnt_empty = count(index, (i, j))

                if cnt_friends > rv[0] or (cnt_friends == rv[0] and cnt_empty > rv[1]):
                    rv = (cnt_friends, cnt_empty, i, j)
                
                if rv[2:] == [-1, -1]:
                    rv[2], rv[3] = i, j
    
    seats[rv[2]][rv[3]] = friend

def cnt_friends(cur):
    cy, cx = cur

    cnt_friends = 0

    for zipped in zip(dy, dx):
        ny = cy + zipped[0]
        nx = cx + zipped[1]

        if 0 <= nx < n and 0 <= ny < n:
            if seats[ny][nx] in dict_friends.get(seats[cy][cx]):
                cnt_friends += 1 
    
    return cnt_friends

    
def get_score():
    total = 0
    for i in range(n):
        for j in range(n):
            cnt = cnt_friends((i, j))
            total += scores[cnt]

    return total

for i in range(n**2):
    dict_friends[friends[i][0]] = friends[i][1:] 
    ride(i)

print(get_score())