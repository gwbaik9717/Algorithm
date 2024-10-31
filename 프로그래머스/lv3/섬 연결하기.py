def get_parent(a, parent):
    if parent[a] == a:
        return a 
    
    parent[a] = get_parent(parent[a], parent)
    return parent[a]

def union(a, b, parent):
    parent_a = get_parent(a, parent)
    parent_b = get_parent(b, parent)
    
    if parent_a < parent_b:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a

def is_cycle(a, b, parent):
    parent_a = get_parent(a, parent)
    parent_b = get_parent(b, parent)
    
    return parent_a == parent_b
        
def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    costs = sorted(costs, key=lambda x: x[-1])
    
    
    for start, end, cost in costs:
        if not is_cycle(start, end, parent):
            union(start, end, parent)
            answer += cost
        
    return answer