import sys
sys.setrecursionlimit(10**9)

n, c = map(int, sys.stdin.readline().strip().split())
candidates = [int(sys.stdin.readline().strip()) for _ in range(n)]
sorted_candidates = sorted(candidates)

left, right = 0, sorted_candidates[-1] - sorted_candidates[0]

def is_possible(dist):
    answer = False

    def dfs(lv, start):
        nonlocal answer

        if lv == c:
            answer = True
            return
        
        for i in range(start + 1, n):
            if sorted_candidates[i] - sorted_candidates[start] >= dist:
                dfs(lv + 1, i)
                break
    
    dfs(1, 0)

    return answer

while left <= right:
    mid = (left + right) // 2
    
    if is_possible(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)