def get_parent(a, parent):
    if a == parent[a]:
        return a
    
    parent[a] = get_parent(parent[a], parent)
    return parent[a]

def union(a, b, parent):
    parent_a = get_parent(a, parent)
    parent_b = get_parent(b, parent)
    
    if parent_a < parent_b:
        parent[parent_b] = parent_a 
    else:
        parent[parent_a] = parent_b

def solution(n, computers):
    answer = 0
    parent = [i for i in range(n)]
    
    for i, computer in enumerate(computers):
        for j, c in enumerate(computer):
            if i == j:
                continue
            if c == 1:
                union(i, j, parent)
    
    for i in range(n):
        get_parent(i, parent)
    
    answer = len(set(parent))
    
    
    return answer