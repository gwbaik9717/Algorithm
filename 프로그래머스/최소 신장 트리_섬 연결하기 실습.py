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

def is_cycle(a, b, parent):
    return get_parent(a, parent) == get_parent(b, parent)
        
def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[-1])
    parent = [i for i in range(n)]
    
    for cost in costs:
        a, b, c = cost
        
        if is_cycle(a, b, parent):
            continue
        
        union(a, b, parent)
        answer += c
    
    return answer