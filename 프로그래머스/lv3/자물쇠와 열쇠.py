from copy import deepcopy

def rotate_90(key):
    new_arr = deepcopy(key)
    
    n = len(key)
    
    for i in range(n):
        for j in range(n):
            ny, nx = j, n - 1 - i
            new_arr[ny][nx] = key[i][j]
            
    return new_arr

def check(start, key, lock, total):
    sy, sx = start
    m = len(key)
    n = len(lock)
    cnt = 0
    for i in range(m):
        for j in range(m):
            
            cy, cx = sy + i, sx + j

            if 0 <= cy <n and 0 <= cx < n:
                if lock[cy][cx] + key[cy - sy][cx - sx] == 2:
                    return False
                
                if key[cy - sy][cx - sx] == 1 and lock[cy][cx] == 0:
                    cnt += 1
    
    if cnt == total:
        # print(start, key)
        return True

    return False


def solution(key, lock):
    answer = True
    n = len(lock)
    m = len(key)
    rotations = []
    
    current_key = key
    for _ in range(4):
        rotations.append(current_key)
        current_key = rotate_90(current_key)
    
    total = 0
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                total += 1

    
    for rotation in rotations:
        for i in range(-(m-1), n):
            for j in range(-(m-1), n):
                if check((i, j), rotation, lock, total):
                    return True
    
    return False