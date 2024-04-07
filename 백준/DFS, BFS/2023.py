import sys, math
n = int(sys.stdin.readline().strip())

def is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False 
    return True

def dfs(num, len):
    if len == n:
        print(num)
        return
    

    for i in range(1, 10):
        new_num = int(str(num) + str(i))
        if is_prime(new_num):
            dfs(new_num, len + 1)

dfs(0, 0)