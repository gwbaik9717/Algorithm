from collections import defaultdict

def solution(picks, minerals):
    answer = 0
    hps = [{"diamond": 1, "iron": 1, "stone": 1}, {"diamond": 5, "iron": 1, "stone": 1}, {"diamond": 25, "iron": 5, "stone": 1}]
    groups = []
    
    minerals = minerals[:sum(picks) * 5]
    
    for i, mineral in enumerate(minerals):
        if i % 5 == 0:
            mineral_dict = defaultdict(int)
            mineral_dict[mineral] += 1
            groups.append(mineral_dict)
        else:
            groups[-1][mineral] += 1
            
                
    sorted_groups = sorted(groups, key = lambda x: (x['diamond'], x['iron']), reverse=True)
    
    for group in sorted_groups:
        for i, pick in enumerate(picks):
            if pick > 0:
                hp = hps[i]
                for key in group:
                    answer += hp[key] * group[key]
                    
                picks[i] -= 1
                break
                
    return answer