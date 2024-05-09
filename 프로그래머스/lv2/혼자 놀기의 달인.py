from collections import Counter

def get_parent(start, a, parent, visited):
    
    visited[a] = 1
    
    if a == start:
        parent[start] = a
        return a
    
    parent[a] = get_parent(start, parent[a], parent, visited)
    return parent[a]

def solution(cards):
    answer = 0
    new_cards = list(map(lambda x: x - 1, cards))
    visited = [0] * len(cards)
    
    for i in range(len(cards)):
        if visited[i] == 0:
            visited[i] = 1
            get_parent(i, new_cards[i], new_cards, visited)
    
    counts = Counter(new_cards)
    
    sorted_counts = sorted(counts.values(),reverse=True)

    if len(sorted_counts) > 1:
        answer = sorted_counts[0] * sorted_counts[1]    
    

    return answer