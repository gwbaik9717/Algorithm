def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        skill_list = list(skill)
        
        for char in tree:
            if char in skill:
                if char != skill_list.pop(0):
                    break
        else:
            answer += 1
                    
    
    return answer