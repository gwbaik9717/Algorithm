def solution(picks, minerals):
    answer = 0
    costs = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    n = len(minerals)
    
    grouped_minerals = []
    for i in range(0, n, 5):
        result = [0, 0, 0]
        for j in range(i, min(n, i+5)):
            if minerals[j] == "diamond":
                result[0] += 1
            elif minerals[j] == "iron":
                result[1] += 1
            else:
                result[2] += 1
        grouped_minerals.append(result)
    
    grouped_minerals = grouped_minerals[:sum(picks)]
    grouped_minerals.sort()
    
    current_pick = 0
    
    while grouped_minerals and sum(picks) > 0:
        cd, ci, cs = grouped_minerals.pop()
        
        while picks[current_pick] == 0: 
            current_pick += 1
        
        
        picks[current_pick] -= 1
        
        cost = costs[current_pick][0] * cd + costs[current_pick][1] * ci + costs[current_pick][2] * cs
        
        answer += cost

    
    return answer