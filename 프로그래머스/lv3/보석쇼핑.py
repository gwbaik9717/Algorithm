from collections import defaultdict

def solution(gems):
    n = len(gems)
    answer = [1, n]
    left, right = 0, 0 
    
    setty = set()
    gem_dict = defaultdict(int)
    
    for gem in gems:
        setty.add(gem)
    
    kinds = len(setty)
    
    gem_dict[gems[0]] += 1
    
    while left < n and right < n :
        
        if len(gem_dict.keys()) == kinds:
            if right - left < answer[1] - answer[0]:
                answer = [left + 1, right + 1]
                
            gem_dict[gems[left]] -= 1

            if gem_dict[gems[left]] == 0:
                del gem_dict[gems[left]]

            left += 1   
        else:
            right += 1
            
            if right < n:
                gem_dict[gems[right]] += 1
        
    
    return answer